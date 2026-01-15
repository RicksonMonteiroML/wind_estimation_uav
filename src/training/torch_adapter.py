import torch
from torch.utils.data import Dataset
from data.dataset.windowed_dataset import WindowedDataset


class TorchDatasetAdapter(Dataset):
    def __init__(self, dataset: WindowedDataset):
        self.dataset = dataset

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        X, y = self.dataset[idx]
        return (
            torch.tensor(X, dtype=torch.float32),
            torch.tensor(y, dtype=torch.float32),
        )
