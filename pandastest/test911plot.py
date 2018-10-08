# coding=utf-8
import numpy

import pandas
from matplotlib import pyplot

data = pandas.read_csv("./911.csv")
data["timeStamp"] = pandas.to_datetime(data["timeStamp"])
to_list = data["title"].str.split(": ").tolist()
cate_list = [i[0] for i in to_list]
data["cate"] = pandas.DataFrame(numpy.array(cate_list).reshape((data.shape[0], 1)))
data.set_index(data["timeStamp"], inplace=True)
pyplot.figure(figsize=(20, 8), dpi=80)
for group_name, group_data in data.groupby(by="cate"):
    count = group_data.resample("M").count()["title"]
    _x = count.index
    _x = [i.strftime("%Y-%m-%d") for i in _x]
    _y = count.values
    pyplot.plot(range(len(_x)), _y, label=group_name)

pyplot.legend(loc="best")
pyplot.xticks(range(len(_x)), _x, rotation=45)
pyplot.show()
