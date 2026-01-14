from abc import ABC, abstractmethod
from typing import Optional
import numpy as np

from utils.types import Vector3


class WindModel(ABC):
    """
    Abstract base class for wind models.
    Wind is always expressed in the world frame.
    """

    @abstractmethod
    def step(self, dt: float, airspeed: Optional[float] = None) -> None:
        """
        Advances the internal wind state.

        Parameters
        ----------
        dt : float
            Simulation timestep [s]
        airspeed : Optional[float]
            Reference airspeed for turbulence scaling (used by Dryden)
        """
        pass

    @abstractmethod
    def get_wind(self) -> Vector3:
        """
        Returns
        -------
        wind : Vector3
            Wind velocity in world frame [m/s]
        """
        pass
