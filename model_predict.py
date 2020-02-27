# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 20:14:08 2019
@author: sunwf1114
"""
from tensorflow import keras
import numpy as np  # 用于转换数据
import pandas as pd  # 用于分析数据集
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog,QApplication
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
    def msg(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                          "All Files (*);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔
        return fileName1


def load_model():  # 加载模型
    with open(r'./model/model.json', 'r') as file:
        model_json1 = file.read()
    model = keras.models.model_from_json(model_json1)  # 返回模型结构
    model.load_weights("./model/model.hdf5", by_name=False)  # 加载模型的权重
    return model


# 加载基本数据进行归一化
def read_min_max():
    filename = "./model/data.txt"
    with open(filename, 'r+', encoding='utf-8') as f:
        for lines in f.readlines():
            ss = lines.strip('[]').split(', ')
    ds = np.asarray(ss)
    li_max = []
    li_min = []
    for i in range(0, len(ds), 2):  # 分成最大最小分别存储
        li_max.append(ds[i])
        li_min.append(ds[i + 1])
    nu_max = np.asarray(li_max)  # 转换为数组
    nu_min = np.asarray(li_min)
    return nu_max, nu_min


def searchButtonClicked(y_test, y_test_pred):
    #############第一张图##################
    fig = Figure(figsize=(5, 4), dpi=100)
    axes1 = fig.add_subplot(121, facecolor=(.18, .31, .31))
    axes1.set_facecolor('#eafff5')
    axes1.set_title('Result of Test(1)')
    t = np.arange(0, len(y_test), 1)
    p1 = axes1.plot(t, y_test)
    p2 = axes1.plot(t, y_test_pred)
    axes1.legend((p1[0], p2[0]), ('y_test', 'y_test_pred'))
    axes1.set_ylabel('The Value of Variable')
    axes1.set_xlabel('Seq')
    axes1.set_ylim(np.min(y_test) - 10, np.max(y_test) + 10)
    axes1.tick_params(labelcolor='tab:orange')

    print('====================================================')
    ############第二张图###################
    axes2 = fig.add_subplot(122, facecolor=(.18, .31, .31))
    axes2.set_facecolor('#eafff5')
    axes2.set_title('Result of Test(2)')
    p11 = axes2.plot(y_test, y_test, 'xkcd:crimson')
    p22 = axes2.scatter(y_test, np.sort(y_test_pred))
    axes2.legend((p11[0], p22), ('y_test', 'y_test_pred'))
    axes2.set_ylabel('The Value of Validation Set')
    axes2.set_xlabel('The Value of Validation Set')
    axes2.tick_params(labelcolor='tab:orange')


# 可视化
def get_show(y_test, y_test_pred):
    fig, axs0 = plt.subplots()
    fig.subplots_adjust(left=0.5, wspace=0.6)
    t = np.arange(0, len(y_test), 1)
    # Fixing random state for reproducibility
    ax1 = axs0
    p1 = ax1.plot(t, y_test,linewidth=0.9)
    p2 = ax1.plot(t, y_test_pred,linewidth=0.9)
    ax1.legend((p1[0], p2[0]), ('y_test', 'y_test_pred'))
    ax1.set_ylabel('The Value of Variable')
    ax1.set_xlabel('Seq')
    ax1.set_ylim(np.min(y_test) - 10, np.max(y_test) + 10)
    # ax1.tick_params(labelcolor='tab:orange')
    plt.show()

    fig1, axs2 = plt.subplots()
    ax2 = axs2
    ax2.set_title('True & Prediction')
    p11 = ax2.plot(y_test, y_test,'xkcd:green',linewidth=3)
    p22 = ax2.scatter(y_test, np.sort(y_test_pred))
    ax2.legend((p11[0], p22), ('y_test', 'y_test_pred'))
    ax2.set_ylabel('The Value of Validation Set')
    ax2.set_xlabel('The Value of Validation Set')
    ax2.set_ylim(np.min(y_test) - 10, np.max(y_test) + 10)

    plt.show()


# 相对误差
def mean_relative_error(y_true, y_pred):
    import numpy as np
    relative_error = np.average(np.abs(y_true - y_pred) / y_true, axis=0)
    return relative_error


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    filename = myshow.msg()
    read = pd.read_excel(filename)
    ts = read.iloc[:, 0:read.columns.size].values  # 读取所有列，
    ds = np.asarray(ts)  # ts转换为数组矩阵
    wnd_sz = read.columns.size  # 定义矩阵宽度
    x_1 = ds[:, 0:wnd_sz - 1]  # 输出前n - 1维的特征
    y_T = ds[:, wnd_sz - 1:wnd_sz]
    max, min = read_min_max()  # 加载数据中的最大最小值用于还原归一化
    x_nomal = np.full((len(x_1), wnd_sz - 1), -1000., dtype=float)  # 创建一个空数组,用来存储float类型的归一值
    for i in range(0, len(x_1)):
        for j in range(0, len(x_1[i])):
            x = x_1[i]
            new = x_nomal[i]
            up = float(x[j]) - float(min[j])
            down = float(max[j]) - float(min[j])
            new[j] = up / down  # 归一化

    model = load_model()  # 加载模型
    y = model.predict(x_nomal)  # 预测加载值
    y = y * (float(max[-1]) - float(min[-1])) + float(min[-1])
    get_show(y_T, y)
    p = []
    for i in range(len(y)):
        p.append((float(abs(y[i] - y_T[i])) / float(y_T[i])) * float(100))
    m_re_error = mean_relative_error(y_T, y)
    print("*****************************************************************************************************************")
    print("平均相对误差：            ", m_re_error * 100, "     (%)")
    print("**************************************************************************************************************")
    print("预测值(kw)：               真实值(kw):                     误差百分比(%):     ")
    for i in range(len(y)):
        print(y[i], "               ", y_T[i], "                        ", p[i])

main()

