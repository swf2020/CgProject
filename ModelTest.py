# -*- coding: utf-8 -*-
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# import qdarkstyle
# import sys
from tensorflow import keras
import numpy as np  # 用于转换数据
import pandas as pd  # 用于分析数据集
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget,QFileDialog
from threading import Thread


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
    def msg(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                          "All Files (*);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔
        return fileName1

class ModelTest(Thread):
    def load_model(self):  # 加载模型
        with open(r'./model_train/model.json', 'r') as file:
            model_json1 = file.read()
        model = keras.models.model_from_json(model_json1)  # 返回模型结构
        model.load_weights("./model_train/model.hdf5", by_name=False)  # 加载模型的权重
        return model

    #加载基本数据进行归一化
    def read_min_max(self):
        filename = "./model_train/data.txt"
        with open(filename, 'r+', encoding='utf-8') as f:
            for lines in f.readlines():
                ss = lines.strip('[]').split(', ')
        ds = np.asarray(ss)
        li_max = []
        li_min = []
        for i in range(0, len(ds), 2): #分成最大最小分别存储
            li_max.append(ds[i])
            li_min.append(ds[i + 1])
        nu_max = np.asarray(li_max) #转换为数组
        nu_min = np.asarray(li_min)
        return nu_max, nu_min

    def main(self):
        myshow = MyWindow()
        fn = myshow.msg()  # 文本框加载文件
        read = pd.read_excel(fn)
        ts = read.iloc[:, 0:read.columns.size].values  # 读取所有列数据
        ds = np.asarray(ts)  # ts转换为数组矩阵
        wnd_sz = read.columns.size  # 定义矩阵宽度
        x_1 = ds[:, 0:wnd_sz - 1]  # 输出前n - 1维的特征
        y_T = ds[:, wnd_sz - 1:wnd_sz]
        max, min = self.read_min_max()  # 加载数据中的最大最小值用于还原归一化
        x_nomal = np.full((len(x_1), wnd_sz - 1), -1000., dtype=float)  # 创建一个空数组,用来存储float类型的归一值
        for i in range(0, len(x_1)):
            for j in range(0, len(x_1[i])):
                x = x_1[i]
                new = x_nomal[i]
                up = float(x[j]) - float(min[j])
                down = float(max[j]) - float(min[j])
                new[j] = up / down  # 归一化

        model = self.load_model()  # 加载模型
        y = model.predict(x_nomal)  # 预测加载值
        y = y * (float(max[-1]) - float(min[-1])) + float(min[-1])
        p = []
        for i in range(len(y)):
            p.append((float(abs(y[i] - y_T[i])) / float(y_T[i])) * float(100))
        print(
            "**************************************************************************************************************")
        print(
            "**************************************************************************************************************")
        print(
            "**************************************************************************************************************")
        print("预测值(kw)：               真实值(kw):                     误差百分比(%):     ")
        for i in range(len(y)):
            print(y[i], "               ", y_T[i], "                        ", p[i])

    def run(self):
            self.main()

#
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
#     myshow = MyWindow()
#     filename = myshow.msg()  # 文本框加载文件
#     user = ModelTest()
#     user.start()
#
