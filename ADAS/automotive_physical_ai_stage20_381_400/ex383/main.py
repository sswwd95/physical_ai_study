config={
"learning_rate":3e-4,
"n_steps":256,
"batch_size":64,
"n_epochs":10,
"gamma":0.99,
"gae_lambda":0.95,
"clip_range":0.2,
"ent_coef":0.0}
for k,v in config.items():
    print(k,v)
