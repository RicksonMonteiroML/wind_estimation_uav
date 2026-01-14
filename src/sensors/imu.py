import numpy as np
from utils.types import State6DOF


class IMUSensor:
    def __init__(self, noise_std: float):
        self.noise_std = noise_std

    def measure(self, state: State6DOF) -> np.ndarray:
        _, v, _, w = state
        noise = np.random.randn(6) * self.noise_std
        return np.hstack((v, w)) + noise
