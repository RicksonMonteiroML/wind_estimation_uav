import numpy as np

class MeasurementModel:
    """
    GPS velocity measurement model.
    z = [v_x, v_y, v_z]
    """

    def __init__(self, R: np.ndarray):
        self.R = R

    def h(self, x: np.ndarray) -> np.ndarray:
        return x[0:3]

    def H(self, x: np.ndarray) -> np.ndarray:
        H = np.zeros((3, 5))
        H[:, 0:3] = np.eye(3)
        return H
