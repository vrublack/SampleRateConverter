from AbstractSegment import AbstractSegment
from sensor_reading import SensorReading


class AverageSegment(AbstractSegment):
    """
    Combines segment by calculating the average of all the samples in the segment
    """

    def __init__(self, sensor_type, start_time, increment_time):
        super().__init__(sensor_type, start_time, increment_time)
        self.sum = (0.0, 0.0, 0.0)
        self.samples = 0

    def add(self, sample):
        self.sum = (self.sum[0] + sample.x, self.sum[1] + sample.y, self.sum[2] + sample.z)
        self.samples += 1

    def combine(self):
        if self.samples > 0:
            combined_sample = SensorReading()
            combined_sample.sensor_type = self.sensor_type
            combined_sample.x = self.sum[0] / self.samples
            combined_sample.y = self.sum[1] / self.samples
            combined_sample.z = self.sum[2] / self.samples
            # time in the middle of segment
            combined_sample.time = self.start_time + self.increment_time / 2
            return combined_sample

    def next_segment(self):
        self.sum = (0.0, 0.0, 0.0)
        self.samples = 0
        self.start_time += self.increment_time
