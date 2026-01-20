import numpy as np

class ProcessModel:
    """
    EKF process model with horizontal wind only (w_x, w_y).
    """

    def __init__(self, Q: np.ndarray, mass: float, drag_coeffs_xy: np.ndarray):
        """
        drag_coeffs_xy : np.ndarray (2,)
            Drag coefficients for X and Y axes.
        """
        self.Q = Q
        self.m = mass
        self.D_xy = np.diag(drag_coeffs_xy)

    def f(self, x: np.ndarray, a_imu: np.ndarray, dt: float) -> np.ndarray:
        # State unpacking
        v = x[0:3]        # v_x, v_y, v_z
        w_xy = x[3:5]     # w_x, w_y

        # Relative velocity in XY
        v_rel_xy = v[0:2] - w_xy

        # Drag acceleration in XY only
        drag_acc_xy = -(self.D_xy @ v_rel_xy) / self.m

        # Full acceleration
        a = a_imu.copy()
        a[0:2] += drag_acc_xy   # drag only in X/Y

        # Integrate
        v_next = v + dt * a
        w_next = w_xy           # random walk

        return np.hstack([v_next, w_next])

    def F(self, x: np.ndarray, a_imu: np.ndarray, dt: float) -> np.ndarray:
        F = np.eye(5)

        # ∂v_xy / ∂v_xy
        F[0:2, 0:2] += -dt * self.D_xy / self.m

        # ∂v_xy / ∂w_xy
        F[0:2, 3:5] += dt * self.D_xy / self.m

        return F
