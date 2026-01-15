import numpy as np
import matplotlib.pyplot as plt


def plot_time_series(
    y_gt: np.ndarray,
    y_hat: np.ndarray,
    labels=("x", "y", "z"),
    title: str = "Wind estimation",
):
    """
    Time-series plot of ground truth vs estimate.
    """
    t = np.arange(len(y_gt))

    fig, axs = plt.subplots(3, 1, sharex=True, figsize=(10, 6))

    for i in range(3):
        axs[i].plot(t, y_gt[:, i], label="GT")
        axs[i].plot(t, y_hat[:, i], label="Estimate")
        axs[i].set_ylabel(labels[i])
        axs[i].grid(True)

    axs[-1].set_xlabel("Time step")
    axs[0].legend()
    fig.suptitle(title)

    return fig

def plot_psd(
    f,
    Pxx_gt,
    Pxx_hat,
    title: str = "Wind PSD",
):
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.semilogy(f, Pxx_gt, label="GT")
    ax.semilogy(f, Pxx_hat, label="Estimate")

    ax.set_xlabel("Frequency [Hz]")
    ax.set_ylabel("PSD")
    ax.grid(True)
    ax.legend()
    ax.set_title(title)

    return fig
