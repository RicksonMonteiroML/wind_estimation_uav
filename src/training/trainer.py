import torch
from torch.utils.data import DataLoader
from typing import Callable


class Trainer:
    """
    Generic trainer for supervised learning models.
    """

    def __init__(
        self,
        model,
        optimizer,
        loss_fn: Callable,
        device: str = "cpu",
    ):
        self.model = model.to(device)
        self.optimizer = optimizer
        self.loss_fn = loss_fn
        self.device = device

    def train_epoch(self, loader: DataLoader) -> float:
        self.model.train()
        total_loss = 0.0

        for X, y in loader:
            X, y = X.to(self.device), y.to(self.device)

            self.optimizer.zero_grad()
            y_hat = self.model(X)
            loss = self.loss_fn(y_hat, y)
            loss.backward()
            self.optimizer.step()

            total_loss += loss.item()

        return total_loss / len(loader)

    def evaluate(self, loader: DataLoader) -> float:
        self.model.eval()
        total_loss = 0.0

        with torch.no_grad():
            for X, y in loader:
                X, y = X.to(self.device), y.to(self.device)
                y_hat = self.model(X)
                total_loss += self.loss_fn(y_hat, y).item()

        return total_loss / len(loader)
