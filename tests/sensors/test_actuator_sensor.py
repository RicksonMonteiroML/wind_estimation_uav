import numpy as np
from sensors.actuator import ActuatorSensor


def test_actuator_sensor():
    sensor = ActuatorSensor(noise_std=0.0)
    u = np.array([1.0, 2.0, 3.0])
    meas = sensor.measure(u)

    assert np.allclose(meas, u)
