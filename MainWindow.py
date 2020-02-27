
from PyQt5.QtWidgets import QMainWindow,QHBoxLayout,QAction,QApplication
from PyQt5.QtGui import QIcon
from sip import delete
from qdarkstyle import load_stylesheet_pyqt5
from sys import argv,exit
from win32api import GetSystemMetrics
from win32con import SM_CXSCREEN,SM_CYSCREEN

from AdminHome import AdminHome
from changePasswordDialog import changePasswordDialog
from inTrain import inTrainWidget
from SignIn import SignInWidget

class Main(QMainWindow):
    iFenbianlv_x = GetSystemMetrics(SM_CXSCREEN)
    iFenbianlv_y = GetSystemMetrics(SM_CYSCREEN)
    yanshi_flag = 0
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.widget = SignInWidget()
        self.resize(self.iFenbianlv_x, self.iFenbianlv_y)
        self.setWindowTitle("银河智维AI平台")
        self.setCentralWidget(self.widget)
        bar = self.menuBar()
        self.Menu = bar.addMenu("菜单栏")
        self.signUpAction = QAction("模型演示", self)
        self.inTrainAction = QAction("模型训练",self)
        self.changePasswordAction =QAction("修改密码",self)
        # self.signInAction = QAction("登录", self)
        # self.quitSignInAction = QAction("退出登录", self)
        self.quitAction = QAction("退出", self)
        self.Menu.addAction(self.signUpAction)
        self.Menu.addAction(self.inTrainAction)
        self.Menu.addAction(self.changePasswordAction)
        # self.Menu.addAction(self.signInAction)
        # self.Menu.addAction(self.quitSignInAction)
        self.Menu.addAction(self.quitAction)
        self.signUpAction.setEnabled(False)
        self.inTrainAction.setEnabled(False)
        self.changePasswordAction.setEnabled(True)
        # self.signInAction.setEnabled(False)
        # self.quitSignInAction.setEnabled(False)
        self.widget.is_admin_signal.connect(self.adminSignIn)
        self.widget.is_student_signal[str].connect(self.studentSignIn)
        self.Menu.triggered[QAction].connect(self.menuTriggered)

    def adminSignIn(self):
        delete(self.widget)
        self.widget = AdminHome()
        self.setCentralWidget(self.widget)
        self.signUpAction.setEnabled(False)
        self.inTrainAction.setEnabled(True)
        self.changePasswordAction.setEnabled(True)
        # self.signInAction.setEnabled(True)
        # self.quitSignInAction.setEnabled(True)

    def studentSignIn(self, studentId):
        delete(self.widget)
        self.widget = AdminHome()
        self.setCentralWidget(self.widget)
        self.signUpAction.setEnabled(False)
        self.inTrainAction.setEnabled(True)
        self.changePasswordAction.setEnabled(False)
        # self.signInAction.setEnabled(False)
        # self.quitSignInAction.setEnabled(True)

    def inTrainModel(self):
        delete(self.widget)
        self.widget = inTrainWidget()
        self.setCentralWidget(self.widget)
        self.changePasswordAction.setEnabled(True)
        self.signUpAction.setEnabled(True)
        # self.signInAction.setEnabled(False)
        # self.quitSignInAction.setEnabled(True)

    def menuTriggered(self, q):
        if(q.text()=="修改密码"):
            changePsdDialog=changePasswordDialog(self)
            changePsdDialog.show()
            changePsdDialog.exec_()
        if (q.text() == "模型演示"):
            self.yanshi_flag = 2
            delete(self.widget)
            self.widget = AdminHome()
            self.setCentralWidget(self.widget)
            self.signUpAction.setEnabled(False)
            self.inTrainAction.setEnabled(True)
            self.changePasswordAction.setEnabled(True)
            # self.signInAction.setEnabled(True)
            # self.quitSignInAction.setEnabled(True)
        if(q.text()=="模型训练"):
            if self.yanshi_flag == 2 or self.yanshi_flag == 0:
                if self.widget.flag != 0:
                    self.yanshi_flag = 1
                    self.widget.close()
            delete(self.widget)
            self.widget = inTrainWidget()
            self.setCentralWidget(self.widget)
            self.signUpAction.setEnabled(True)
            self.inTrainAction.setEnabled(False)
            self.changePasswordAction.setEnabled(True)
            # self.signInAction.setEnabled(False)
            # self.quitSignInAction.setEnabled(True)
        if (q.text() == "退出登录"):
            if self.yanshi_flag == 2 or self.yanshi_flag == 0:
                if self.widget.flag != 0:
                    self.yanshi_flag == 0
                    self.widget.close()
            if self.yanshi_flag == 1:
                self.widget.stopThreading()
                self.yanshi_flag == 0
            delete(self.widget)
            self.widget = SignInWidget()
            self.setCentralWidget(self.widget)
            self.widget.is_admin_signal.connect(self.adminSignIn)
            self.widget.is_student_signal[str].connect(self.studentSignIn)
            self.signUpAction.setEnabled(True)
            self.changePasswordAction.setEnabled(True)
            # self.signInAction.setEnabled(True)
            # self.quitSignInAction.setEnabled(False)
        if (q.text() == "登录"):
            delete(self.widget)
            self.widget = SignInWidget()
            self.setCentralWidget(self.widget)
            self.widget.is_admin_signal.connect(self.adminSignIn)
            self.widget.is_student_signal[str].connect(self.studentSignIn)
            self.signUpAction.setEnabled(True)
            self.changePasswordAction.setEnabled(True)
            # self.signInAction.setEnabled(True)
            # self.quitSignInAction.setEnabled(True)
        if (q.text() == "退出"):
            if self.yanshi_flag == 2 or self.yanshi_flag == 0:
                if self.widget.flag != 0:
                    self.yanshi_flag == 0
                    self.widget.close()
            if self.yanshi_flag == 1:
                self.widget.stopThreading()
                self.yanshi_flag == 0
            qApp = QApplication.instance()
            qApp.quit()
        return

if __name__ == "__main__":
    app = QApplication(argv)
    app.setWindowIcon(QIcon("./images/MainWindow_2.png"))
    app.setStyleSheet(load_stylesheet_pyqt5())
    mainMindow = Main()
    mainMindow.show()
    mainMindow.setWindowOpacity(0.95)
    exit(app.exec_())

