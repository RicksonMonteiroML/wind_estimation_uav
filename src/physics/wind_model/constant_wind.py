import numpy as np
from typing import Optional

from utils.types import Vector3
from physics.wind_model.base_wind_model import WindModel


class ConstantWind(WindModel):
    """
    Constant wind model.

    Represents a spatially uniform and time-invariant wind vector.
    """

    def __init__(self, wind_vector: Vector3):
        """
        Parameters
        ----------
        wind_vector : Vector3
            Constant wind velocity in world frame [m/s]
        """
        self._wind: Vector3 = np.asarray(wind_vector, dtype=float)

    def step(self, dt: float, airspeed: Optional[float] = None) -> None:
        """
        No internal dynamics.
        Method exists to satisfy the WindModel interface.
        """
        return None

    def get_wind(self) -> Vector3:
        """
        Returns
        -------
        wind : Vector3
            Constant wind vector [m/s]
        """
        return self._wind.copy()
