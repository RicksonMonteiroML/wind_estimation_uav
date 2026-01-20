import numpy as np


class IMUSensor:
    """
    IMU sensor model.
    Measures specific force (linear acceleration without gravity).
    """

    def __init__(self, noise_std: float):
        self.noise_std = noise_std

    def measure(self, a_specific: np.ndarray) -> np.ndarray:
        """
        Parameters
        ----------
        a_specific : np.ndarray (3,)
            Specific force (acceleration without gravity) in world frame.
        """
        noise = np.random.randn(3) * self.noise_std
        return a_specific + noise
