import numpy as np
from typing import Tuple


def run_ekf(
    ekf,
    stream_dataset,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Runs EKF on a sequential dataset and collects wind estimates.

    Returns
    -------
    y_hat : np.ndarray
        Estimated wind (T, 3)
    y_gt : np.ndarray
        Ground-truth wind (T, 3)
    """
    estimates = []
    gt = []

    for sample in stream_dataset:
        z = sample["measurement"]
        dt = sample["dt"]

        ekf.predict(u=None, dt=dt)
        ekf.update(z)

        estimates.append(ekf.get_state()[-3:])
        gt.append(sample["wind_gt"])

    return np.asarray(estimates), np.asarray(gt)
