# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeatherWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(100, 70, 481, 351))
        self.groupBox.setObjectName("groupBox")
        self.resultText = QtWidgets.QTextEdit(self.groupBox)
        self.resultText.setGeometry(QtCore.QRect(60, 100, 371, 131))
        self.resultText.setObjectName("resultText")
        self.queryBtn = QtWidgets.QPushButton(self.groupBox)
        self.queryBtn.setGeometry(QtCore.QRect(80, 250, 93, 28))
        self.queryBtn.setObjectName("queryBtn")
        self.clearBtn = QtWidgets.QPushButton(self.groupBox)
        self.clearBtn.setGeometry(QtCore.QRect(280, 250, 93, 28))
        self.clearBtn.setObjectName("clearBtn")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 30, 201, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.WeathercomboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.WeathercomboBox.setObjectName("WeathercomboBox")
        self.WeathercomboBox.addItem("")
        self.WeathercomboBox.addItem("")
        self.WeathercomboBox.addItem("")
        self.WeathercomboBox.addItem("")
        self.horizontalLayout.addWidget(self.WeathercomboBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.groupBox.setTitle(_translate("MainWindow", "查询天气"))
        self.queryBtn.setText(_translate("MainWindow", "查询"))
        self.clearBtn.setText(_translate("MainWindow", "清空"))
        self.label.setText(_translate("MainWindow", "城市"))
        self.WeathercomboBox.setItemText(0, _translate("MainWindow", "北京"))
        self.WeathercomboBox.setItemText(1, _translate("MainWindow", "天津"))
        self.WeathercomboBox.setItemText(2, _translate("MainWindow", "上海"))
        self.WeathercomboBox.setItemText(3, _translate("MainWindow", "孝感"))
