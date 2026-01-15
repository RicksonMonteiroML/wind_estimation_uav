import numpy as np
from estimation.models.base_model import BaseModel


class PersistenceModel(BaseModel):
    """
    w_hat(t) = w_hat(t-1)
    """

    def __init__(self):
        self.last = np.zeros(3)

    def predict(self, x: np.ndarray) -> np.ndarray:
        return self.last

    def update(self, w: np.ndarray) -> None:
        self.last = w.copy()
