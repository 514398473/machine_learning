# coding=utf-8
from matplotlib import pyplot, font_manager

properties = font_manager.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
a = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22,
     23]
b = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13, 12,
     13, 6]
x_3 = range(1, 32)
x_10 = range(51, 82)
pyplot.figure(figsize=(20, 8), dpi=100)
pyplot.scatter(x_3, a, label='三月')
pyplot.scatter(x_10, b, label='十月')
pyplot.legend(prop=properties)
_x_lable = ['3月%d' % i for i in x_3]
_x_lable += ['十月%d' % (i - 50) for i in x_10]
pyplot.xticks((list(x_3) + list(x_10))[::3], _x_lable[::3], fontproperties=properties, rotation=45)
pyplot.show()
