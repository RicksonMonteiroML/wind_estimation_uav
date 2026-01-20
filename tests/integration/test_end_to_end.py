import numpy as np

def test_full_pipeline_with_ekf(simulator, ekf):
    simulator.reset()

    mass = simulator.rb.m
    g = np.linalg.norm(simulator.rb.g)
    u_hover = np.array([0.0, 0.0, mass * g])

    for _ in range(50):
        simulator.step(u_hover)
        sensors = simulator.get_sensors()

        z = sensors["state"][:3]  # ex: velocidade
        ekf.predict(u=None, dt=simulator.dt)
        ekf.update(z)

    state = ekf.get_state()
    assert np.all(np.isfinite(state))
