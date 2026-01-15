import numpy as np


class ProcessModel:
    """
    Process model for EKF with wind as random walk.
    """

    def __init__(self, Q: np.ndarray):
        self.Q = Q

    def f(self, x: np.ndarray, u: np.ndarray, dt: float) -> np.ndarray:
        """
        State propagation model.
        Simplified: wind follows random walk.
        """
        x_pred = x.copy()
        # wind is last 3 states
        # w_k+1 = w_k
        return x_pred

    def F(self, x: np.ndarray, u: np.ndarray, dt: float) -> np.ndarray:
        """
        Jacobian of f w.r.t state.
        """
        return np.eye(len(x))
