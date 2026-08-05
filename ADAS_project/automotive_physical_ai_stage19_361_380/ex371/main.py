max_steps=300
for steps in [10,299,300,301]:
    truncated=steps>=max_steps
    print(steps,truncated)
