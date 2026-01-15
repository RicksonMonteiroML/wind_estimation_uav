import torch


def mse_loss(y_hat: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    return torch.mean((y_hat - y) ** 2)


def rmse_loss(y_hat: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    return torch.sqrt(mse_loss(y_hat, y))
