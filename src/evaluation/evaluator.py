from typing import Dict
import numpy as np
from evaluation.metrics import rmse, angular_error


class Evaluator:
    def evaluate(self, y_hat: np.ndarray, y: np.ndarray) -> Dict[str, float]:
        return {
            "rmse": rmse(y_hat, y),
            "angular_error": angular_error(y_hat, y),
        }
