
from PyQt5.QtWidgets import QDialog, QFormLayout,QLabel,QPushButton,QComboBox,QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal,Qt

from dnnThread import dnnThread

class addBookDialog(QDialog):
    get_result_signal = pyqtSignal(list)
    train_signal = pyqtSignal(int,int,int,float)
    def __init__(self, parent=None):
        super(addBookDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("配置超参数")

    def setUpUI(self):
        trainLayer = ["请选择", "3", "4", "5", "6", "7", "8", "9", "10"]
        epoches = ["请选择", "100", "150", "200", "250", "300", "400", "500","100"]
        batches = ["请选择", "4", "6", "8", "10", "12", "14", "16", "20", "24"]
        learnRate = ["请选择", "0.01", "0.03", "0.05", "0.07", "0.1", "0.3", "0.5"]
        self.resize(300, 220)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Label控件
        self.titlelabel = QLabel("  配置超参数")
        self.trainLayerLabel = QLabel("层    数：")
        self.epochsLabel =QLabel("迭代次数：")
        self.batchesLabel = QLabel("批   次：")
        self.learnRateLabel = QLabel("学 习 率：")

        # button控件
        self.addBookButton = QPushButton("添加文件并训练")

        # lineEdit控件
        self.trainLayerComboBox = QComboBox()
        self.epochsComboBox = QComboBox()
        self.batchesComboBox = QComboBox()
        self.learnRateComboBox = QComboBox()
        self.trainLayerComboBox.addItems(trainLayer)
        self.epochsComboBox.addItems(epoches)
        self.batchesComboBox.addItems(batches)
        self.learnRateComboBox.addItems(learnRate)

        # 添加进formlayout
        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.trainLayerLabel, self.trainLayerComboBox)
        self.layout.addRow(self.epochsLabel, self.epochsComboBox)
        self.layout.addRow(self.batchesLabel, self.batchesComboBox)
        self.layout.addRow(self.learnRateLabel, self.learnRateComboBox)
        self.layout.addRow("", self.addBookButton)

        # 设置字体
        font = QFont()
        font.setPixelSize(20)
        self.titlelabel.setFont(font)
        font.setPixelSize(14)
        self.trainLayerLabel.setFont(font)
        self.epochsLabel.setFont(font)
        self.batchesLabel.setFont(font)
        self.learnRateLabel.setFont(font)

        self.trainLayerComboBox.setFont(font)
        self.epochsComboBox.setFont(font)
        self.batchesComboBox.setFont(font)
        self.learnRateComboBox.setFont(font)

        # button设置
        font.setPixelSize(16)
        self.addBookButton.setFont(font)
        self.addBookButton.setFixedHeight(32)
        self.addBookButton.setFixedWidth(140)

        # 设置间距
        self.titlelabel.setMargin(6)
        self.layout.setVerticalSpacing(40)

        self.addBookButton.clicked.connect(self.addBookButtonCicked)

    def addBookButtonCicked(self):
        layer = self.trainLayerComboBox.currentText()
        epochs = self.epochsComboBox.currentText()
        batches = self.batchesComboBox.currentText()
        learnRate = self.learnRateComboBox.currentText()
        if (
                layer == "请选择" or epochs == "请选择" or batches == "请选择" or learnRate == "请选择"):
            print(QMessageBox.warning(self, "提示", "请选择相关参数", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            layer = int(layer)
            batches = int(batches)
            epochs = int(epochs)
            learnRate = float(learnRate)
            self.train = dnnThread(layer, batches, epochs,learnRate)
            self.setVisible(False)
            self.train.start()
            self.train.dnnThread_signal.connect(self.getResult)
            self.close()
        return

    def getResult(self, result):
        self.get_result_signal.emit(result)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
#     app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
#     mainMindow = addBookDialog()
#     palette = QPalette()
#     palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/cg.png")))
#     mainMindow.setPalette(palette)
#     mainMindow.show()
#     sys.exit(app.exec_())
