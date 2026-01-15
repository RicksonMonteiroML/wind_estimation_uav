import numpy as np
from sensors.state import StateSensor


def test_state_sensor_shape():
    sensor = StateSensor()
    state = (
        np.zeros(3),
        np.zeros(3),
        np.array([1, 0, 0, 0]),
        np.zeros(3),
    )

    meas = sensor.measure(state)
    assert meas.shape == (13,)
