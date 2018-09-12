# coding=utf-8
import pandas

data = pandas.read_csv("./dogNames2.csv")
# 按次数排序取前10
# data = data.sort_values(by=["Count_AnimalName"], ascending=False)
# print(data[:10])

data = data[(data["Count_AnimalName"] > 700) & (data["Row_Labels"].str.len() > 4)]
print(data)

