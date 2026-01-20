import numpy as np
from simulation.custom_simulator import CustomSimulator


def test_hover_no_wind(simulator: CustomSimulator):
    simulator.reset()

    # força de hover = m * g (em body frame)
    mass = simulator.rb.m
    g = np.linalg.norm(simulator.rb.g)

    u_hover = np.array([0.0, 0.0, mass * g])

    for _ in range(100):
        simulator.step(u_hover)

    p, v, _, _ = simulator.get_state()
    assert np.linalg.norm(v) < 1e-2
