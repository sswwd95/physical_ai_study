import math
import numpy as np
try:
    import gymnasium as gym
    from gymnasium import spaces
except ImportError:
    gym = None
    spaces = None

class SimpleCarEnv:
    metadata = {"render_modes": []}

    def __init__(self, max_steps=300, dt=0.1, seed=42):
        if gym is None:
            raise ImportError("Install gymnasium using environment.yml")
        self.max_steps = int(max_steps)
        self.dt = float(dt)
        self.rng = np.random.default_rng(seed)
        self.observation_space = spaces.Box(
            low=np.array([-5.0, -3.0, -math.pi, 0.0, 0.0], dtype=np.float32),
            high=np.array([5.0, 3.0, math.pi, 2.0, 20.0], dtype=np.float32),
            dtype=np.float32,
        )
        self.action_space = spaces.Box(
            low=np.array([-1.0, -1.0], dtype=np.float32),
            high=np.array([1.0, 1.0], dtype=np.float32),
            dtype=np.float32,
        )
        self.state = None
        self.steps = 0

    def _get_obs(self):
        return self.state.astype(np.float32)

    def reset(self, seed=None, options=None):
        if seed is not None:
            self.rng = np.random.default_rng(seed)
        lateral_error = self.rng.uniform(-1.0, 1.0)
        heading_error = self.rng.uniform(-0.3, 0.3)
        speed = self.rng.uniform(0.2, 0.8)
        obstacle_distance = self.rng.uniform(8.0, 18.0)
        self.state = np.array(
            [0.0, lateral_error, heading_error, speed, obstacle_distance],
            dtype=np.float32
        )
        self.steps = 0
        return self._get_obs(), {"reset_seed": seed}

    def step(self, action):
        action = np.clip(np.asarray(action, dtype=np.float32), -1.0, 1.0)
        throttle, steering = float(action[0]), float(action[1])
        x, lateral_error, heading_error, speed, obstacle_distance = self.state

        accel = 1.2 * throttle - 0.25 * speed
        yaw_rate = 1.4 * steering
        speed = float(np.clip(speed + accel*self.dt, 0.0, 2.0))
        heading_error = float(np.clip(heading_error + yaw_rate*self.dt, -math.pi, math.pi))
        x += speed * math.cos(heading_error) * self.dt
        lateral_error += speed * math.sin(heading_error) * self.dt
        obstacle_distance -= speed * self.dt

        progress_reward = speed * self.dt
        lane_penalty = 1.5 * abs(lateral_error)
        heading_penalty = 0.4 * abs(heading_error)
        action_penalty = 0.05 * float(np.sum(action**2))
        collision = obstacle_distance <= 0.5
        lane_departure = abs(lateral_error) >= 2.5

        reward = progress_reward - lane_penalty - heading_penalty - action_penalty
        if collision:
            reward -= 25.0
        if lane_departure:
            reward -= 15.0

        self.state = np.array(
            [x, lateral_error, heading_error, speed, obstacle_distance],
            dtype=np.float32
        )
        self.steps += 1
        terminated = bool(collision or lane_departure)
        truncated = bool(self.steps >= self.max_steps)
        info = {
            "collision": collision,
            "lane_departure": lane_departure,
            "progress_reward": progress_reward,
            "lane_penalty": lane_penalty,
            "heading_penalty": heading_penalty,
            "action_penalty": action_penalty,
        }
        return self._get_obs(), float(reward), terminated, truncated, info

    def close(self):
        pass
