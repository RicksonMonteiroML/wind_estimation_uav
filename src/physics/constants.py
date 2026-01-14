import numpy as np
from utils.types import Vector3

GRAVITY: Vector3 = np.array([0.0, 0.0, -9.81], dtype=float)
AIR_DENSITY: float = 1.225  # kg/m^3 (nível do mar)
