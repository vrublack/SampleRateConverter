import csv
from sensor_reading import SensorReading

__author__ = 'Valentin'


def read_file(filename):
    f = open(filename)
    reader = csv.reader(f)
    readings = []
    count = 0
    for row in reader:
        count += 1
        if count == 1:  # header
            continue
        if count % 100000 == 0:
            print(str(count) + ' lines read')
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

        readings.append(reading)

    f.close()

    return readings


def write_file(filename, readings):
    f = open(filename, 'w')
    # header
    f.write("Sensor type,x,y,z,time (ms)\n")
    count = 0
    for reading in readings:
        f.write(reading.sensor_type + ',' + str(reading.x) + ',' + str(reading.y) + ',' + str(
            reading.z) + ',' + str(reading.time) + '\n')
        count += 1
        if count % 100000 == 0:
            print(str(count) + ' lines written')

    f.close()
