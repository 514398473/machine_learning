# coding=utf-8
import pandas

data = pandas.read_csv("./starbucks_store_worldwide.csv")
country_groupby = data.groupby(by="Country")
count = country_groupby["Brand"].count()
# print(count["US"])
# print(count["CN"])
# china_data = data[data["Country"] =="CN"]
# brand_ = china_data.groupby(by="State/Province")["Brand"].count()
# print(brand_)
group_data = data["Brand"].groupby(by=[data["Country"], data["State/Province"]]).count()
# print(group_data)
print(group_data.index)
