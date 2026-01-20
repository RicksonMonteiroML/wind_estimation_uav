import numpy as np
from data.preprocessing.windowing import build_windows


def test_windowing_shapes():
    traj = {
        "imu": np.random.randn(100, 6),
        "state": np.random.randn(100, 6),
        "wind_gt": np.random.randn(100, 3),
    }

    X, y = build_windows(
        [traj],
        input_keys=["imu", "state"],
        target_key="wind_gt",
        window_size=10,
    )

    assert X.shape[1] == 10
    assert y.shape[1] == 3
