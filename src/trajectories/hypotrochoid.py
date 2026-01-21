# src/trajectories/hypotrochoid.py
import numpy as np
from trajectories.base_trajectory import TrajectoryBase


class HypotrochoidTrajectory(TrajectoryBase):
    """
    Hypotrochoid trajectory in the XY plane.
    """

    def __init__(self, config):
        super().__init__(config)

        self.R = float(config.get("R", 2.0))
        self.r = float(config.get("r", 1.0))
        self.d = float(config.get("d", 0.5))
        self.omega = float(config.get("omega", 0.5))  # angular speed
        self.z = float(config.get("z", 0.0))

        self.k = (self.R - self.r) / self.r

    def reference(self, t: float):
        τ = self.omega * t

        # Position
        x = (self.R - self.r) * np.cos(τ) + self.d * np.cos(self.k * τ)
        y = (self.R - self.r) * np.sin(τ) - self.d * np.sin(self.k * τ)
        z = self.z

        # Velocity (first derivative)
        x_dot = (
            - (self.R - self.r) * self.omega * np.sin(τ)
            - self.d * self.k * self.omega * np.sin(self.k * τ)
        )
        y_dot = (
            (self.R - self.r) * self.omega * np.cos(τ)
            - self.d * self.k * self.omega * np.cos(self.k * τ)
        )
        z_dot = 0.0

        # Acceleration (second derivative)
        x_ddot = (
            - (self.R - self.r) * self.omega**2 * np.cos(τ)
            - self.d * self.k**2 * self.omega**2 * np.cos(self.k * τ)
        )
        y_ddot = (
            - (self.R - self.r) * self.omega**2 * np.sin(τ)
            + self.d * self.k**2 * self.omega**2 * np.sin(self.k * τ)
        )
        z_ddot = 0.0

        return {
            "position": np.array([x, y, z]),
            "velocity": np.array([x_dot, y_dot, z_dot]),
            "acceleration": np.array([x_ddot, y_ddot, z_ddot]),
        }
