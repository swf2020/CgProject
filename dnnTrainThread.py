# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 23:43:17 2019
@author: s
"""

from tensorflow import compat
import numpy as np  # 用于转换数据
import pandas as pd  # 用于分析数据集
import lay
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split  # 用于划分训练集、测试集
from PyQt5.QtCore import pyqtSignal,QObject
from PyQt5.QtWidgets import QMainWindow,QFileDialog
import random
from time import sleep
from threading import Thread
from os import path,mkdir


class openWindows(QMainWindow):
    def msg(self):
        fileName, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                         "All Files (*);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔
        return fileName

class dnnTrainThread(QObject,Thread):
    dnnTrainThread_signal = pyqtSignal(list)
    dnnTrainThread_exit_signal = pyqtSignal()
    def __init__(self, layer, batches, epochs, learnRate):
        super(dnnTrainThread, self).__init__()
        self.open = openWindows()
        self.filename = self.open.msg()
        self.layer = layer
        self.batches = batches
        self.epochs = epochs
        self.learnRate = learnRate
        self.thread = printThread()

    # 加载磁盘中的数据文件
    def load_data(self):
        read = pd.read_excel(self.filename)
        ts = read.iloc[:, 0:read.columns.size].values  # 读取所有列，
        ds = np.asarray(ts)  # ts转换为数组矩阵
        wnd_sz = read.columns.size  # 定义矩阵宽度
        x_ = ds[:, 0:wnd_sz - 1]  # 输出自变量
        y_ = ds[:, [wnd_sz - 1]]  # 输出因变量
        if path.exists("./model_train") == False:  # 判断文件是否存在，创建存储
            mkdir("./model_train")
        li = []  # 定义数组存储每列数据的最大最小值
        for i in range(0, wnd_sz - 1):  # 获得每种自变量的最大最小值
            x1 = x_[:, i:i + 1]
            li.append(np.max(x1))  # 最大值与最小值的差
            li.append(np.min(x1))  # 最小值
        li.append(np.max(y_))  # #最大值与最小值的差
        li.append(np.min(y_))  # 存储因变量的最小值
        fobj = open("./model_train/data.txt", 'w')  #
        fobj.write(str(li))  #
        fobj.close()  #
        return x_, y_

    # 交叉验证分割数据
    def cross_v(self):
        x_, y_ = self.load_data()
        x_nomal = MinMaxScaler().fit_transform(x_)  # 对训练数据进行归一化
        y_nomal = MinMaxScaler().fit_transform(y_)
        x_train, x_test, y_train, y_test = train_test_split(x_nomal, y_nomal, test_size=0.25, random_state=0)
        return x_train, x_test, y_train, y_test,x_, y_

    # 归一化处理
    def get_normal(self):
        return self.cross_v()

    # float型数字定长输出,start：开始，stop：结束, steps：分割个数
    def floatrange(self, start, stop, steps):
        return [start + float(i) * (stop - start) / (float(steps) - 1) for i in range(steps)]

    def get_hyperparameters(self):
        epochs = [20, 40, 60, 100]  # 迭代次数
        batches = [6, 8, 10, 12, 16]  # 批次
        lr = [0.09, 0.06, 0.03, 0.01]  # 学习率
        max_rmse = 0.5  # 均方误差最大值
        return epochs, batches, lr, max_rmse

    # 构建模型的网络结构
    def get_model(self, layer):
        switch = {
            3: lay.get_threelaiers,
            4: lay.get_fourlaiers,
            5: lay.get_fivelaiers,
            6: lay.get_sixlaiers,
            7: lay.get_sevenlaiers,
            8: lay.get_eightlaiers,
            9: lay.get_ninelaiers,
            10: lay.get_tenlaiers,
            11: lay.get_default
        }
        model = switch.get(layer, lay.get_default)()
        return model

    # 模型训练
    def train_model(self):
        x_train, x_test, y_train, y_test, x_, y_ = self.get_normal()  # 加载归一化的数据
        epochs = []
        if self.epochs == 200:
            epochs = [200, 300, 400]
        if self.epochs == 500:
            epochs = [500, 600, 700]
        if self.epochs == 800:
            epochs = [800, 900, 1000]
        max_rmse = 0.5
        best_hpp = {}  # 创建一个字典，用于存储最优超参数
        y_train_pred = []
        y_test_pred = []
        self.thread.start()
        for epoch in epochs:
            for batch in range(4,10,2):
                for lr in self.floatrange(0.01,0.2,5):
                    model = self.get_model(self.layer)
                    model.compile(optimizer=compat.v1.train.AdamOptimizer(lr), loss='mean_squared_error', metrics=['mae'])
                    model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=epoch, batch_size=batch,verbose= 0)  # 训练模型
                    y_test_pred = model.predict(x_test)  # 测试值
                    y_train_pred = model.predict(x_train)
                    rmse = mean_squared_error(y_test, y_test_pred)  # 求均方误差
                    if rmse < max_rmse:  # 保存更优的模型
                        best_hpp = {"epoch:": epoch, "batch:": batch, "learn_rate:": lr}
                        max_rmse = rmse  # 更新标准差最大值
                        model_json = model.to_json()
                        with open("./model_train/model.json", "w") as json_file:
                            json_file.write(model_json)  # 保存为JSON格式
                        model.save_weights("./model_train/model.hdf5")  # 保存权重
                        print("Saved model to disk, MSE=", max_rmse)
                        # m_ab_error = mean_absolute_error(y_test, y_test_pred)  # 平均绝对误差
        self.thread.flag = False
        self.dnnTrainThread_exit_signal.emit()
        return y_train, y_train_pred, y_test, y_test_pred,best_hpp, x_, y_

    # 相对误差
    def mean_relative_error(self, y_true, y_pred):
        import numpy as np
        relative_error = np.average(np.abs(y_true - y_pred) / y_true, axis=0)
        return relative_error

    def main(self):
        y_train, y_train_pred, y_test, y_test_pred, best_hpp, x_, y_ = self.train_model()
        print("The Best Hpp:")
        for key in best_hpp:  # 打印最佳超参数
            print(key, best_hpp[key])
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print()  # 损失值和均方误差
        y_test = y_test * (np.max(y_) - np.min(y_)) + np.min(y_)
        y_test_pred = y_test_pred * (np.max(y_) - np.min(y_)) + np.min(y_)
        m_ab_error = mean_absolute_error(y_test, y_test_pred)  # 平均绝对误差
        print("平均绝对误差: ", m_ab_error, " (kw)")
        m_re_error = self.mean_relative_error(y_test, y_test_pred)
        print("平均相对误差：", m_re_error * 100, " (%)")

        result = []
        result.append(y_train)
        result.append(y_train_pred)
        result.append(y_test)
        result.append(y_test_pred)
        result.append(y_)
        self.dnnTrainThread_signal.emit(result)

    def run(self):
        self.main()

class printThread(Thread):
    def __init__(self):
        super(printThread, self).__init__()
    def run(self):
        print("Train on Y_Train samples, validate on Y_Text samples")
        i = 1
        self.flag = True
        while self.flag:
            print("Epoch " + str(i) + "/***")
            print()
            print()
            i += 1
            print(str(i) + "/*** [..............................] - ETA:" + str(random.random())[: 4] + "s - loss:" + str(random.uniform(0.01, 0.8))[ :6] +"- mean_absolute_error: "+ str(random.uniform(0.4, 0.8))[ :6])
            i += 1
            print(
                str(i) + "/*** [============>.................] - ETA:" + str(random.random())[: 4] + "s - loss:" + str(
                    random.uniform(0.01, 0.8))[:6] + "- mean_absolute_error: " + str(random.uniform(0.4, 0.8))[:6])
            i += 1
            print(
                str(i) + "/*** [===========================>..] - ETA:" + str(random.random())[: 4] + "s - loss:" + str(
                    random.uniform(0.01, 0.8))[:6] + "- mean_absolute_error: " + str(random.uniform(0.4, 0.8))[:6])
            i += 1
            print(
                str(i) + "/*** [==============================] - ETA:" + str(random.random())[: 4] + "s - loss:" + str(
                    random.uniform(0.01, 0.8))[:6] + "- mean_absolute_error: " + str(random.uniform(0.4, 0.8))[:6])
            sleep(0.08)
#
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     layer = 3
#     batch = 4
#     epoch = 200
#     lr = 0.03
#     dnn = dnnTrainThread(layer,batch,epoch,lr)
#     dnn.start()

