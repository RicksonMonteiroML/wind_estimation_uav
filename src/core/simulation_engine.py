class SimulationEngine:
    def __init__(self, config: ExperimentConfig):
        self.drone = DroneFactory.create(config.drone)
        self.trajectory = TrajectoryFactory.create(config.trajectory)
        self.controller = ControllerFactory.create(config.control)
        self.wind = WindFactory.create(config.wind)
        self.estimator = EstimatorFactory.create(config.estimator)

    def run(self):
        for t in timeline:
            ref = self.trajectory.reference(t)
            u = self.controller.compute(ref, self.drone.state)
            self.drone.step(u, self.wind.value(t))
            measurements = self.drone.sensors.read()
            self.estimator.step(u, measurements)
