
class Registry:
    drones = {}
    winds = {}
    controllers = {}
    trajectories = {}
    estimators = {}

    @classmethod
    def register_drone(cls, name, constructor):
        cls.drones[name] = constructor

    @classmethod
    def register_wind(cls, name, constructor):
        cls.winds[name] = constructor

    @classmethod
    def register_controller(cls, name, constructor):
        cls.controllers[name] = constructor

    @classmethod
    def register_trajectory(cls, name, constructor):
        cls.trajectories[name] = constructor

    @classmethod
    def register_estimator(cls, name, constructor):
        cls.estimators[name] = constructor
