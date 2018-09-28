# coding=utf-8
import pandas
from matplotlib import pyplot

csv = pandas.read_csv("./books.csv")
#不同年份书的数量
# csv = csv[pandas.notnull(csv["original_publication_year"])]
# year_ = csv.groupby(by="original_publication_year").count()["original_title"]
# _x=year_.index
# _y=year_.values
# pyplot.figure(figsize=(20,8),dpi=80)
# pyplot.bar(range(len(_x)),_y)
# pyplot.xticks(range(len(_x))[::50],_x[::50])
# pyplot.show()
#不同年份书的平均评分情况
csv = csv[pandas.notnull(csv["original_publication_year"])]
# print(csv.info())
year_ = csv.groupby(by="average_rating").mean()["original_publication_year"]
_x=year_.index
_y=year_.values
pyplot.figure(figsize=(20,8),dpi=80)
pyplot.plot(range(len(_x)),_y)
pyplot.xticks(range(len(_x))[::10],_x[::10],rotation=90)
pyplot.show()
