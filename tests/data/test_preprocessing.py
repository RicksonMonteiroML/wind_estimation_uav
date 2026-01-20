from data.preprocessing.splits import split_trajectories


def test_split_sizes():
    trajs = list(range(10))
    train, val, test = split_trajectories(trajs, 0.6, 0.2)

    assert len(train) == 6
    assert len(val) == 2
    assert len(test) == 2
