import numpy as np


class MeasurementModel:
    """
    Measurement model for EKF.
    """

    def __init__(self, R: np.ndarray):
        self.R = R

    def h(self, x: np.ndarray) -> np.ndarray:
        """
        Measurement function.
        Example: returns velocity estimate.
        """
        return x[:3]

    def H(self, x: np.ndarray) -> np.ndarray:
        """
        Jacobian of h.
        """
        H = np.zeros((3, len(x)))
        H[:, :3] = np.eye(3)
        return H
