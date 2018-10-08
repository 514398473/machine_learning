# coding=utf-8
import numpy

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Imputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
import jieba


def dictvec():
    """
    字典数据抽取
    :return: None
    """
    vectorizer = DictVectorizer(sparse=False)
    data = vectorizer.fit_transform(
        [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30}])
    print(data)
    return None


def countvec():
    """
    对文本值进行特征化
    :return:None
    """
    vectorizer = CountVectorizer()
    data = vectorizer.fit_transform(["The more difficult something became, the more rewarding it was in the end.",
                                     "success belongs to the persevering"])
    print(vectorizer.get_feature_names())
    print(data.toarray())
    print(data)
    return None


def cutword():
    """
    对文本进行分词
    :return:
    """
    data1 = jieba.cut("今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。")
    data2 = jieba.cut("我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。")
    data3 = jieba.cut("如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。")

    data1 = list(data1)
    data2 = list(data2)
    data3 = list(data3)
    data1 = " ".join(data1)
    data2 = " ".join(data2)
    data3 = " ".join(data3)
    return data1, data2, data3


def chinesevec():
    """
    对中文进行特征化
    :return:None
    """
    d1, d2, d3 = cutword()
    vectorizer = CountVectorizer()
    data = vectorizer.fit_transform([d1, d2, d3])
    print(vectorizer.get_feature_names())
    print(data.toarray())
    return None


def tfidfvec():
    """
    文本的重要程度
    :return: None
    """
    d1, d2, d3 = cutword()
    tfidfvectorizer = TfidfVectorizer()
    data = tfidfvectorizer.fit_transform([d1, d2, d3])
    print(tfidfvectorizer.get_feature_names())
    print(data.toarray())
    return None


def mm():
    """
    归一化处理
    :return: None
    """
    scaler = MinMaxScaler(feature_range=(0, 1))
    data = scaler.fit_transform([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])
    print(data)
    return None


def stand():
    """
    标准化处理
    :return: None
    """
    scaler = StandardScaler()
    data = scaler.fit_transform([[1., -1., 3.], [2., 4., 2.], [4., 6., -1.]])
    print(data)
    return None


def im():
    """
    缺失值处理
    :return: None
    """
    imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
    data = imputer.fit_transform([[1, 2], [numpy.nan, 3], [7, 6]])
    print(data)
    return None


def var():
    """
    删除低方差的特征
    :return:None
    """
    threshold = VarianceThreshold(threshold=0.0)
    data = threshold.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])
    print(data)
    return None


def pca():
    """
    主成分分析进行特征降维
    :return: None
    """
    pca = PCA(n_components=0.95)
    data = pca.fit_transform([[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]])
    print(data)
    return None


if __name__ == "__main__":
    pca()
