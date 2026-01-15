from typing import Dict, List
import numpy as np


class StandardScaler:
    """
    Standard scaler for time-series data.
    """

    def __init__(self):
        self.mean: Dict[str, np.ndarray] = {}
        self.std: Dict[str, np.ndarray] = {}

    def fit(self, trajectories: List[Dict[str, np.ndarray]]) -> None:
        for key in trajectories[0].keys():
            data = np.concatenate([t[key] for t in trajectories], axis=0)
            self.mean[key] = data.mean(axis=0)
            self.std[key] = data.std(axis=0) + 1e-8

    def transform(
        self, trajectories: List[Dict[str, np.ndarray]]
    ) -> List[Dict[str, np.ndarray]]:
        output = []
        for traj in trajectories:
            norm_traj = {}
            for key, value in traj.items():
                norm_traj[key] = (value - self.mean[key]) / self.std[key]
            output.append(norm_traj)
        return output
