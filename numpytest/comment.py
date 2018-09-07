# coding=utf-8
import numpy
from matplotlib import pyplot

data = numpy.loadtxt("./US_video_data_numbers.csv", delimiter=",", dtype='int')
data_ = data[:, 3]
data_ = data_[data_ < 5000]
num = (data_.max() - data_.min()) // 50
print(num)
pyplot.figure(figsize=(20,8),dpi=80)
pyplot.hist(data_, num)
pyplot.show()
