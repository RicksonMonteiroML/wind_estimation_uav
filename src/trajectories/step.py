import numpy as np
from trajectories.base_trajectory import TrajectoryBase


class StepTrajectory(TrajectoryBase):
    """
    Step change in position at time t_step.
    """

    def __init__(self, config):
        super().__init__(config)
        self.p0 = np.array(config["p0"])
        self.p1 = np.array(config["p1"])
        self.t_step = float(config.get("t_step", 1.0))

    def reference(self, t: float):
        p = self.p1 if t >= self.t_step else self.p0
        return {
            "position": p,
            "velocity": np.zeros(3),
            "acceleration": np.zeros(3),
        }
