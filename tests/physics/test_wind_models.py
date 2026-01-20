import numpy as np
from physics.wind_model.constant_wind import ConstantWind 
from physics.wind_model.dryden_wind import DrydenWind
from physics.wind_model.random_walk import RandomWalkWind 


def test_constant_wind():
    w = np.array([1.0, -2.0, 0.5])
    model = ConstantWind(w)

    for _ in range(10):
        model.step(0.01)
        assert np.allclose(model.get_wind(), w)


def test_dryden_statistics():
    model = DrydenWind(
        Lu=50, Lv=50, Lw=10,
        sigma_u=1.0, sigma_v=1.0, sigma_w=0.5,
    )

    winds = []
    for _ in range(2000):
        model.step(0.01, airspeed=5.0)
        winds.append(model.get_wind())

    winds = np.array(winds)
    assert winds.std(axis=0).mean() > 0.1

