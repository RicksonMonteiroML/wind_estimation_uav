import numpy as np
from estimation.filters.base_filter import BaseFilter
from estimation.filters.ekf.state import EKFState
from estimation.filters.ekf.process_model import ProcessModel
from estimation.filters.ekf.measurement import MeasurementModel


class WindEKF(BaseFilter):
    """
    Extended Kalman Filter for wind estimation.
    """

    def __init__(
        self,
        process_model: ProcessModel,
        measurement_model: MeasurementModel,
    ):
        self.pm = process_model
        self.mm = measurement_model
        self.state: EKFState | None = None

    def reset(self, x0: np.ndarray, P0: np.ndarray) -> None:
        self.state = EKFState(x=x0, P=P0)

    def predict(self, u: np.ndarray, dt: float) -> None:
        x, P = self.state.x, self.state.P

        x_pred = self.pm.f(x, u, dt)
        F = self.pm.F(x, u, dt)
        P_pred = F @ P @ F.T + self.pm.Q

        self.state = EKFState(x=x_pred, P=P_pred)

    def update(self, z: np.ndarray) -> None:
        x, P = self.state.x, self.state.P

        y = z - self.mm.h(x)
        H = self.mm.H(x)
        S = H @ P @ H.T + self.mm.R
        K = P @ H.T @ np.linalg.inv(S)

        x_upd = x + K @ y
        P_upd = (np.eye(len(x)) - K @ H) @ P

        self.state = EKFState(x=x_upd, P=P_upd)

    def get_state(self) -> np.ndarray:
        return self.state.x
