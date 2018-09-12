# coding=utf-8
import numpy

uk_data = numpy.loadtxt('./GB_video_data_numbers.csv', delimiter=",", dtype=int)
us_data = numpy.loadtxt('./US_video_data_numbers.csv', delimiter=",", dtype=int)
ones = numpy.ones((uk_data.shape[0], 1), dtype=int)
zeros = numpy.zeros((us_data.shape[0], 1), dtype=int)
uk_data = numpy.hstack((uk_data, ones))
us_data = numpy.hstack((us_data, zeros))
all_data = numpy.vstack((uk_data, us_data))
print(all_data)
