from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class DroneConfig:
    model: str
    mass: float
    inertia: list
    drag_coeffs: list


@dataclass
class WindConfig:
    model: str
    value: list


@dataclass
class ControlConfig:
    strategy: str
    params: Dict[str, Any]


@dataclass
class TrajectoryConfig:
    file: str

@dataclass
class EstimatorConfig:
    type: str
    params: Dict[str, Any]


@dataclass
class ExperimentConfig:
    name: str
    duration: float
    dt: float

    drone: DroneConfig
    wind: WindConfig
    control: ControlConfig
    trajectory: TrajectoryConfig
    estimator: EstimatorConfig
