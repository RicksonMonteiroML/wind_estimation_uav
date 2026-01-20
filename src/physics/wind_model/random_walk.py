import numpy as np
from typing import Optional

from utils.types import Vector3
from physics.wind_model.base_wind_model import WindModel


class RandomWalkWind(WindModel):
    """
    Random-walk wind model.

    Wind evolves as a continuous-time random walk:
        w_dot = eta,   eta ~ N(0, sigma^2)
    """

    def __init__(self, sigma: float):
        """
        Parameters
        ----------
        sigma : float
            Standard deviation of the wind rate [m/s^(3/2)]
        """
        self.sigma: float = float(sigma)
        self._wind: Vector3 = np.zeros(3, dtype=float)

    def step(self, dt: float, airspeed: Optional[float] = None) -> None:
        """
        Propagates the wind state.

        Parameters
        ----------
        dt : float
            Simulation timestep [s]
        airspeed : Optional[float]
            Unused (kept for interface compatibility)
        """
        noise: Vector3 = np.random.randn(3) * self.sigma * np.sqrt(dt)
        self._wind += noise

    def get_wind(self) -> Vector3:
        """
        Returns
        -------
        wind : Vector3
            Wind velocity in world frame [m/s]
        """
        return self._wind.copy()
