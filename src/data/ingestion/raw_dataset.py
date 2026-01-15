from typing import Dict, List
import numpy as np

Trajectory = Dict[str, np.ndarray]


class RawDataset:
    """
    Collection of full trajectories from simulation.
    """

    def __init__(self, trajectories: List[Trajectory]):
        self.trajectories = trajectories

    def __len__(self) -> int:
        return len(self.trajectories)

    def get(self, idx: int) -> Trajectory:
        return self.trajectories[idx]
