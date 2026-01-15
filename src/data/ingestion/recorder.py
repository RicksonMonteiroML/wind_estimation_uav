from typing import Dict, Any, List
import numpy as np


class DataRecorder:
    """
    Records raw simulation data over time.
    """

    def __init__(self):
        self._records: List[Dict[str, Any]] = []

    def record(
        self,
        sensors: Dict[str, np.ndarray],
        control: np.ndarray,
        wind_gt: np.ndarray,
    ) -> None:
        self._records.append({
            "sensors": {k: v.copy() for k, v in sensors.items()},
            "control": control.copy(),
            "wind_gt": wind_gt.copy(),
        })

    def get_records(self) -> List[Dict[str, Any]]:
        return self._records
