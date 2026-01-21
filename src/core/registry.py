class Registry:
    trajectories = {}
    controllers = {}
    drones = {}
    winds = {}
    estimators = {}

    @staticmethod
    def register_trajectory(name, cls):
        Registry.trajectories[name] = cls

    @staticmethod
    def register_controller(name, cls):
        Registry.controllers[name] = cls

    @staticmethod
    def register_drone(name, cls):
        Registry.drones[name] = cls

    @staticmethod
    def register_wind(name, cls):
        Registry.winds[name] = cls

    @staticmethod
    def register_estimator(name, cls):
        Registry.estimators[name] = cls
