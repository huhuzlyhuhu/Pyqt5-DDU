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
    # 设置窗口样式(基本窗口类型)
    # #对话框窗口，有问号和关闭按钮
    # MainWindow.setWindowFlags(QtCore.Qt.Dialog)
    # #普通窗口，有最大化，最小化和关闭按钮
    # MainWindow.setWindowFlags(QtCore.Qt.Window)
    # #无边框的弹出窗口(没有关闭按钮)
    # MainWindow.setWindowFlags(QtCore.Qt.Popup)
    # #无边框的提示窗口，没有任务栏(没有关闭按钮)
    # MainWindow.setWindowFlags(QtCore.Qt.ToolTip)
    # #无边框的闪屏窗口，没有任务栏(没有关闭按钮)
    # MainWindow.setWindowFlags(QtCore.Qt.SplashScreen)
    # #子窗口，没有按钮，但有标题
    # MainWindow.setWindowFlags(QtCore.Qt.SubWindow)
    # 设置窗口样式(自定义顶层窗口外观)（不能全屏）
    # MainWindow.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
    # 无边框窗口(没有关闭按钮)
    # MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    # 有边框但无标题栏和按钮，不能移动和拖动的窗口
    # MainWindow.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    # 添加标题栏和一个关闭按钮(关闭按钮不可用)
    # MainWindow.setWindowFlags(QtCore.Qt.WindowTitleHint)
    # 添加系统目录和一个关闭按钮(关闭按钮不可用)
    # MainWindow.setWindowFlags(QtCore.Qt.WindowSystemMenuHint)
    # 激活最大化按钮
    # MainWindow.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint)
    # 激活最小化按钮
    # MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    # 激活最大化和最小化按钮
    # MainWindow.setWindowFlags(QtCore.Qt.WindowMinMaxButtonsHint)
    # 只有关闭按钮
    # MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    # 添加一个想像对话框一样的问号和关闭按钮
    # MainWindow.setWindowFlags(QtCore.Qt.WindowContextHelpButtonHint)
    # 使窗口始终处于顶层位置(无用)
    # MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    # 使窗口始终处于底层位置
    # MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnBottomHint)
    MainWindow.show()
    sys.exit(app.exec_())
