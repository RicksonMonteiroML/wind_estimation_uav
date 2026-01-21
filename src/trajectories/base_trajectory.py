from abc import ABC, abstractmethod
import numpy as np
from typing import Dict


class TrajectoryBase(ABC):
    """
    Base class for reference trajectories.
    """

    def __init__(self, config: Dict):
        self.config = config

    @abstractmethod
    def reference(self, t: float) -> Dict[str, np.ndarray]:
        """
        Returns reference at time t.

        Expected keys:
        - position: np.ndarray (3,)
        - velocity: np.ndarray (3,)
        - acceleration: np.ndarray (3,) [optional]
        """
        pass
