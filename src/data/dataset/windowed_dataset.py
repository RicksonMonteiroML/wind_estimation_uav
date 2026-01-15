import numpy as np
from typing import Tuple


class WindowedDataset:
    """
    Dataset of fixed-length temporal windows for supervised learning.

    Each sample:
        X: (window_size, feature_dim)
        y: (target_dim,)
    """

    def __init__(self, X: np.ndarray, y: np.ndarray):
        """
        Parameters
        ----------
        X : np.ndarray
            Shape (N, L, D)
        y : np.ndarray
            Shape (N, target_dim)
        """
        self.X = X
        self.y = y

    def __len__(self) -> int:
        return self.X.shape[0]

    def __getitem__(self, idx: int) -> Tuple[np.ndarray, np.ndarray]:
        return self.X[idx], self.y[idx]
