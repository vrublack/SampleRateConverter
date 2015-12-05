import csv
from sensor_reading import SensorReading

__author__ = 'Valentin'


class FileReader:
    def __init__(self, filename):
        self.f = open(filename)
        self.reader = csv.reader(self.f)
        self.count = 0
        self.overlapping = None

    def read_next_chunk(self, to_time):

        """

        :param to_time: Up to what time should be read (exclusively)
        :return: Sensor readings up to the specified point of time,
        starting from where the method ended the last time it was called.
        """

        readings = []

        if self.overlapping is not None:
            readings.append(self.overlapping)
            self.overlapping = None

        for row in self.reader:
            self.count += 1
            if self.count == 1:  # header
                continue
            reading = SensorReading()

            for index, col in enumerate(row):
                if index == 0:
                    reading.sensor_type = col
                elif index == 1:
                    reading.x = float(col)
                elif index == 2:
                    reading.y = float(col)
                elif index == 3:
                    reading.z = float(col)
                elif index == 4:
                    reading.time = float(col)

            if not hasattr(reading, 'time'):
                print('Error in line: ' + str(row))
                continue

            if reading.time >= to_time:
                self.overlapping = reading
                return readings

            readings.append(reading)

        return readings
