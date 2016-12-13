import sys
from file_reader import FileReader
from file_writer import FileWriter
from sample_rate_converter import SampleRateConverter

__author__ = 'Valentin'


def main():
    usage = "[path] [strategy] [target sample rate 1] ... [target sample rate n].\nFor example arguments, 'recording.csv center-point 500 25' convert recording.csv into both 500 and 25 hz using the center-point strategy.\nStrategies are random, average and center-point."
    if len(sys.argv) < 4:
        print('Wrong number of arguments. Usage: ' + usage)
        quit()
    filename = sys.argv[1]
    combination_strategy = sys.argv[2]

    target_sample_rates = []
    target_sample_rates.append(float(sys.argv[3]))
    for i in range(4, len(sys.argv)):
        target_sample_rates.append(float(sys.argv[i]))

    for target_sample_rate in target_sample_rates:

        print('Converting to ' + str(target_sample_rate) + ' hz')

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
