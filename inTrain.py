from PyQt5.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QPushButton
from PyQt5.QtGui import QFont
import random
from time import sleep
from win32api import GetSystemMetrics
from win32con import SM_CXSCREEN,SM_CYSCREEN
from threading import Thread
from ctypes import c_long,pythonapi,py_object
from inspect import isclass

from addParameter import addParameter
from ConfigurationView import ConfigurationView
from ModelTest import ModelTest

class printThread(Thread):
    def __init__(self):
        super(printThread, self).__init__()
        self.flag = True

    def changeFlag(self):
        self.flag = False

    def run(self):
        print("Train on Y_Train samples, validate on Y_Text samples")
        i = 1
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

class inTrainWidget(QWidget):
    iFenbianlv_x = GetSystemMetrics(SM_CXSCREEN)
    iFenbianlv_y = GetSystemMetrics(SM_CYSCREEN)
    train_is_begin = False
    flag = -1
    count = 0
    def __init__(self):
        super(inTrainWidget, self).__init__()
        self.setUpUI()

    def setUpUI(self):
        self.resize(self.iFenbianlv_x, self.iFenbianlv_y)
        self.setWindowTitle("欢迎使用银河智维AI系统")
        self.layout = QHBoxLayout()
        self.buttonlayout = QVBoxLayout()
        self.setLayout(self.layout)

        font = QFont()
        font.setPixelSize(16)
        self.userManageButton = QPushButton("测试模型")
        self.configurePButton = QPushButton("选定参数")
        self.continueTrainPButton = QPushButton("继续训练")
        self.stopTrainPButton = QPushButton("暂停训练")
        self.userManageButton.setFont(font)
        self.configurePButton.setFont(font)
        self.continueTrainPButton.setFont(font)
        self.stopTrainPButton.setFont(font)
        self.userManageButton.setFixedWidth(100)
        self.userManageButton.setFixedHeight(42)
        self.configurePButton.setFixedWidth(100)
        self.configurePButton.setFixedHeight(42)
        self.continueTrainPButton.setFixedWidth(100)
        self.continueTrainPButton.setFixedHeight(42)
        self.stopTrainPButton.setFixedWidth(100)
        self.stopTrainPButton.setFixedHeight(42)
        self.buttonlayout.addWidget(self.configurePButton)
        self.buttonlayout.addWidget(self.continueTrainPButton)
        self.buttonlayout.addWidget(self.stopTrainPButton)
        self.buttonlayout.addWidget(self.userManageButton)
        self.layout.addLayout(self.buttonlayout)
        self.cView = ConfigurationView()
        self.layout.addWidget(self.cView)
        self.configurePButton.clicked.connect(self.configureParameterClicked)
        self.userManageButton.clicked.connect(self.userManage)
        self.continueTrainPButton.clicked.connect(self.ContinueTrain)
        self.stopTrainPButton.clicked.connect(self.stopThreading)

    def configureParameterClicked(self):
        self.cView.text_browser.clear()
        self.cView.reDirect()
        self.addDialog = addParameter(self)
        self.addDialog.get_result_signal.connect(self.cView.searchButtonClicked)
        self.addDialog.show()
        self.train_is_begin = True
        self.count = 1
        self.addDialog.exec_()

    def userManage(self):
        self.cView.text_browser.clear()
        self.cView.reDirect()
        self.modelPredict = ModelTest()
        self.modelPredict.start()

    def ContinueTrain(self):
        if self.train_is_begin:
            if self.flag == 3:
                # self.cView.reDirect()
                if self.addDialog.flag == 2 and self.addDialog.train.is_alive():
                    self.flag = 2
                    self.pt = printThread()
                    self.pt.start()
                    self.addDialog.train.dnnTrainThread_exit_signal.connect(self.pt.changeFlag)

    def stopThreading(self):
        if self.train_is_begin:
            if self.flag == 2:
                self.flag = 3
                self._async_raise(self.pt.ident, SystemExit)
            if self.count == 1 and self.addDialog.flag == 2:
                self.count += 1
                if self.addDialog.train.is_alive():
                    self.flag = 3
                    self._async_raise(self.addDialog.train.thread.ident, SystemExit)

    def _async_raise(self, tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = c_long(tid)
        if not isclass(exctype):
            exctype = type(exctype)
        res = pythonapi.PyThreadState_SetAsyncExc(tid, py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
#     app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
#     mainMindow = inTrainWidget()
#     mainMindow.show()
#     sys.exit(app.exec_())
