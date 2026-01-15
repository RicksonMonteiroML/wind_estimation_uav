import numpy as np
from dataclasses import dataclass


@dataclass
class EKFState:
    """
    EKF augmented state.
    """
    x: np.ndarray   # state vector
    P: np.ndarray   # covariance
