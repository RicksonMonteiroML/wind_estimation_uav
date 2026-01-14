import numpy as np
from utils.types import Vector3


class AerodynamicModel:
    """
    Linear aerodynamic drag model.
    """

    def __init__(self, drag_coeffs: Vector3):
        self.D: np.ndarray = np.diag(drag_coeffs)

    def compute_force(self, v_rel: Vector3) -> Vector3:
        """
        Computes aerodynamic force in body frame.

        Parameters
        ----------
        v_rel : Vector3
            Air-relative velocity in body frame [m/s]
        """
        return -self.D @ v_rel
