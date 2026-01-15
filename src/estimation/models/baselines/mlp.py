import torch
import torch.nn as nn
from estimation.models.base_model import BaseModel


class WindMLP(BaseModel, nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 3),
        )

    def forward(self, x):
        return self.net(x)

    def predict(self, x):
        with torch.no_grad():
            return self.forward(x)
