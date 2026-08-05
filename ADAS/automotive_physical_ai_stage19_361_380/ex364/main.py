from common.rl_utils import normalize,denormalize
speed=1.2
normalized=normalize(speed,0.0,2.0)
restored=denormalize(normalized,0.0,2.0)
print(speed,normalized,restored)
