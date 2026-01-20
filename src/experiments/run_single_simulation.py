import numpy as np
import os

from utils.serialization import save_object

from physics.rigid_body import RigidBody6DOF
from physics.aerodynamics import AerodynamicModel
from physics.wind_model.constant_wind import ConstantWind

from simulation.custom_simulator import CustomSimulator
from sensors.imu import IMUSensor
from sensors.state import StateSensor

from estimation.filters.ekf.ekf_wind import WindEKF
from estimation.filters.ekf.process_model import ProcessModel
from estimation.filters.ekf.measurement import MeasurementModel

RESULTS_PATH = "results"


def main():
    # =====================================================
    # 1. Physical setup
    # =====================================================
    rb = RigidBody6DOF(
        mass=1.0,
        inertia=np.eye(3),
        gravity=np.array([0, 0, -9.81]),
    )

    aero = AerodynamicModel(drag_coeffs=np.array([0.1, 0.1, 0.2]))
    wind_model = ConstantWind(np.array([1.0, 0.0, 0.0]))

    imu = IMUSensor(noise_std=0.01)
    state_sensor = StateSensor(velocity_noise_std=0.05)

    dt = 0.01

    initial_state = (
        np.zeros(3),              # position
        np.zeros(3),              # velocity
        np.array([1, 0, 0, 0]),    # quaternion
        np.zeros(3),              # angular velocity
    )

    sim = CustomSimulator(
        rigid_body=rb,
        aero_model=aero,
        wind_model=wind_model,
        imu=imu,
        state_sensor=state_sensor,
        dt=dt,
        initial_state=initial_state,
    )

    # =====================================================
    # 2. EKF setup (OPTION A: horizontal wind only)
    # =====================================================
    Q = np.diag([
        0.02, 0.02, 0.05,   # v_x, v_y, v_z
        0.05,  0.05           # w_x, w_y  (↑ para convergência mais rápida)
    ])

    R = 0.05 * np.eye(3)

    process_model = ProcessModel(
        Q=Q,
        mass=rb.m,
        drag_coeffs_xy=np.array([0.3, 0.3]),
    )

    measurement_model = MeasurementModel(R)

    ekf = WindEKF(process_model, measurement_model)
    ekf.reset(np.zeros(5), np.eye(5))

    # =====================================================
    # 3. Logging
    # =====================================================
    log = {
        "time": [],
        "state_gt": [],
        "state_meas": [],
        "imu": [],
        "control": [],
        "wind_gt": [],
        "wind_ekf": [],
    }

    sim.reset()

    # =====================================================
    # 4. Simulation loop
    # =====================================================
    for k in range(5000):
        t = k * dt

        # --- Small horizontal excitation (critical) ---
        if 0.0 < t < 2.0:
            u = np.array([
                # 0.3 * np.sin(1.0 * t),     # thrust X
                0.3,     # thrust X
                0.0,     # thrust Y
                rb.m * np.linalg.norm(rb.g)
            ])
        else:
                
            u = np.array([
                0.0,     # thrust X
                0.0,                       # thrust Y
                rb.m * np.linalg.norm(rb.g)
            ])

        sim.step(u)

        state_gt = sim.get_state()
        sensors = sim.get_sensors()
        wind_gt = sim.get_wind_ground_truth()

        a_imu = sensors["imu"]            # (3,)
        z = sensors["state"][3:6]         # GPS velocity

        ekf.predict(u=a_imu, dt=dt)
        ekf.update(z)

        wind_ekf = ekf.get_state()[3:5]   # w_x, w_y

        log["time"].append(t)
        log["state_gt"].append(state_gt)
        log["state_meas"].append(sensors["state"])
        log["imu"].append(a_imu)
        log["control"].append(u)
        log["wind_gt"].append(wind_gt[:2])
        log["wind_ekf"].append(wind_ekf)

    # =====================================================
    # 5. Save results
    # =====================================================
    os.makedirs(RESULTS_PATH, exist_ok=True)
    save_object(
        log,
        os.path.join(RESULTS_PATH, "single_simulation_log.pkl"),
    )


if __name__ == "__main__":
    main()
