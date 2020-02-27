# import sys
# import qdarkstyle
# from PyQt5.QtGui import *

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from dnnThread import dnnThread

class modelTrain(QDialog):
    set_flag_signal = pyqtSignal()
    get_result_signal = pyqtSignal(list)
    def __init__(self, parent=None):
        super(modelTrain, self).__init__(parent)

    def addBookButtonCicked(self):
        layer = int(4)
        epochs = int(100)
        batches = int(4)
        learnRate = float(0.01)
        self.train = dnnThread(layer, batches, epochs,learnRate)
        self.train.setDaemon(True)
        self.train.start()
        self.train.dnnThread_signal.connect(self.getResult)
        self.close()

    def addBookButtonCicked1(self):
        layer = int(4)
        epochs = int(100)
        batches = int(4)
        learnRate = float(0.03)
        self.train = dnnThread(layer, batches, epochs,learnRate)
        self.train.setDaemon(True)
        self.setVisible(False)
        self.train.start()
        self.train.dnnThread_signal.connect(self.getResult)
        self.close()

    def addBookButtonCicked2(self):
        layer = int(4)
        epochs = int(100)
        batches = int(6)
        learnRate = float(0.01)
        self.train = dnnThread(layer, batches, epochs,learnRate)
        self.train.setDaemon(True)
        self.setVisible(False)
        self.train.start()
        self.train.dnnThread_signal.connect(self.getResult)
        self.close()

    def addBookButtonCicked3(self):
        layer = int(4)
        epochs = int(100)
        batches = int(6)
        learnRate = float(0.03)
        self.train = dnnThread(layer, batches, epochs,learnRate)
        self.train.setDaemon(True)
        self.setVisible(False)
        self.train.start()
        self.train.dnnThread_signal.connect(self.getResult)
        self.close()

    def getResult(self, result):
        self.get_result_signal.emit(result)
        self.set_flag_signal.emit()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
#     app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
#     mainMindow = modelTrain()
#     mainMindow.show()
#     sys.exit(app.exec_())
