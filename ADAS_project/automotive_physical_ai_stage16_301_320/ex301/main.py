from common.control_utils import PID
pid = PID(kp=1.0, ki=0.2, kd=0.05, output_limit=2.0)
for measurement in [0.0, 0.3, 0.7, 0.9]:
    output, error, integral, derivative = pid.update(1.0, measurement, 0.1)
    print(measurement, output, error, integral, derivative)
