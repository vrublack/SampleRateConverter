__author__ = 'Valentin'


class FileWriter:
    def __init__(self, filename):
        self.f = open(filename, 'w')

        self.count = 0

    def write_next_chunk(self, readings):

        if self.count == 0:
            # header
            self.f.write("Sensor type,x,y,z,time (ms)\n")

        for reading in readings:
            self.f.write(reading.sensor_type + ',' + str(reading.x) + ',' + str(reading.y) + ',' + str(
                reading.z) + ',' + str(reading.time) + '\n')
            self.count += 1
