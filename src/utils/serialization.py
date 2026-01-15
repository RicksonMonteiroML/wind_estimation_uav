import pickle
from typing import Any


def save_object(obj: Any, path: str) -> None:
    with open(path, "wb") as f:
        pickle.dump(obj, f)


def load_object(path: str) -> Any:
    with open(path, "rb") as f:
        return pickle.load(f)
