import numpy as np
from typing import Dict

from simulation.simulator_base import SimulatorBase
from physics.rigid_body import RigidBody6DOF
from physics.aerodynamics import AerodynamicModel
from physics.wind_model.base_wind_model import WindModel
from physics.frames import quat_to_rotmat
from sensors.imu import IMUSensor
from sensors.state import StateSensor
from utils.types import State6DOF, SensorDict, Vector3


class CustomSimulator(SimulatorBase):
    """
    Physics-based UAV simulator using a custom 6-DOF model.
    Provides true acceleration and consistent IMU measurements.
    """

    def __init__(
        self,
        rigid_body: RigidBody6DOF,
        aero_model: AerodynamicModel,
        wind_model: WindModel,
        imu: IMUSensor,
        state_sensor: StateSensor,
        dt: float,
        initial_state: State6DOF,
    ):
        self.rb = rigid_body
        self.aero = aero_model
        self.wind = wind_model
        self.imu = imu
        self.state_sensor = state_sensor
        self.dt = float(dt)
        self._initial_state = initial_state
        self.state = initial_state

        # Stores true linear acceleration in world frame (including gravity)
        self._last_acc_world = np.zeros(3)

    def reset(self) -> None:
        self.state = self._initial_state
        self.wind.step(0.0)
        self._last_acc_world = np.zeros(3)

    def step(self, control_input: Vector3) -> None:
        """
        Parameters
        ----------
        control_input : Vector3
            Thrust force in body frame [N]
        """
        p, v, q, w = self.state

        # Update wind model
        self.wind.step(self.dt)

        # Rotation matrices
        R_wb = quat_to_rotmat(q)   # body -> world
        R_bw = R_wb.T              # world -> body

        # Wind and relative air velocity (body frame)
        wind_world = self.wind.get_wind()
        v_rel_body = R_bw @ (v - wind_world)

        # Aerodynamic force (body frame)
        f_aero_body = self.aero.compute_force(v_rel_body)

        # Total forces and torques (body frame)
        total_force_body = control_input + f_aero_body
        total_torque_body = np.zeros(3)

        # ---- True acceleration (world frame, INCLUDING gravity) ----
        total_force_world = R_wb @ total_force_body
        self._last_acc_world = (
            total_force_world / self.rb.m + self.rb.g
        )
        # ------------------------------------------------------------

        # Integrate rigid-body dynamics
        self.state = self.rb.step(
            self.state,
            total_force_body,
            total_torque_body,
            self.dt,
        )

    def get_state(self) -> State6DOF:
        return self.state

    def get_true_acceleration(self) -> Vector3:
        """
        Returns true linear acceleration in world frame (includes gravity).
        """
        return self._last_acc_world

    def get_sensors(self) -> SensorDict:
        """
        Returns sensor measurements.
        IMU measures specific force (acceleration without gravity).
        State sensor provides position/velocity.
        """
        a_true = self.get_true_acceleration()
        a_specific = a_true - self.rb.g
        imu_meas = self.imu.measure(a_specific)

        return {
            "imu": imu_meas,
            "state": self.state_sensor.measure(self.state),
        }

    def get_wind_ground_truth(self) -> Vector3:
        return self.wind.get_wind()
