from sensor_reading import SensorReading

__author__ = 'Valentin'


class Segment:
    pass


class SampleRateConverter:
    def __init__(self, target_rate):
        self.target_rate = target_rate
        self.increment_ms = 1000 / target_rate

    def convert(self, sensor_readings):
        """

        :param sensor_readings: Readings that should be converted
        :param target_rate: Desired sampling rate (samples per second)
        :return: Readings where multiple samples are combined into one average
        sample so it matches the desired sampling rate
        """

        # In this algorithm, the time axis is divided up by segments that have
        # the size of self.increment_ms. In each segment, we collect all samples
        # and replace them by one sample containing the average value.

        converted_samples = []

        self.segments_for_sensor_type = {}

        for count, reading in enumerate(sensor_readings):

            if count % 100000 == 0:
                print(str(count) + ' lines converted')

            segment = self.__get_segment(reading.sensor_type)

            if reading.time >= segment.end:
                # segment ended here, so possibly combine samples in that segment into one average
                if segment.samples >= 1:
                    combined_sample = SensorReading()
                    combined_sample.sensor_type = reading.sensor_type
                    combined_sample.x = segment.sum[0] / segment.samples
                    combined_sample.y = segment.sum[1] / segment.samples
                    combined_sample.z = segment.sum[2] / segment.samples
                    # time in the middle of segment
                    combined_sample.time = segment.end - self.increment_ms / 2
                    converted_samples.append(combined_sample)
                segment.sum = (0.0, 0.0, 0.0)
                segment.samples = 0
                segment.end += self.increment_ms

            segment.samples += 1
            segment.sum = (segment.sum[0] + reading.x,
                           segment.sum[1] + reading.y,
                           segment.sum[2] + reading.z)

        return converted_samples

    def __get_segment(self, sensor_type):
        if sensor_type in self.segments_for_sensor_type:
            return self.segments_for_sensor_type[sensor_type]
        else:
            segment = Segment()
            segment.sum = (0.0, 0.0, 0.0)  # sum of x, y and z values
            segment.samples = 0
            segment.end = 0 + self.increment_ms
            self.segments_for_sensor_type[sensor_type] = segment
            return segment
