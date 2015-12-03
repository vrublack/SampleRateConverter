import sys
import file_handler
from sample_rate_converter import SampleRateConverter

__author__ = 'Valentin'


def main():
    if len(sys.argv) != 3:
        print('Error: Path as 1st and target sample rate as 2nd argument expected')
        quit()
    filename = sys.argv[1]
    target_sample_rate = float(sys.argv[2])
    readings = file_handler.read_file(filename)
    print("Loaded")
    converter = SampleRateConverter(target_sample_rate)
    converted_readings = converter.convert(readings)
    print("Converted")
    file_handler.write_file(filename + '@' + str(target_sample_rate) + 'hz', converted_readings)
    print("Done.")

if __name__ == '__main__':
    main()
