import file_handler
from sample_rate_converter import SampleRateConverter

__author__ = 'Valentin'


def main():
    filename = '/home/pi/acquisitions/readings'
    readings = file_handler.read_file(filename)
    print("Loaded")
    target_sample_rate = 100
    converter = SampleRateConverter(target_sample_rate)
    converted_readings = converter.convert(readings)
    print("Converted")
    file_handler.write_file(filename + '@' + str(target_sample_rate) + 'hz', converted_readings)
    print("Done.")

if __name__ == '__main__':
    main()
