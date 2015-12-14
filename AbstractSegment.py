class AbstractSegment:
    def __init__(self, sensor_type, start_time, increment_time):
        self.sensor_type = sensor_type
        self.start_time = start_time
        self.increment_time = increment_time

    def add(self, sample):
        raise NotImplementedError("Not implemented")

    def combine(self):
        """

        :return: Combined data point from this segment
        """
        raise NotImplementedError("Not implemented")

    def next_segment(self):
        """
            Resets samples in this segment and moves time according to the increment time
        """
        raise NotImplementedError("Not implemented")

    def getStart(self):
        return self.start_time

    def getEnd(self):
        return self.start_time + self.increment_time