import numpy as np
from scipy.signal import welch


def wind_psd(signal: np.ndarray, fs: float):
    """
    Power spectral density using Welch method.
    """
    f, Pxx = welch(signal, fs=fs, axis=0)
    return f, Pxx
