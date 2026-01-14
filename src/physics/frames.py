import numpy as np
from utils.types import Quaternion, Vector3


def quat_to_rotmat(q: Quaternion) -> np.ndarray:
    w, x, y, z = q
    return np.array([
        [1 - 2*(y**2 + z**2), 2*(x*y - z*w),     2*(x*z + y*w)],
        [2*(x*y + z*w),     1 - 2*(x**2 + z**2), 2*(y*z - x*w)],
        [2*(x*z - y*w),     2*(y*z + x*w),     1 - 2*(x**2 + y**2)]
    ])


def normalize_quat(q: Quaternion) -> Quaternion:
    return q / np.linalg.norm(q)


def quat_derivative(q: Quaternion, omega: Vector3) -> Quaternion:
    wx, wy, wz = omega
    Omega = np.array([
        [0.0, -wx, -wy, -wz],
        [wx,  0.0,  wz, -wy],
        [wy, -wz,  0.0,  wx],
        [wz,  wy, -wx,  0.0],
    ])
    return 0.5 * Omega @ q
