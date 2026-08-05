import pymc as pm
import pytensor

print("PyMC:", pm.__version__)
print("PyTensor:", pytensor.__version__)
print("floatX:", pytensor.config.floatX)
