# coding=utf-8
import numpy
import pandas
from matplotlib import pyplot

data = pandas.read_csv("./IMDB-Movie-Data.csv")
tolist = data["Genre"].str.split(",").tolist()
list_data = list(set([i for j in tolist for i in j]))
zeros_data = pandas.DataFrame(numpy.zeros((data.shape[0], len(list_data))), columns=list_data)
for i in range(data.shape[0]):
    zeros_data.loc[i, tolist[i]] = 1
final_data = zeros_data.sum(axis=0)
values = final_data.sort_values()
pyplot.figure(figsize=(20, 8), dpi=100)
pyplot.bar(values.index, values.values)
pyplot.xticks(rotation=90)
pyplot.show()
