# -*- coding: utf-8 -*-
import sys
import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
sys.path.append(os.getcwd())
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys,win32api,win32con
import numpy as np

class MyMplCanvas(FigureCanvas):
    update_signal = pyqtSignal()
    def __init__(self, width=5, height=4, dpi=80):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, self.fig)

class EmittingStr(QtCore.QObject): #输出重定向
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号
    def write(self, text):
        self.textWritten.emit(str(text))

class BookStorageViewer(QWidget):
    iFenbianlv_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    iFenbianlv_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    def __init__(self):
        super(BookStorageViewer, self).__init__()
        self.resize(self.iFenbianlv_x, self.iFenbianlv_y)
        self.setWindowTitle("欢迎使用银河智维AI系统")
        self.setUpUI()

    def reDirect(self):
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)

    def outputWritten(self, text):
        cursor = self.text_browser.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.text_browser.setTextCursor(cursor)
        self.text_browser.ensureCursorVisible()

    def setUpUI(self):
        self.layout = QVBoxLayout()
        self.Hlayout1 = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()

        self.text_browser = QTextBrowser(self)
        # pixmap = QPixmap('./images/cg.png')
        # self.text_browser.setBackgroundRole(pixmap)
        # self.text_browser.set
        palette1 = QPalette()
        # palette1.setColor(self.backgroundRole(), QColor(192, 253, 123))  # 设置背景颜色
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('./images/cg.png')))  # 设置背景图片
        self.text_browser.setPalette(palette1)
        # setPixmap(pixmap)
        # self.text_browser.setPalette(palette)
        self.text_browser.setFixedHeight(2*(self.iFenbianlv_y/6))
        self.text_browser.setFixedWidth(self.iFenbianlv_x - 200)
        self.Hlayout1.addWidget(self.text_browser)

        # Hlayout2初始化
        self.graphicsView_1 = QGraphicsView(self)
        self.graphicsView_2 = QGraphicsView(self)
        self.fie = QGridLayout(self.graphicsView_1)
        self.fie1 = QGridLayout(self.graphicsView_2)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(self.graphicsView_1)
        Hlayout.addWidget(self.graphicsView_2)

        widget = QWidget()
        widget.setLayout(Hlayout)
        widget.setFixedWidth(self.iFenbianlv_x - 180)
        self.Hlayout2.addWidget(widget)

        self.layout.addLayout(self.Hlayout1)
        self.layout.addLayout(self.Hlayout2)
        self.setLayout(self.layout)

    def searchButtonClicked(self, result):
        y_test, y_test_pred, y_ = result[2], result[3], result[4]
        #############第一张图##################
        F1 = MyMplCanvas(3,3,80)
        axes1 = F1.fig.add_subplot(111,facecolor=(.18, .31, .31))
        axes1.set_facecolor('#eafff5')
        axes1.set_title('Result of Test(1)')
        t = np.arange(0, len(y_test), 1)
        p1 = axes1.plot(t, y_test, linewidth=0.9)
        p2 = axes1.plot(t, y_test_pred, linewidth=0.9)
        axes1.legend((p1[0], p2[0]), ('y_test', 'y_test_pred'))
        axes1.set_ylabel('The Value of Variable')
        axes1.set_xlabel('Seq')
        axes1.set_ylim(np.min(y_test) - 10, np.max(y_test) + 10)
        axes1.tick_params(labelcolor='tab:orange')
        while self.fie.count():
            item = self.fie.takeAt(0)
            widget = item.widget()
            widget.deleteLater()
        self.fie.addWidget(F1)
        ############第二张图###################
        F2 = MyMplCanvas(3, 3, 80)
        axes2 = F2.fig.add_subplot(111,facecolor=(.18, .31, .31))
        axes2.set_facecolor('#eafff5')
        axes2.set_title('Result of Test(2)')
        p11 = axes2.plot(y_test, y_test,'xkcd:crimson', linewidth=3)
        p22 = axes2.scatter(y_test, np.sort(y_test_pred))
        axes2.legend((p11[0], p22), ('y_test', 'y_test_pred'))
        axes2.set_ylabel('The Value of Validation Set')
        axes2.set_xlabel('The Value of Validation Set')
        axes2.tick_params(labelcolor='tab:orange')
        while self.fie1.count():
            item = self.fie1.takeAt(0)
            widget = item.widget()
            widget.deleteLater()
        self.fie1.addWidget(F2)

    def clearFigure(self):
        while self.fie.count():
            item1 = self.fie.takeAt(0)
            widget1 = item1.widget()
            widget1.deleteLater()
        while self.fie1.count():
            item2 = self.fie1.takeAt(0)
            widget2 = item2.widget()
            widget2.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = BookStorageViewer()
    mainMindow.show()
    sys.exit(app.exec_())

