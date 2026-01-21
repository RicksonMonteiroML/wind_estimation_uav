from dataclasses import dataclass


@dataclass
class ModuleConfig:
    file: str


@dataclass
class ExperimentConfig:
    name: str
    duration: float
    dt: float

    trajectory: ModuleConfig
    control: ModuleConfig
    drone: ModuleConfig
    wind: ModuleConfig
    estimator: ModuleConfig
