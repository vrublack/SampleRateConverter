from AbstractSegment import AbstractSegment
from AverageSegment import AverageSegment
from CenterPointSegment import CenterPointSegment
from RandomizedSegment import RandomizedSegment
from sensor_reading import SensorReading

__author__ = 'Valentin'


class SampleRateConverter:
    def __init__(self, target_rate, combination_strategy):
        self.target_rate = target_rate
        self.increment_ms = 1000.0 / target_rate
        self.combination_strategy = combination_strategy

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

            segment = self.__get_segment(reading.sensor_type, reading.time)

            if reading.time >= segment.getEnd():
                # segment ended here, so possibly combine samples in that segment into one average
                combined_sample = segment.combine()
                if combined_sample is not None:
                    converted_samples.append(combined_sample)

                segment.next_segment()

            segment.add(reading)
            # segment.last_reading_time = reading.time

        # add last segment that might not be full
        for sensor_type, segment in self.segments_for_sensor_type.items():
            combined_sample = segment.combine()
            if combined_sample is not None:
                converted_samples.append(combined_sample)

        return converted_samples

    def __get_segment(self, sensor_type, reading_time):
        """

        :param sensor_type: Type of sensor
        :param reading_time: Time of current reading. This is relevant for the segment end.
        :return: Existing segment or newly created segment
        """

        if sensor_type in self.segments_for_sensor_type:
            return self.segments_for_sensor_type[sensor_type]
        else:
            if self.combination_strategy == 'random':
                segment = RandomizedSegment(sensor_type, reading_time - reading_time % self.increment_ms,
                                            self.increment_ms)
            elif self.combination_strategy == 'average':
                segment = AverageSegment(sensor_type, reading_time - reading_time % self.increment_ms,
                                         self.increment_ms)
            elif self.combination_strategy == 'center-point':
                segment = CenterPointSegment(sensor_type, reading_time - reading_time % self.increment_ms,
                                         self.increment_ms)
            else:
                raise ValueError('Strategy must be either "random" or "average"')
            self.segments_for_sensor_type[sensor_type] = segment
            return segment
