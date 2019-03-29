# coding=utf-8
from matplotlib import pyplot as plt

# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# x轴
x = range(2, 26, 2)
# y轴
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]
# 设置图片大小
fig = plt.figure(figsize=(15, 8), dpi=100)
# 标题
plt.title("温度变化")
# x轴标题
plt.xlabel("时间")
# x轴刻度
plt.xticks(range(2, 25, 1))
# y轴标题
plt.ylabel("气温°C", rotation=360)
# y轴刻度
plt.yticks(range(min(y), max(y) + 1))
# 绘图
plt.plot(x, y, color="red", alpha=0.3, linestyle=":")
# 图例
plt.legend("气温")
# 网格
plt.grid()
# 水印
fig.text(0.75, 0.45, '水印',
         fontsize=40, color='green',
         ha='right', va='bottom', alpha=0.4)
# 保存到本地
# plt.savefig("./2.png")
# 显示图片
plt.show()
