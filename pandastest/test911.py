# coding=utf-8
import numpy
import pandas

csv = pandas.read_csv("./911.csv")
# print(csv.info())
# print(csv['title'].head())
# 第一种方法
# tolist = csv['title'].str.split(": ").tolist()
# arr = list(set([i[0] for i in tolist]))
# frame = pandas.DataFrame(numpy.zeros((csv.shape[0], len(arr))), columns=arr)
# for i in arr:
#     frame[i][csv['title'].str.contains(i)] = 1
# frame_sum = frame.sum(axis=0)
# print(frame_sum)
# 第二种方法
tolist = csv['title'].str.split(": ").tolist()
tolist_ = [i[0] for i in tolist]
csv["cate"] = pandas.DataFrame(numpy.array(tolist_).reshape(csv.shape[0],1))
title_ = csv.groupby(by="cate").count()["title"]
print(title_)