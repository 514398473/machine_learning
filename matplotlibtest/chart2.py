# coding=utf-8

from matplotlib import pyplot as plt
import random

# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(20, 8), dpi=80)
x = range(0, 120)
_x = ["10点{}分".format(i) for i in range(60)]
_x += ["11点{}分".format(i) for i in range(60)]
y = [random.randint(20, 35) for i in range(120)]
plt.xticks(x[::3], _x[::3], rotation=45)
plt.yticks(range(min(y), max(y) + 1))
plt.xlabel("时间")
plt.ylabel("温度", rotation=360)
plt.title("气温的变化")
plt.plot(x, y)
plt.show()
