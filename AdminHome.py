from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout
from PyQt5.QtGui import QFont\
# ,QPalette,QBrush,QPixmap

from time import sleep
from PyQt5.QtWidgets import QHBoxLayout
# ,QMainWindow,QAction,QApplication
# from PyQt5.QtGui import QIcon
# from qdarkstyle import load_stylesheet_pyqt5
# from sys import argv,exit
from win32api import GetSystemMetrics
from win32con import SM_CXSCREEN,SM_CYSCREEN
from ctypes import c_long,pythonapi,py_object
from inspect import isclass

from modelTrain import modelTrain
from BookStorageViewer import BookStorageViewer
from UserManage import UserManage

class AdminHome(QWidget):
    iFenbianlv_x = GetSystemMetrics(SM_CXSCREEN)
    iFenbianlv_y = GetSystemMetrics(SM_CYSCREEN)
    flag = 0
    def __init__(self):
        super(AdminHome, self).__init__()
        self.setUpUI()

    def setUpUI(self):
        self.resize(self.iFenbianlv_x, self.iFenbianlv_y)
        self.setWindowTitle("欢迎使用银河智维AI系统")
        self.layout = QVBoxLayout()
        self.buttonlayout = QHBoxLayout()
        self.setLayout(self.layout)

        font = QFont()
        font.setPixelSize(16)
        self.userManageButton = QPushButton("模型预测")
        self.addBookButton = QPushButton("训练模型1")
        self.addBookButton1 = QPushButton("训练模型2")
        self.addBookButton2 = QPushButton("训练模型3")
        self.addBookButton3 = QPushButton("训练模型4")
        self.userManageButton.setFont(font)
        self.addBookButton.setFont(font)
        self.addBookButton1.setFont(font)
        self.addBookButton2.setFont(font)
        self.addBookButton3.setFont(font)
        self.userManageButton.setFixedWidth(100)
        self.userManageButton.setFixedHeight(42)
        self.addBookButton.setFixedWidth(100)
        self.addBookButton.setFixedHeight(42)
        self.addBookButton1.setFixedWidth(100)
        self.addBookButton1.setFixedHeight(42)
        self.addBookButton2.setFixedWidth(100)
        self.addBookButton2.setFixedHeight(42)
        self.addBookButton3.setFixedWidth(100)
        self.addBookButton3.setFixedHeight(42)
        self.buttonlayout.addWidget(self.addBookButton)
        self.buttonlayout.addWidget(self.addBookButton1)
        self.buttonlayout.addWidget(self.addBookButton2)
        self.buttonlayout.addWidget(self.addBookButton3)
        self.buttonlayout.addWidget(self.userManageButton)
        self.layout.addLayout(self.buttonlayout)
        self.storageView = BookStorageViewer()
        self.layout.addWidget(self.storageView)
        self.addBookButton.clicked.connect(self.addBookButtonClicked)
        self.addBookButton1.clicked.connect(self.addBookButtonClicked1)
        self.addBookButton2.clicked.connect(self.addBookButtonClicked2)
        self.addBookButton3.clicked.connect(self.addBookButtonClicked3)
        self.userManageButton.clicked.connect(self.userManage)

    def addBookButtonClicked(self):
        if self.flag == 2:
            self._async_raise_21()
            self._async_raise_22()
            sleep(0.1)
        if self.flag == 3:
            self._async_raise_31()
            self._async_raise_32()
            sleep(0.1)
        if self.flag == 4:
            self._async_raise_41()
            self._async_raise_42()
            sleep(0.1)
        self.flag = 1
        self.storageView.text_browser.clear()
        self.storageView.reDirect()
        self.storageView.clearFigure()

        self.addDialog = modelTrain(self)
        self.addDialog.addBookButtonCicked()
        self.addDialog.setVisible(False)
        self.addDialog.get_result_signal.connect(self.storageView.searchButtonClicked)
        self.addDialog.set_flag_signal.connect(self.setFlag)

    def addBookButtonClicked1(self):
        if self.flag == 1:
            self._async_raise_11()
            self._async_raise_12()
            sleep(0.1)
        if self.flag == 3:
            self._async_raise_31()
            self._async_raise_32()
            sleep(0.1)
        if self.flag == 4:
            self._async_raise_41()
            self._async_raise_42()
            sleep(0.1)
        self.flag = 2
        self.storageView.text_browser.clear()
        self.storageView.reDirect()
        self.storageView.clearFigure()

        self.addDialog = modelTrain(self)
        self.addDialog.addBookButtonCicked1()
        self.addDialog.get_result_signal.connect(self.storageView.searchButtonClicked)
        self.addDialog.set_flag_signal.connect(self.setFlag)

    def addBookButtonClicked2(self):
        if self.flag == 1:
            self._async_raise_11()
            self._async_raise_12()
            sleep(0.1)
        if self.flag == 2:
            self._async_raise_21()
            self._async_raise_22()
            sleep(0.1)
        if self.flag == 4:
            self._async_raise_41()
            self._async_raise_42()
            sleep(0.1)
        self.flag = 3
        self.storageView.text_browser.clear()
        self.storageView.reDirect()
        self.storageView.clearFigure()

        self.addDialog = modelTrain(self)
        self.addDialog.addBookButtonCicked2()
        self.addDialog.get_result_signal.connect(self.storageView.searchButtonClicked)
        self.addDialog.set_flag_signal.connect(self.setFlag)

    def addBookButtonClicked3(self):
        if self.flag == 1:
            self._async_raise_11()
            self._async_raise_12()
            sleep(0.1)
        if self.flag == 2:
            self._async_raise_21()
            self._async_raise_22()
            sleep(0.1)
        if self.flag == 3:
            self._async_raise_31()
            self._async_raise_32()
            sleep(0.1)
        self.flag = 4
        self.storageView.text_browser.clear()
        self.storageView.reDirect()
        self.storageView.clearFigure()

        self.addDialog = modelTrain(self)
        self.addDialog.addBookButtonCicked3()
        self.addDialog.get_result_signal.connect(self.storageView.searchButtonClicked)
        self.addDialog.set_flag_signal.connect(self.setFlag)

    def _async_raise1(self):
        tid = self.addDialog.train.thread.ident
        exctype = SystemExit
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

    def _async_raise2(self):
        tid = self.addDialog.train.ident
        exctype = SystemExit
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

    def _async_raise_11(self):
        tid = self.addDialog.train.thread.ident
        exctype = SystemExit
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

    def _async_raise_12(self):
        tid = self.addDialog.train.ident
        exctype = SystemExit
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

    def _async_raise_21(self):
        tid = self.addDialog.train.thread.ident
        exctype = SystemExit
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

    def _async_raise_22(self):
        tid = self.addDialog.train.ident
        exctype = SystemExit
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

    def _async_raise_31(self):
        tid = self.addDialog.train.thread.ident
        exctype = SystemExit
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

    def _async_raise_32(self):
        tid = self.addDialog.train.ident
        exctype = SystemExit
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

    def _async_raise_41(self):
        tid = self.addDialog.train.thread.ident
        exctype = SystemExit
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

    def _async_raise_42(self):
        tid = self.addDialog.train.ident
        exctype = SystemExit
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

    def userManage(self):
        if self.flag == 1:
            self._async_raise_11()
            self._async_raise_12()
            sleep(0.1)
        if self.flag == 2:
            self._async_raise_21()
            self._async_raise_22()
            sleep(0.1)
        if self.flag == 3:
            self._async_raise_31()
            self._async_raise_32()
            sleep(0.1)
        if self.flag == 4:
            self._async_raise_41()
            self._async_raise_42()
            sleep(0.1)
        self.flag = 0
        self.storageView.text_browser.clear()
        self.storageView.reDirect()
        self.modelPredict = UserManage()
        self.modelPredict.start()

    def close(self):
        if self.flag == 1:
            self._async_raise_11()
            self._async_raise_12()
            sleep(0.1)
        if self.flag == 2:
            self._async_raise_21()
            self._async_raise_22()
            sleep(0.1)
        if self.flag == 3:
            self._async_raise_31()
            self._async_raise_32()
            sleep(0.1)
        if self.flag == 4:
            self._async_raise_41()
            self._async_raise_42()
            sleep(0.1)
        self.flag = 0

    def setFlag(self):
        self.flag = 0
#
# if __name__ == "__main__":
#     app = QApplication(argv)
#     app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
#     app.setStyleSheet(load_stylesheet_pyqt5())
#     mainMindow = AdminHome()
#     palette = QPalette()
#     palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/cg.png")))
#     mainMindow.setPalette(palette)
#     mainMindow.show()
#     exit(app.exec_())
