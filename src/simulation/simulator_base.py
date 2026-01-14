from abc import ABC, abstractmethod
from typing import Dict
import numpy as np

from utils.types import State6DOF, SensorDict, Vector3


class SimulatorBase(ABC):
    """
    Abstract interface for UAV simulators.
    """

    @abstractmethod
    def reset(self) -> None:
        """
        Resets the simulator to its initial state.
        """
        pass

    @abstractmethod
    def step(self, control_input: Vector3) -> None:
        """
        Advances the simulation by one timestep.

        Parameters
        ----------
        control_input : Vector3
            Control force expressed in body frame [N]
        """
        pass

    @abstractmethod
    def get_state(self) -> State6DOF:
        """
        Returns the true continuous system state.
        """
        pass

    @abstractmethod
    def get_sensors(self) -> SensorDict:
        """
        Returns simulated sensor measurements.
        """
        pass

    @abstractmethod
    def get_wind_ground_truth(self) -> Vector3:
        """
        Returns ground-truth wind in world frame.
        """
        pass
