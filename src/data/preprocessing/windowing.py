from typing import Tuple, List
import numpy as np


def build_windows(
    trajectories: List[dict],
    input_keys: List[str],
    target_key: str,
    window_size: int,
) -> Tuple[np.ndarray, np.ndarray]:
    X, y = [], []

    for traj in trajectories:
        inputs = np.concatenate(
            [traj[k] for k in input_keys], axis=1
        )
        targets = traj[target_key]

        T = inputs.shape[0]
        for t in range(window_size - 1, T):
            X.append(inputs[t - window_size + 1 : t + 1])
            y.append(targets[t])

    return np.array(X), np.array(y)
