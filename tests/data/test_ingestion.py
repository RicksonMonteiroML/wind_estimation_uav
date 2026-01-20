from data.ingestion.recorder import DataRecorder
import numpy as np


def test_recorder_shapes():
    recorder = DataRecorder()

    for _ in range(10):
        recorder.record(
            sensors={"imu": np.zeros(6)},
            control=np.zeros(3),
            wind_gt=np.zeros(3),
        )

    records = recorder.get_records()
    assert len(records) == 10
