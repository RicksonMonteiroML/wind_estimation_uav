from typing import List, Tuple
import numpy as np


def split_trajectories(
    trajectories: List,
    train_ratio: float,
    val_ratio: float,
    seed: int = 42,
) -> Tuple[List, List, List]:
    rng = np.random.default_rng(seed)
    indices = rng.permutation(len(trajectories))

    n = len(trajectories)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)

    train = [trajectories[i] for i in indices[:n_train]]
    val = [trajectories[i] for i in indices[n_train:n_train + n_val]]
    test = [trajectories[i] for i in indices[n_train + n_val:]]

    return train, val, test
