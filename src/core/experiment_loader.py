import yaml
from core.experiment_config import (
    ExperimentConfig,
    DroneConfig,
    WindConfig,
    ControlConfig,
    TrajectoryConfig,
    EstimatorConfig,
)


class ExperimentLoader:

    @staticmethod
    def load(path: str) -> ExperimentConfig:
        with open(path, "r") as f:
            data = yaml.safe_load(f)

        return ExperimentConfig(
            name=data["experiment"]["name"],
            duration=data["experiment"]["duration"],
            dt=data["experiment"]["dt"],

            drone=DroneConfig(**data["drone"]),
            wind=WindConfig(**data["wind"]),
            control=ControlConfig(**data["control"]),
            trajectory=TrajectoryConfig(**data["trajectory"]),
            estimator=EstimatorConfig(**data["estimator"]),
        )
