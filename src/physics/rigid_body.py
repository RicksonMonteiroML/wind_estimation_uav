import numpy as np
from typing import Tuple

from utils.types import State6DOF, Vector3
from physics.frames import quat_to_rotmat, quat_derivative, normalize_quat


class RigidBody6DOF:
    """
    6-DOF rigid body dynamics using Newton–Euler equations.
    """

    def __init__(self, mass: float, inertia: np.ndarray, gravity: Vector3):
        self.m: float = float(mass)
        self.J: np.ndarray = inertia
        self.g: Vector3 = gravity

    def step(
        self,
        state: State6DOF,
        forces_body: Vector3,
        torques_body: Vector3,
        dt: float,
    ) -> State6DOF:
        p, v, q, w = state

        R = quat_to_rotmat(q)

        # Translational dynamics
        p_dot: Vector3 = v
        v_dot: Vector3 = (R @ forces_body) / self.m + self.g

        # Rotational dynamics
        q_dot = quat_derivative(q, w)
        w_dot = np.linalg.inv(self.J) @ (
            torques_body - np.cross(w, self.J @ w)
        )

        # Integration (Euler explícito)
        p = p + p_dot * dt
        v = v + v_dot * dt
        q = normalize_quat(q + q_dot * dt)
        w = w + w_dot * dt

        return p, v, q, w
