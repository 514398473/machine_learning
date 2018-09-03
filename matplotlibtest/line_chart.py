# coding=utf-8
from matplotlib import pyplot

x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]
#设置图形大小
pyplot.figure(figsize=(20,10),dpi=80)
pyplot.xticks(x)
pyplot.plot(x,y)
# pyplot.savefig("./1.png")
pyplot.show()

