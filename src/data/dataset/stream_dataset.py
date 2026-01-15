from typing import Dict, Iterator
import numpy as np


class StreamDataset:
    """
    Sequential dataset for recursive estimators (EKF).
    """

    def __init__(self, trajectory: Dict[str, np.ndarray]):
        self.trajectory = trajectory
        self.length = next(iter(trajectory.values())).shape[0]

    def __iter__(self) -> Iterator[Dict[str, np.ndarray]]:
        for t in range(self.length):
            yield {k: v[t] for k, v in self.trajectory.items()}
