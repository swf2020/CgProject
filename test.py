
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

app = QApplication(sys.argv)
win = QMainWindow()

#设置窗口标题与初始大小
win.setWindowTitle("界面背景图片设置")
win.resize(350, 250)
#设置对象名称
win.setObjectName("MainWindow")

# #todo 1 设置窗口背景图片
win.setStyleSheet("#MainWindow{border-image:url(./images/cg.png);}")

#todo 2 设置窗口背景色
#win.setStyleSheet("#MainWindow{background-color: yellow}")

win.show()
sys.exit(app.exec_())

# app = QApplication(sys.argv)
# win = QMainWindow()
# win.setWindowOpacity(0.51)
# win.setWindowTitle("界面背景图片设置")
# palette = QPalette()
# palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/cg.png")))
# win.setPalette(palette)
#
# # todo 1 当背景图片的宽度和高度大于窗口的宽度和高度时
# win.resize(460,  255 )
# #
# # # todo 2 当背景图片的宽度和高度小于窗口的宽度和高度时
# # win.resize(800, 600)
#
# win.show()
# sys.exit(app.exec_())
