from core.registry import Registry
from trajectories.hover import HoverTrajectory
from trajectories.step import StepTrajectory
from trajectories.waypoint import WaypointTrajectory
from trajectories.hypotrochoid import HypotrochoidTrajectory

Registry.register_trajectory("hover", HoverTrajectory)
Registry.register_trajectory("step", StepTrajectory)
Registry.register_trajectory("waypoint", WaypointTrajectory)
Registry.register_trajectory("hypotrochoid", HypotrochoidTrajectory)