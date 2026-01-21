import yaml
from core.experiment_config import ExperimentConfig, ModuleConfig


class ExperimentLoader:

    @staticmethod
    def load(path: str) -> ExperimentConfig:
        with open(path, "r") as f:
            data = yaml.safe_load(f)

        exp = data["experiment"]

        return ExperimentConfig(
            name=exp["name"],
            duration=exp["duration"],
            dt=exp["dt"],

            trajectory=ModuleConfig(**data["trajectory"]),
            control=ModuleConfig(**data["control"]),
            drone=ModuleConfig(**data["drone"]),
            wind=ModuleConfig(**data["wind"]),
            estimator=ModuleConfig(**data["estimator"]),
        )
