from abc import ABC, abstractmethod
import numpy as np


class BaseModel(ABC):
    """
    Base interface for learning-based estimators.
    """

    @abstractmethod
    def predict(self, x: np.ndarray) -> np.ndarray:
        pass
