# coding=utf-8
import pandas
import pymongo as pm

# 获取连接
client = pm.MongoClient('top.mongo.tusvn.net', 27017)  # 端口号是数值型

# 连接数据库
db = client.qdyktest

# 获取集合
stb = db.car_201809

# 获取数据信息
data = pandas.DataFrame(list(stb.find()))
print(data)