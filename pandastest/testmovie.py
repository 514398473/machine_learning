# coding=utf-8
import pandas

data = pandas.read_csv("./IMDB-Movie-Data.csv")
# mean = data["Rating"].mean()
# print(mean)
actors_ = data["Actors"].str.split(",").tolist()
n = set()
l = []
for i in actors_:
    for j in i:
        n.add(j)
print(len(n),n)
