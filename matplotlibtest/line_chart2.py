# coding=utf-8
from matplotlib import pyplot, font_manager

properties = font_manager.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
b = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]
c = range(11,31)
pyplot.plot(c,a,color='red',linestyle="--",linewidth=5,alpha=0.2,label='自己')
pyplot.plot(c,b,label='同学')
pyplot.legend(prop=properties,loc="lower right")
pyplot.xticks(c,[ "%d岁" % i for i in c],fontproperties=properties)
pyplot.show()