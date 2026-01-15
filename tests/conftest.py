import numpy as np
import pytest

# Simulator fixture (você já tem algo assim)
from physics.rigid_body import RigidBody6DOF
from physics.aerodynamics import AerodynamicModel
from physics.wind_model.constant_wind import ConstantWind
from sensors.imu import IMUSensor
from sensors.state import StateSensor
from simulation.custom_simulator import CustomSimulator

# EKF imports
from estimation.filters.ekf.ekf_wind import WindEKF
from estimation.filters.ekf.process_model import ProcessModel
from estimation.filters.ekf.measurement import MeasurementModel


@pytest.fixture
def ekf():
    dim = 6
    ekf = WindEKF(
        ProcessModel(Q=0.01 * np.eye(dim)),
        MeasurementModel(R=0.1 * np.eye(3)),
    )
    ekf.reset(
        x0=np.zeros(dim),
        P0=np.eye(dim),
    )
    return ekf

@pytest.fixture
def simulator():
    rb = RigidBody6DOF(
        mass=1.0,
        inertia=np.eye(3),
        gravity=np.array([0, 0, -9.81]),
    )

    aero = AerodynamicModel(drag_coeffs=np.array([0.1, 0.1, 0.2]))
    wind = ConstantWind(np.array([0.0, 0.0, 0.0]))

    imu = IMUSensor(noise_std=0.0)
    state_sensor = StateSensor()

    dt = 0.01
    initial_state = (
        np.zeros(3),
        np.zeros(3),
        np.array([1, 0, 0, 0]),
        np.zeros(3),
    )

    return CustomSimulator(
        rigid_body=rb,
        aero_model=aero,
        wind_model=wind,
        imu=imu,
        state_sensor=state_sensor,
        dt=dt,
        initial_state=initial_state,
    )
