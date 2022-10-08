# 设置窗口样式
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 872)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(460, 280, 424, 111))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 1, 1, 1)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.widget)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.gridLayout.addWidget(self.commandLinkButton, 2, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1140, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.commandLinkButton.setText(_translate("MainWindow", "CommandLinkButton"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 初始化窗口系统
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_MainWindow()  # 创建PyQt设计的主体窗口
    ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    # 更换图标
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("img/aqa.ico"), QtGui.QIcon.Normal)
    MainWindow.setWindowIcon(icon)
    # 更换背景颜色
    MainWindow.setStyleSheet("#MainWindow{background-color:Teal}")
    # 更换背景图片
    # MainWindow.setStyleSheet("#MainWindow{border-image:url(img/bckimg.jpeg)}")
    # MainWindow.setStyleSheet("#MainWindow{background-image:url(img/bckimg.jpeg)}")
    # QPalette设置窗口背景
    # MainWindow.setObjectName("Mainwindow")
    # palette = QtGui.QPalette()
    # palette.setColor(QtGui.QPalette.Background, Qt.red)
    # MainWindow.setPalette(palette)
    # 设置窗口透明度
    # MainWindow.setWindowOpacity(0.5)
    # 设置窗口样式
    # 对话框窗口，有问号和关闭按钮
    # MainWindow.setWindowFlags(QtCore.Qt.Dialog)
    # 普通窗口，有最大化，最小化和关闭按钮
    # MainWindow.setWindowFlags(QtCore.Qt.Window)
    # 无边框的弹出窗口(没有关闭按钮)
    # MainWindow.setWindowFlags(QtCore.Qt.Popup)
    # 无边框的提示窗口，没有任务栏(没有关闭按钮)
    # MainWindow.setWindowFlags(QtCore.Qt.ToolTip)
    # 无边框的闪屏窗口，没有任务栏(没有关闭按钮)
    # MainWindow.setWindowFlags(QtCore.Qt.SplashScreen)
    # 子窗口，没有按钮，但有标题
    # MainWindow.setWindowFlags(QtCore.Qt.SubWindow)
    MainWindow.show()
    sys.exit(app.exec_())
