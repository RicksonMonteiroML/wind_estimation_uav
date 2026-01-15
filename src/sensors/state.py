import numpy as np
from typing import Tuple

# State6DOF = (p, v, q, w)
State6DOF = Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]


class StateSensor:
    """
    Simulated onboard state estimator (e.g., VIO/GPS + IMU fusion).

    Measures position, velocity, orientation and angular velocity,
    possibly corrupted by noise.
    """

    def __init__(
        self,
        position_noise_std: float = 0.0,
        velocity_noise_std: float = 0.0,
        orientation_noise_std: float = 0.0,
        angular_velocity_noise_std: float = 0.0,
    ):
        self.pos_std = position_noise_std
        self.vel_std = velocity_noise_std
        self.ori_std = orientation_noise_std
        self.ang_std = angular_velocity_noise_std

    def reset(self) -> State6DOF:
        """
        Returns a zero initial estimate.
        """
        return (
            np.zeros(3),                 # position
            np.zeros(3),                 # velocity
            np.array([1.0, 0.0, 0.0, 0.0]),  # unit quaternion
            np.zeros(3),                 # angular velocity
        )

    def measure(self, state: State6DOF) -> np.ndarray:
        """
        Returns a noisy estimate of the full state.

        Output shape: (13,)
        [p(3), v(3), q(4), w(3)]
        """
        p, v, q, w = state

        p_m = p + np.random.randn(3) * self.pos_std
        v_m = v + np.random.randn(3) * self.vel_std
        q_m = q + np.random.randn(4) * self.ori_std
        w_m = w + np.random.randn(3) * self.ang_std

        return np.concatenate([p_m, v_m, q_m, w_m])
