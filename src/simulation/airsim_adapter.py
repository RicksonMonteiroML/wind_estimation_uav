import numpy as np
from simulation.simulator_base import SimulatorBase
from utils.types import State6DOF, SensorDict, Vector3


class AirSimAdapter(SimulatorBase):
    """
    Adapter to make AirSim compatible with SimulatorBase.
    """

    def __init__(self, client):
        self.client = client

    def reset(self) -> None:
        self.client.reset()

    def step(self, control_input: Vector3) -> None:
        # Control mapping omitted (depends on AirSim config)
        self.client.moveByForceAsync(
            control_input[0],
            control_input[1],
            control_input[2],
            duration=0.01,
        ).join()

    def get_state(self) -> State6DOF:
        state = self.client.getMultirotorState()
        # Map AirSim state → State6DOF (explicit mapping)
        raise NotImplementedError

    def get_sensors(self) -> SensorDict:
        # IMU, GPS, etc.
        raise NotImplementedError

    def get_wind_ground_truth(self) -> Vector3:
        # AirSim wind is not ground truth unless explicitly set
        raise NotImplementedError
