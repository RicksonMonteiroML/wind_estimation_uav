import yaml
from core.registry import Registry


def load_module(file_path: str, registry: dict):
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)

    module_type = data["type"]
    params = data.get("params", {})

    return registry[module_type](params)


class SimulationEngine:

    def __init__(self, config):
        self.config = config

        # --- Load modules ---
        self.drone = load_module(
            config.drone.file, Registry.drones
        )

        self.wind = load_module(
            config.wind.file, Registry.winds
        )

        self.trajectory = load_module(
            config.trajectory.file, Registry.trajectories
        )

        self.controller = load_module(
            config.control.file, Registry.controllers
        )

        self.estimator = load_module(
            config.estimator.file, Registry.estimators
        )

        self.dt = config.dt
        self.duration = config.duration
