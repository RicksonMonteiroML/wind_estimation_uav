import numpy as np


class ActuatorSensor:
    """
    Represents actuator command measurement.

    Typically available onboard:
    - total thrust
    - body-frame force command
    """

    def __init__(self, noise_std: float = 0.0):
        self.noise_std = noise_std

    def measure(self, control_input: np.ndarray) -> np.ndarray:
        """
        Measures the applied control input.

        Parameters
        ----------
        control_input : np.ndarray
            Control command applied to the drone (e.g., body-frame force).

        Returns
        -------
        np.ndarray
            Noisy control measurement.
        """
        noise = np.random.randn(*control_input.shape) * self.noise_std
        return control_input + noise
