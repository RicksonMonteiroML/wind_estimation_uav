import numpy as np


def rmse(y_hat: np.ndarray, y: np.ndarray) -> float:
    return np.sqrt(np.mean((y_hat - y) ** 2))


def angular_error(y_hat: np.ndarray, y: np.ndarray) -> float:
    dot = np.sum(y_hat * y, axis=1)
    norm = np.linalg.norm(y_hat, axis=1) * np.linalg.norm(y, axis=1)
    cos = np.clip(dot / (norm + 1e-8), -1.0, 1.0)
    return np.mean(np.arccos(cos))
