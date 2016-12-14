# SampleRateConverter
Perform downsampling on recordings from https://github.com/vrublack/GY-85

# Usage

Syntax: [path] [strategy] [target sample rate 1] ... [target sample rate n]

For example arguments, 'recording.csv center-point 500 25' convert recording.csv into both 500 and 25 hz using the center-point strategy.

# Strategies

The input data is divided into [target sample rate-many] segments per second. To convert the data into the target sample rate, we need to pick one sample per second. The strategy specifies, which sample to pick.

- Random: pick random sample
- Average: compute average over all samples in the segment and use that
- Center-point: use sample in the middle of the segment
