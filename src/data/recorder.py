from typing import List, Dict, Any
import numpy as np


class DataRecorder:
    def __init__(self):
        self.records: List[Dict[str, Any]] = []

    def record(
        self,
        sensors: Dict[str, np.ndarray],
        control: np.ndarray,
        wind_gt: np.ndarray,
    ) -> None:
        self.records.append({
            "sensors": sensors,
            "control": control.copy(),
            "wind_gt": wind_gt.copy(),
        })

    def to_array(self) -> Dict[str, np.ndarray]:
        return {
            key: np.array([r[key] for r in self.records])
            for key in self.records[0]
        }
