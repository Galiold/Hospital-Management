# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hospital_Management.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(886, 669)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #303841;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(300, 500))
        self.frame.setStyleSheet("background-color: #11999e;\n"
                                 "border-radius: 10px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setObjectName("formLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.login = QtWidgets.QPushButton(self.frame)
        self.login.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.login.setFont(font)
        self.login.setStyleSheet("QPushButton#login\n"
                                 "{\n"
                                 "    border: 2px solid #fff;\n"
                                 "    background-color: #96dae4;\n"
                                 "    color: #fff;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover#login\n"
                                 "{\n"
                                 "    background-color: #FFF;\n"
                                 "    color: black;\n"
                                 "}")
        self.login.setObjectName("login")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.login)
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setMinimumSize(QtCore.QSize(200, 50))
        self.textEdit.setMaximumSize(QtCore.QSize(200, 50))
        self.textEdit.setStyleSheet("border: 2px solid #fff;\n"
                                    "color: #fff;\n"
                                    "")
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textEdit.setObjectName("textEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.textEdit)
        self.gridLayout_3.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 886, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.login.setText(_translate("MainWindow", "Login"))



