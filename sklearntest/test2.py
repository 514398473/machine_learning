# coding=utf-8
import numpy
import pandas
from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def iris():
    """
    鸢尾花数据
    :return:None
    """
    iris = load_iris()
    # print("特征值")
    # print(iris.data)
    # print("目标值")
    # print(iris.target)

    # print(iris.DESCR)
    # 返回值 训练集的特征值,测试集的特征值,训练集的目标值,测试集的目标值
    train_f, test_f, train_t, test_t = train_test_split(iris.data, iris.target, test_size=0.25)

    # print("训练集的特征值和目标值:", train_f, train_t)
    # print("测试集的特征值和目标值:", test_f, test_t)
    # knn = KNeighborsClassifier(n_neighbors=10, algorithm="auto")
    # knn.fit(train_f, train_t)
    # print("预测值是:", knn.predict(test_f))
    # print("准确率是:", knn.score(test_f, test_t))
    knn = KNeighborsClassifier()
    params = {"n_neighbors": [3, 5, 7, 10, 15]}
    gc = GridSearchCV(knn, param_grid=params, cv=10)
    gc.fit(train_f, train_t)
    print("准确率是:", gc.score(test_f, test_t))
    print("交叉验证最好的结果:", gc.best_score_)
    print("最好的模型:", gc.best_estimator_)
    print("每个超参数每次交叉验证的结果:", gc.cv_results_)
    return None


def news():
    """
    新闻数据
    :return: None
    """
    newsgroups = fetch_20newsgroups()
    print("特征值")
    print(newsgroups.data)
    print("目标值")
    print(newsgroups.target)

    return None


def boston():
    """
    房价数据
    :return:None
    """
    boston = load_boston()
    print("特征值")
    print(boston.data)
    print("目标值")
    print(boston.target)
    print(boston.DESCR)

    return None


def knncls():
    """
    k近邻
    :return: None
    """
    # 读取数据
    data = pandas.read_csv("C:\\Users\dell\\.kaggle\\train.csv")
    # print(data.head(10))

    # 处理数据
    data.query("x > 1.0 & x < 1.25 & y > 2.5 & y < 2.75", inplace=True)

    # 处理时间数据
    data_time = pandas.to_datetime(data["time"], unit="s")
    # print(data_time)

    # 把日期格式转换成字典格式
    data_time = pandas.DatetimeIndex(data_time)

    # 构造特征
    data["day"] = data_time.day
    data["hour"] = data_time.hour
    data["weekday"] = data_time.weekday

    # 把时间戳特征删除
    data.drop(["time"], axis=1, inplace=True)
    # print(data)

    # 把签到数量少于3个的目标位置删除
    place_count = data.groupby("place_id").count()
    index = place_count[place_count.row_id > 3].reset_index()
    data = data[data["place_id"].isin(index.place_id)]

    # 取出数据中的特征值和目标值
    t = data["place_id"]
    f = data.drop(["place_id"], axis=1)
    f = data.drop(["row_id"], axis=1)

    # 分隔测试集和训练集
    train_f, test_f, train_t, test_t = train_test_split(f, t, test_size=0.25)

    # 特征工程(标准化)
    scaler = StandardScaler()
    train_f = scaler.fit_transform(train_f)
    test_f = scaler.transform(test_f)

    # 进行算法流程
    knn = KNeighborsClassifier()
    # knn.fit(train_f, train_t)
    # # 得出预测结果
    # predict = knn.predict(test_f)
    # print("预测的目标签到值是:", predict)
    # # 得出准确率
    # print("预测的准确率是:", knn.score(test_f, test_t))

    # 构建参数
    params = {"n_neighbors": [3, 5, 10]}
    # 进行网格搜索
    gc = GridSearchCV(knn, param_grid=params, cv=3)
    gc.fit(train_f, train_t)
    # 预测准确率
    print("在测试集的准确率:", gc.score(test_f, test_t))
    print("在交叉验证最好的结果:", gc.best_score_)
    print("选择最好的模型是:", gc.best_estimator_)
    print("每个超参数每次交叉验证的结果:", gc.cv_results_)
    return None


def navibayes():
    """
    朴素贝叶斯进行文本分类
    :return: None
    """
    data = fetch_20newsgroups(subset="all")
    # 对数据进行分割
    train_f, test_f, train_t, test_t = train_test_split(data.data, data.target, test_size=0.25)
    # 对数据进行特征抽取
    tf = TfidfVectorizer()
    # 对训练集当中的词的列表进行每篇文章重要行统计
    train_f = tf.fit_transform(train_f)
    print(train_f)
    print(tf.get_feature_names())

    test_f = tf.transform(test_f)
    # 进行朴素贝叶斯的预测
    nb = MultinomialNB(alpha=1.0)
    nb.fit(train_f, train_t)
    result = nb.predict(test_f)
    print("预测的文章类别:", result)
    # 得出准确率
    print("准确率为:", nb.score(test_f, test_t))
    print("每个类别的精准率和召回率:", classification_report(test_t, result, target_names=data.target_names))

    return None


def decision():
    """
    用决策树对泰但尼克号进行预测生死
    :return: None
    """
    data = pandas.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    # 处理数据找出特征值和目标值
    feature_data = data[["pclass", "age", "sex"]]
    target_data = data["survived"]
    # 缺失值处理
    feature_data["age"].fillna(feature_data["age"].mean(), inplace=True)
    train_f, test_f, train_t, test_t = train_test_split(feature_data, target_data, test_size=0.25)
    # 进行特征处理
    dict = DictVectorizer(sparse=False)
    train_f = dict.fit_transform(train_f.to_dict(orient="records"))
    print(dict.get_feature_names())
    test_f = dict.transform(test_f.to_dict(orient="records"))

    # # 用决策树进行预测
    # dtc = DecisionTreeClassifier()
    # dtc.fit(train_f, train_t)
    # # 预测准确率
    # print("准确率是:", dtc.score(test_f, test_t))

    # 导出决策树结构
    # export_graphviz(dtc,out_file="./tree.dot",feature_names=dict.get_feature_names())

    # 随机森林进行验证(超参数调优)
    rfc = RandomForestClassifier(n_jobs=4)

    params = {"n_estimators": [120, 200, 300, 500, 800, 1200], "max_depth": [5, 8, 15, 25, 30]}

    # 网格搜索与参数调优
    gc = GridSearchCV(rfc, param_grid=params, cv=3)
    gc.fit(train_f, train_t)

    print("准确率是:", gc.score(test_f, test_t))
    print("查看选择的参数模型:", gc.best_params_)
    return None


def londondata():
    """
    伦敦数据科学
    :return:None
    """
    test_data = pandas.read_csv("./test.csv")
    train_data = pandas.read_csv("./train.csv")
    trainLabels = pandas.read_csv("./trainLabels.csv")

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(train_data, trainLabels)
    test_t = knn.predict(test_data)
    print("结果是:", test_t)
    return None


if __name__ == "__main__":
    londondata()
