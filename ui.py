# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hospital_Management.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(10, 50, 10, 45)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.user_lbl = QtWidgets.QLabel(self.frame)
        self.user_lbl.setMaximumSize(QtCore.QSize(1000000, 20))
        self.user_lbl.setStyleSheet("color: white;")
        self.user_lbl.setObjectName("user_lbl")
        self.verticalLayout_2.addWidget(self.user_lbl)
        self.username = QtWidgets.QTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMinimumSize(QtCore.QSize(200, 50))
        self.username.setMaximumSize(QtCore.QSize(10000000, 50))
        self.username.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;")
        self.username.setObjectName("username")
        self.verticalLayout_2.addWidget(self.username)
        self.pass_lbl = QtWidgets.QLabel(self.frame)
        self.pass_lbl.setMinimumSize(QtCore.QSize(10, 10))
        self.pass_lbl.setMaximumSize(QtCore.QSize(1000000, 20))
        self.pass_lbl.setStyleSheet("margin-top: 10px; margin-bottom:0; color: white; padding: 0px;")
        self.pass_lbl.setObjectName("pass_lbl")
        self.verticalLayout_2.addWidget(self.pass_lbl)
        self.password = QtWidgets.QTextEdit(self.frame)
        self.password.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMinimumSize(QtCore.QSize(200, 50))
        self.password.setMaximumSize(QtCore.QSize(100000, 50))
        self.password.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;")
        self.password.setInputMethodHints(QtCore.Qt.ImhNone)
        self.password.setObjectName("password")
        self.verticalLayout_2.addWidget(self.password, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.login_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("QPushButton#login_btn\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover#login_btn\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout_2.addWidget(self.login_btn, 0, QtCore.Qt.AlignVCenter)
        self.signup_btn = QtWidgets.QPushButton(self.frame)
        self.signup_btn.setMaximumSize(QtCore.QSize(120, 16777215))
        self.signup_btn.setStyleSheet("QPushButton\n"
"{\n"
"    color: white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    color: blue;\n"
"}")
        self.signup_btn.setObjectName("signup_btn")
        self.verticalLayout_2.addWidget(self.signup_btn, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
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
        self.user_lbl.setText(_translate("MainWindow", "Username"))
        self.pass_lbl.setText(_translate("MainWindow", "Password"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.signup_btn.setText(_translate("MainWindow", "New here? Sign up!"))

