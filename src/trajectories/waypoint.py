# src/trajectories/waypoint.py
import numpy as np
from trajectories.base_trajectory import TrajectoryBase


class WaypointTrajectory(TrajectoryBase):
    """
    Piecewise constant waypoint trajectory.
    """

    def __init__(self, config):
        super().__init__(config)
        self.waypoints = [
            (float(wp["t"]), np.array(wp["position"]))
            for wp in config["waypoints"]
        ]

    def reference(self, t: float):
        pos = self.waypoints[0][1]
        for wp_t, wp_p in self.waypoints:
            if t >= wp_t:
                pos = wp_p
            else:
                break

        return {
            "position": pos,
            "velocity": np.zeros(3),
            "acceleration": np.zeros(3),
        }
