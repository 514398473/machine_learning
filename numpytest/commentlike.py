#coding=utf-8
import numpy
from matplotlib import pyplot

data = numpy.loadtxt("./US_video_data_numbers.csv", dtype="int", delimiter=",")
data = data[data[:,1] < 500000]
like = data[:,1]
comment= data[:,3]
pyplot.scatter(like,comment)
pyplot.show()
# print(data)