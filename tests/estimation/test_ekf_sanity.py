import numpy as np
from estimation.filters.ekf.ekf_wind import WindEKF
from estimation.filters.ekf.process_model import ProcessModel
from estimation.filters.ekf.measurement import MeasurementModel


def test_ekf_stability():
    dim = 6
    ekf = WindEKF(
        ProcessModel(Q=0.01 * np.eye(dim)),
        MeasurementModel(R=0.1 * np.eye(3)),
    )

    ekf.reset(np.zeros(dim), np.eye(dim))

    for _ in range(50):
        ekf.predict(u=None, dt=0.01)
        ekf.update(np.zeros(3))

    assert np.all(np.isfinite(ekf.get_state()))
