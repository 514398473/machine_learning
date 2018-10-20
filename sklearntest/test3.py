# coding=utf-8
import numpy
import pandas
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, LogisticRegression
from sklearn.metrics import mean_squared_error, classification_report
from sklearn.externals import joblib


def myLinear():
    """
    线性回归直接预测房价
    :return:None
    """
    # 加载数据
    data = load_boston()

    # 切分数据
    train_f, test_f, train_t, test_t = train_test_split(data.data, data.target, test_size=0.25)

    # 特征标准化处理

    # 特征值处理
    ss_f = StandardScaler()
    train_f = ss_f.fit_transform(train_f)
    test_f = ss_f.transform(test_f)

    # 目标值处理
    ss_t = StandardScaler()
    train_t = ss_t.fit_transform(numpy.array(train_t).reshape(-1, 1))
    test_t = ss_t.transform(numpy.array(test_t).reshape(-1, 1))

    # 正规方程求解方式预测结果
    # lr = LinearRegression()
    # lr.fit(train_f, train_t)
    # print(lr.coef_)
    # # 预测测试集的房价结果
    # predict_t = ss_t.inverse_transform(lr.predict(test_f))
    # print("正规方程测试集里每个房子的预测价格:", predict_t)
    # print("正规方程的均方误差:", mean_squared_error(ss_t.inverse_transform(test_t), predict_t))

    # 梯度下降进行房子预测
    # sr = SGDRegressor()
    # sr.fit(train_f, train_t)
    # print(sr.coef_)
    # # 预测测试集的房价结果
    # predict_t = ss_t.inverse_transform(sr.predict(test_f))
    # print("梯度下降测试集里每个房子的预测价格:", predict_t)
    # print("梯度下降的均方误差:", mean_squared_error(ss_t.inverse_transform(test_t), predict_t))

    # 岭回归进行房子预测
    # ridge = Ridge(alpha=1.0)
    # ridge.fit(train_f, train_t)
    # joblib.dump(ridge,"./tmp/test.pkl")
    # print(ridge.coef_)
    # # 预测测试集的房价结果
    # predict_t = ss_t.inverse_transform(ridge.predict(test_f))
    # print("岭回归测试集里每个房子的预测价格:", predict_t)
    # print("岭回归的均方误差:", mean_squared_error(ss_t.inverse_transform(test_t), predict_t))

    ridge = joblib.load("./tmp/test.pkl")
    predict_t = ss_t.inverse_transform(ridge.predict(test_f))
    print("保存的模型预测的结果是:", predict_t)
    return None


def logistic():
    """
    逻辑回归二分类进行癌症预测
    :return:None
    """
    names = ["Sample code number", "Clump Thickness", "Uniformity of Cell Size", "Uniformity of Cell Shape",
             "Marginal Adhesion", "Single Epithelial Cell Size", "Bare Nuclei", "Bland Chromatin", "Normal Nucleoli",
             "Mitoses", "Class"]
    # 加载数据
    data = pandas.read_csv(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
        names=names)
    # 处理缺失数据
    data = data.replace(to_replace="?", value=numpy.nan)
    data.dropna(inplace=True)
    # 数据切分
    train_f, test_f, train_t, test_t = train_test_split(data[names[1:10]], data[names[10]], test_size=0.25)
    # 标准化处理
    sta = StandardScaler()
    train_f = sta.fit_transform(train_f)
    test_f = sta.transform(test_f)
    lr = LogisticRegression(C=1.0)
    lr.fit(train_f, train_t)
    print(lr.coef_)
    predict = lr.predict(test_f)
    print("准确率是:", lr.score(test_f, test_t))
    print("召回率是:", classification_report(test_t, predict, labels=[2, 4], target_names=["良性", "恶性"]))
    return None


def kmeans():
    """
    kmeans 聚类
    :return: None
    """
    pandas.read_csv("./")
    return None


if __name__ == "__main__":
    kmeans()
