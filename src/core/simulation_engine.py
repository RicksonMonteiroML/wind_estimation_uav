# src/core/simulation_engine.py
from core.registry import Registry
from core.timebase import TimeBase


class SimulationEngine:

    def __init__(self, config):
        self.config = config

        self.drone = Registry.drones[config.drone.model](config.drone)
        self.wind = Registry.winds[config.wind.model](config.wind)
        self.trajectory = Registry.trajectories[config.trajectory.type](config.trajectory)
        self.controller = Registry.controllers[config.control.strategy](config.control)
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
