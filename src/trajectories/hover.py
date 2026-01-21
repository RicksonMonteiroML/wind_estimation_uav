import numpy as np
from trajectories.base_trajectory import TrajectoryBase


class HoverTrajectory(TrajectoryBase):
    """
    Fixed hover at a given position.
    """

    def __init__(self, config):
        super().__init__(config)
        self.position = np.array(config.get("position", [0.0, 0.0, 0.0]))

    def reference(self, t: float):
        return {
            "position": self.position,
            "velocity": np.zeros(3),
            "acceleration": np.zeros(3),
        }
