import mujoco

print("MuJoCo version:", mujoco.__version__)
print("mjVERSION_HEADER:", mujoco.mjVERSION_HEADER)
assert mujoco.__version__.startswith("3.6."), "mujoco 3.6.x가 아닙니다."
