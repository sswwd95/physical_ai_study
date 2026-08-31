"""작은 1차원 Grid World로 Q-learning의 업데이트 흐름을 확인하는 예제."""
import random
import numpy as np

N_STATES = 6
GOAL = N_STATES - 1
ACTIONS = (-1, 1)


def step(state: int, action: int):
    next_state = min(max(state + action, 0), GOAL)
    reward = 1.0 if next_state == GOAL else -0.01
    done = next_state == GOAL
    return next_state, reward, done


def train(episodes=500, alpha=0.2, gamma=0.95, epsilon=0.2):
    q = np.zeros((N_STATES, len(ACTIONS)))

    for _ in range(episodes):
        state = 0
        for _ in range(50):
            if random.random() < epsilon:
                action_idx = random.randrange(len(ACTIONS))
            else:
                action_idx = int(np.argmax(q[state]))

            next_state, reward, done = step(state, ACTIONS[action_idx])
            target = reward if done else reward + gamma * np.max(q[next_state])
            q[state, action_idx] += alpha * (target - q[state, action_idx])
            state = next_state
            if done:
                break
    return q


if __name__ == "__main__":
    q_table = train()
    print(np.round(q_table, 3))
