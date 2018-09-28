# coding=utf-8
import matplotlib
import pandas
from matplotlib import pyplot, font_manager

csv_data = pandas.read_csv("./starbucks_store_worldwide.csv")
# 使用matplotlib呈现出店铺总数排名前10的国家
# brand_ = csv_data.groupby(by="Country").count()["Brand"].sort_values(ascending=False)[:10]
# _x = brand_.index
# _y = brand_.values
# pyplot.figure(figsize=(20,8),dpi=80)
# pyplot.bar(range(len(_x)),_y)
# pyplot.xticks(range(len(_x)),_x)
# pyplot.show()
# 使用matplotlib呈现出每个中国每个城市的店铺数量
properties = matplotlib.font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")
csv_data = csv_data[csv_data["Country"] == "CN"]
brand_ = csv_data.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:10].sort_values()
_x = brand_.index
_y = brand_.values
pyplot.figure(figsize=(20, 8), dpi=80)
pyplot.barh(range(len(_x)), _y)
pyplot.yticks(range(len(_x)), _x,fontproperties=properties)
pyplot.xlabel("数量",fontproperties=properties)
pyplot.ylabel("城市",fontproperties=properties)
pyplot.show()
