# coding=utf-8
import pandas
from matplotlib import pyplot

data = pandas.read_csv("./PM2.5/BeijingPM20100101_20151231.csv")
index = pandas.PeriodIndex(year=data["year"], month=data["month"], day=data["day"], hour=data["hour"], freq="H")
data["datetime"] = index
data.set_index(data["datetime"], inplace=True)
data = data.resample("W").mean()
us_data = data["PM_US Post"]
cn_data = data["PM_Nongzhanguan"]
us_x = us_data.index
cn_x = cn_data.index
us_x = [i.strftime("%Y-%m-%d") for i in us_x]
cn_x = [i.strftime("%Y-%m-%d") for i in cn_x]
us_y = us_data.values
cn_y = cn_data.values
pyplot.figure(figsize=(20, 8), dpi=80)
pyplot.plot(range(len(us_x)), us_y, label="us", alpha=0.7)
pyplot.plot(range(len(cn_x)), cn_y, label="cn", alpha=0.7)
pyplot.xticks(range(len(us_x))[::10], us_x[::10], rotation=45)
pyplot.legend(loc="best")
pyplot.show()
