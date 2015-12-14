import sys
from file_reader import FileReader
from file_writer import FileWriter
from sample_rate_converter import SampleRateConverter

__author__ = 'Valentin'


def main():
    if len(sys.argv) != 4:
        print('Error: Path as 1st, target sample rate as 2nd and "average" or "random" as 3rd argument expected')
        quit()
    filename = sys.argv[1]
    target_sample_rate = float(sys.argv[2])
    combination_strategy = sys.argv[3]

    file_reader = FileReader(filename)
    file_writer = FileWriter(filename + '@' + str(target_sample_rate) + 'hz')
    converter = SampleRateConverter(target_sample_rate, combination_strategy)

    increment = (1000.0 / target_sample_rate) * 1000
    current_time_limit = 0 + increment  # in ms
    count = 0
    while True:
        reading_chunk = file_reader.read_next_chunk(current_time_limit)
        if len(reading_chunk) == 0:
            break
        converted_chunk = converter.convert(reading_chunk)
        file_writer.write_next_chunk(converted_chunk)

        current_time_limit += increment

        count += 1
        if count % 1 == 0:
            print('Iteration ' + str(count))

    print("Done.")


if __name__ == '__main__':
    main()
