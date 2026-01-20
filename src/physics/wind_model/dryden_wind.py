import numpy as np
from typing import Optional

from utils.types import Vector3
from physics.wind_model.base_wind_model import WindModel

class DrydenWind(WindModel):
    """
    Dryden turbulence wind model.

    Implements a continuous-time Dryden spectral model using
    linear stochastic differential equations.
    """

    def __init__(
        self,
        Lu: float,
        Lv: float,
        Lw: float,
        sigma_u: float,
        sigma_v: float,
        sigma_w: float,
        nominal_airspeed: float = 1.0,
    ):
        """
        Parameters
        ----------
        Lu, Lv, Lw : float
            Turbulence scale lengths [m]
        sigma_u, sigma_v, sigma_w : float
            Turbulence intensities [m/s]
        nominal_airspeed : float
            Reference airspeed used if none is provided [m/s]
        """
        self.Lu: float = float(Lu)
        self.Lv: float = float(Lv)
        self.Lw: float = float(Lw)

        self.su: float = float(sigma_u)
        self.sv: float = float(sigma_v)
        self.sw: float = float(sigma_w)

        self.V_ref: float = max(float(nominal_airspeed), 0.1)

        # Internal filter states
        self._xu: float = 0.0
        self._xv: float = 0.0
        self._xw: Vector3 = np.zeros(2, dtype=float)

    def step(self, dt: float, airspeed: Optional[float] = None) -> None:
        """
        Advances the Dryden wind model.

        Parameters
        ----------
        dt : float
            Simulation timestep [s]
        airspeed : Optional[float]
            Reference airspeed for spectral scaling [m/s]
        """
        V: float = max(airspeed if airspeed is not None else self.V_ref, 0.1)

        # White noise inputs
        nu: float = np.random.randn()
        nv: float = np.random.randn()
        nw: float = np.random.randn()

        # Longitudinal (u) component — 1st order
        au: float = -V / self.Lu
        bu: float = self.su * np.sqrt(2.0 * V / self.Lu)
        self._xu += (au * self._xu + bu * nu) * dt

        # Lateral (v) component — 1st order
        av: float = -V / self.Lv
        bv: float = self.sv * np.sqrt(2.0 * V / self.Lv)
        self._xv += (av * self._xv + bv * nv) * dt

        # Vertical (w) component — 2nd order
        aw: float = -V / self.Lw
        bw: float = self.sw * np.sqrt(2.0 * V / self.Lw)

        xw1, xw2 = self._xw
        xw1_dot: float = xw2
        xw2_dot: float = -2.0 * aw * xw2 - (aw ** 2) * xw1 + bw * nw

        self._xw[0] += xw1_dot * dt
        self._xw[1] += xw2_dot * dt

    def get_wind(self) -> Vector3:
        """
        Returns
        -------
        wind : Vector3
            Dryden wind velocity in world frame [m/s]
        """
        return np.array(
            [self._xu, self._xv, self._xw[0]],
            dtype=float
        )
