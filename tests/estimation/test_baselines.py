import numpy as np
from estimation.models.baselines.persistence import PersistenceModel


def test_persistence():
    model = PersistenceModel()
    w = np.array([1.0, 0.0, -1.0])
    model.update(w)

    assert np.allclose(model.predict(None), w)
