from AbstractSegment import AbstractSegment
from random import randint


class RandomizedSegment(AbstractSegment):
    """
    Combines segment by choosing a random sample from the segment
    """

    def __init__(self, sensor_type, start_time, increment_time):
        super().__init__(sensor_type, start_time, increment_time)
        self.samples = []

    def next_segment(self):
        self.samples = []
        self.start_time += self.increment_time

    def combine(self):
        if len(self.samples) > 0:
            index = randint(0, len(self.samples) - 1)
            return self.samples[index]

    def add(self, sample):
        self.samples.append(sample)
