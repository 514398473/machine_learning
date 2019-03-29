# coding=utf-8
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

x = range(11, 31)
y1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
_x = ["{}岁".format(i) for i in x]
plt.figure(figsize=(20, 8), dpi=80, num=5)
plt.xticks(x, _x)
plt.plot(x, y1, color="red", linestyle=":", alpha=0.8, label="自己")
plt.plot(x, y2, color="blue", linestyle="--", alpha=0.3, label="同桌")
plt.legend(loc=0)
plt.show()
