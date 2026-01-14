from typing import Tuple, Dict, Any
import numpy as np

Vector3 = np.ndarray          # shape: (3,)
Quaternion = np.ndarray      # shape: (4,)
State6DOF = Tuple[
    Vector3,   # position
    Vector3,   # velocity
    Quaternion,
    Vector3    # angular velocity
]

SensorDict = Dict[str, np.ndarray]