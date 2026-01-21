import yaml
from core.registry import Registry
from core.timebase import TimeBase


class SimulationEngine:

    def __init__(self, config):
        self.config = config

        # --- Drone ---
        self.drone = Registry.drones[config.drone.model](config.drone)

        # --- Wind ---
        self.wind = Registry.winds[config.wind.model](config.wind)

        # --- Trajectory (NEW) ---
        with open(config.trajectory.file, "r") as f:
            traj_data = yaml.safe_load(f)

        traj_type = traj_data["type"]
        traj_params = traj_data.get("params", {})

        self.trajectory = Registry.trajectories[traj_type](traj_params)

        # --- Controller ---
        self.controller = Registry.controllers[config.control.strategy](config.control)

        # --- Estimator ---
        self.estimator = Registry.estimators[config.estimator.type](config.estimator)

        self.time = TimeBase(config.dt, config.duration)

    def run(self):
        for t in self.time:
            ref = self.trajectory.reference(t)
            u = self.controller.compute(ref, self.drone.state)
            w = self.wind.value(t)

            self.drone.step(u, w)

            measurements = self.drone.sensors.read()
            self.estimator.step(u, measurements)
