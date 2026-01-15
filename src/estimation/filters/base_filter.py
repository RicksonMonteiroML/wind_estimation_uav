from abc import ABC, abstractmethod
import numpy as np


class BaseFilter(ABC):
    """
    Base interface for recursive state estimators (EKF, UKF, PF).
    """

    @abstractmethod
    def reset(self, x0: np.ndarray, P0: np.ndarray) -> None:
        pass

    @abstractmethod
    def predict(self, u: np.ndarray, dt: float) -> None:
        pass

    @abstractmethod
    def update(self, z: np.ndarray) -> None:
        pass

    @abstractmethod
    def get_state(self) -> np.ndarray:
        pass
