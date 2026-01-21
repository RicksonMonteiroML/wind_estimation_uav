class TimeBase:
    def __init__(self, dt: float, duration: float):
        self.dt = dt
        self.duration = duration
        self.t = 0.0

    def __iter__(self):
        self.t = 0.0
        return self

    def __next__(self):
        if self.t > self.duration:
            raise StopIteration
        t = self.t
        self.t += self.dt
        return t
