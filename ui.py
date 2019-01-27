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
        MainWindow.resize(950, 812)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #303841;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.PageStack = QtWidgets.QStackedWidget(self.centralwidget)
        self.PageStack.setObjectName("PageStack")
        self.Login = QtWidgets.QWidget()
        self.Login.setObjectName("Login")
        self.formLayout = QtWidgets.QFormLayout(self.Login)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.frame = QtWidgets.QFrame(self.Login)
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
        self.verticalLayout_2.setSpacing(5)
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
        font = QtGui.QFont()
        font.setPointSize(15)
        self.username.setFont(font)
        self.username.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;")
        self.username.setInputMethodHints(QtCore.Qt.ImhNone)
        self.username.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.username.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.username.setTabChangesFocus(True)
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
        self.password.setTabChangesFocus(True)
        self.password.setObjectName("password")
        self.verticalLayout_2.addWidget(self.password)
        self.passwd_forgot_btn = QtWidgets.QPushButton(self.frame)
        self.passwd_forgot_btn.setStyleSheet("QPushButton\n"
"{\n"
"    color: white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    color: blue;\n"
"}")
        self.passwd_forgot_btn.setObjectName("passwd_forgot_btn")
        self.verticalLayout_2.addWidget(self.passwd_forgot_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
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
        self.verticalLayout_2.addWidget(self.login_btn)
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
        self.PageStack.addWidget(self.Login)
        self.Signup = QtWidgets.QWidget()
        self.Signup.setObjectName("Signup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Signup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.Signup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 600))
        self.frame_2.setMaximumSize(QtCore.QSize(400, 600))
        self.frame_2.setStyleSheet("background-color: #11999e;\n"
"border-radius: 10px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 10, -1, 20)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.register_lbl = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_lbl.sizePolicy().hasHeightForWidth())
        self.register_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.register_lbl.setFont(font)
        self.register_lbl.setStyleSheet("color: white;")
        self.register_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.register_lbl.setObjectName("register_lbl")
        self.verticalLayout_4.addWidget(self.register_lbl, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("padding-left:90; color: white;")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.name = QtWidgets.QTextEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setMinimumSize(QtCore.QSize(0, 0))
        self.name.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.name.setFont(font)
        self.name.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;")
        self.name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.name.setTabChangesFocus(True)
        self.name.setObjectName("name")
        self.verticalLayout_4.addWidget(self.name, 0, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setStyleSheet("padding-left:90; color: white;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.email = QtWidgets.QTextEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email.sizePolicy().hasHeightForWidth())
        self.email.setSizePolicy(sizePolicy)
        self.email.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.email.setFont(font)
        self.email.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;")
        self.email.setTabChangesFocus(True)
        self.email.setObjectName("email")
        self.verticalLayout_4.addWidget(self.email, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setStyleSheet("padding-left:90; color: white;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.phone = QtWidgets.QTextEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone.sizePolicy().hasHeightForWidth())
        self.phone.setSizePolicy(sizePolicy)
        self.phone.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.phone.setFont(font)
        self.phone.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;")
        self.phone.setTabChangesFocus(True)
        self.phone.setObjectName("phone")
        self.verticalLayout_4.addWidget(self.phone, 0, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setStyleSheet("padding-left:90; color: white;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.passwd = QtWidgets.QTextEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwd.sizePolicy().hasHeightForWidth())
        self.passwd.setSizePolicy(sizePolicy)
        self.passwd.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passwd.setFont(font)
        self.passwd.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;\n"
"text-align: right;")
        self.passwd.setTabChangesFocus(True)
        self.passwd.setObjectName("passwd")
        self.verticalLayout_4.addWidget(self.passwd, 0, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setStyleSheet("padding-left:90; color: white;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.selected_role = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selected_role.sizePolicy().hasHeightForWidth())
        self.selected_role.setSizePolicy(sizePolicy)
        self.selected_role.setMinimumSize(QtCore.QSize(200, 0))
        self.selected_role.setMaximumSize(QtCore.QSize(200, 40))
        self.selected_role.setStyleSheet("background-color: white;")
        self.selected_role.setEditable(False)
        self.selected_role.setObjectName("selected_role")
        self.selected_role.addItem("")
        self.selected_role.addItem("")
        self.selected_role.addItem("")
        self.selected_role.addItem("")
        self.selected_role.addItem("")
        self.selected_role.addItem("")
        self.selected_role.addItem("")
        self.selected_role.addItem("")
        self.verticalLayout_4.addWidget(self.selected_role, 0, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem3)
        self.submit_btn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_btn.sizePolicy().hasHeightForWidth())
        self.submit_btn.setSizePolicy(sizePolicy)
        self.submit_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.submit_btn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.submit_btn.setFont(font)
        self.submit_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.submit_btn.setStyleSheet("QPushButton\n"
"{                  \n"
"    border: 2px solid #fff;\\n\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: #FFF;\n"
"color: black;\n"
"}")
        self.submit_btn.setObjectName("submit_btn")
        self.verticalLayout_4.addWidget(self.submit_btn, 0, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem4)
        self.register_back_btn = QtWidgets.QPushButton(self.frame_2)
        self.register_back_btn.setStyleSheet("QPushButton{color:white;}\n"
"QPushButton:hover{color: blue;}")
        self.register_back_btn.setObjectName("register_back_btn")
        self.verticalLayout_4.addWidget(self.register_back_btn)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.PageStack.addWidget(self.Signup)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(900, 700))
        self.frame_3.setStyleSheet("background-color: #11999e;\n"
"border-radius: 10px")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.AdminPanel = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AdminPanel.setFont(font)
        self.AdminPanel.setStyleSheet("color: white;")
        self.AdminPanel.setObjectName("AdminPanel")
        self.verticalLayout_7.addWidget(self.AdminPanel, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(650, 650))
        self.tableWidget.setStyleSheet("background-color: white;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, 50, -1, 50)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.approve_user_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.approve_user_btn.sizePolicy().hasHeightForWidth())
        self.approve_user_btn.setSizePolicy(sizePolicy)
        self.approve_user_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.approve_user_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.approve_user_btn.setObjectName("approve_user_btn")
        self.verticalLayout_8.addWidget(self.approve_user_btn, 0, QtCore.Qt.AlignHCenter)
        self.delete_user_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_user_btn.sizePolicy().hasHeightForWidth())
        self.delete_user_btn.setSizePolicy(sizePolicy)
        self.delete_user_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.delete_user_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.delete_user_btn.setObjectName("delete_user_btn")
        self.verticalLayout_8.addWidget(self.delete_user_btn, 0, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.add_user_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_user_btn.sizePolicy().hasHeightForWidth())
        self.add_user_btn.setSizePolicy(sizePolicy)
        self.add_user_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.add_user_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.add_user_btn.setObjectName("add_user_btn")
        self.verticalLayout_8.addWidget(self.add_user_btn, 0, QtCore.Qt.AlignHCenter)
        self.admin_exit_btn = QtWidgets.QPushButton(self.frame_3)
        self.admin_exit_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.admin_exit_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.admin_exit_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.admin_exit_btn.setObjectName("admin_exit_btn")
        self.verticalLayout_8.addWidget(self.admin_exit_btn, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout.addWidget(self.frame_3)
        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.PageStack.addWidget(self.page)
        self.Recover_Password_Page = QtWidgets.QWidget()
        self.Recover_Password_Page.setObjectName("Recover_Password_Page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.Recover_Password_Page)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.Recover_Password_Page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(300, 200))
        self.frame_4.setStyleSheet("background-color: #11999e;\n"
"border-radius: 10px")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(200, 0))
        self.label_7.setStyleSheet("color: white;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.recovery_email = QtWidgets.QTextEdit(self.frame_4)
        self.recovery_email.setMinimumSize(QtCore.QSize(200, 50))
        self.recovery_email.setMaximumSize(QtCore.QSize(200, 50))
        self.recovery_email.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;")
        self.recovery_email.setObjectName("recovery_email")
        self.verticalLayout_5.addWidget(self.recovery_email, 0, QtCore.Qt.AlignHCenter)
        self.recovery_submit_btn = QtWidgets.QPushButton(self.frame_4)
        self.recovery_submit_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.recovery_submit_btn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.recovery_submit_btn.setFont(font)
        self.recovery_submit_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.recovery_submit_btn.setObjectName("recovery_submit_btn")
        self.verticalLayout_5.addWidget(self.recovery_submit_btn, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.gridLayout_6.addWidget(self.frame_4, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.PageStack.addWidget(self.Recover_Password_Page)
        self.Reception_Page = QtWidgets.QWidget()
        self.Reception_Page.setObjectName("Reception_Page")
        self.reception_table = QtWidgets.QTableWidget(self.Reception_Page)
        self.reception_table.setGeometry(QtCore.QRect(40, 100, 600, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reception_table.sizePolicy().hasHeightForWidth())
        self.reception_table.setSizePolicy(sizePolicy)
        self.reception_table.setMinimumSize(QtCore.QSize(600, 500))
        self.reception_table.setSizeIncrement(QtCore.QSize(600, 500))
        self.reception_table.setStyleSheet("background-color: white;")
        self.reception_table.setObjectName("reception_table")
        self.reception_table.setColumnCount(0)
        self.reception_table.setRowCount(0)
        self.delete_freetime_btn = QtWidgets.QPushButton(self.Reception_Page)
        self.delete_freetime_btn.setGeometry(QtCore.QRect(720, 180, 171, 51))
        self.delete_freetime_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.delete_freetime_btn.setObjectName("delete_freetime_btn")
        self.add_freetime_btn = QtWidgets.QPushButton(self.Reception_Page)
        self.add_freetime_btn.setGeometry(QtCore.QRect(710, 320, 181, 51))
        self.add_freetime_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.add_freetime_btn.setObjectName("add_freetime_btn")
        self.clear_time_btn = QtWidgets.QPushButton(self.Reception_Page)
        self.clear_time_btn.setGeometry(QtCore.QRect(710, 250, 181, 51))
        self.clear_time_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.clear_time_btn.setObjectName("clear_time_btn")
        self.reception_edit_info_btn = QtWidgets.QPushButton(self.Reception_Page)
        self.reception_edit_info_btn.setGeometry(QtCore.QRect(700, 400, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reception_edit_info_btn.sizePolicy().hasHeightForWidth())
        self.reception_edit_info_btn.setSizePolicy(sizePolicy)
        self.reception_edit_info_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.reception_edit_info_btn.setFont(font)
        self.reception_edit_info_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.reception_edit_info_btn.setObjectName("reception_edit_info_btn")
        self.reception_exit_btn = QtWidgets.QPushButton(self.Reception_Page)
        self.reception_exit_btn.setGeometry(QtCore.QRect(700, 470, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reception_exit_btn.sizePolicy().hasHeightForWidth())
        self.reception_exit_btn.setSizePolicy(sizePolicy)
        self.reception_exit_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.reception_exit_btn.setFont(font)
        self.reception_exit_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.reception_exit_btn.setObjectName("reception_exit_btn")
        self.PageStack.addWidget(self.Reception_Page)
        self.Pharmacy_Page = QtWidgets.QWidget()
        self.Pharmacy_Page.setObjectName("Pharmacy_Page")
        self.addDrug_btn = QtWidgets.QPushButton(self.Pharmacy_Page)
        self.addDrug_btn.setGeometry(QtCore.QRect(650, 130, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addDrug_btn.sizePolicy().hasHeightForWidth())
        self.addDrug_btn.setSizePolicy(sizePolicy)
        self.addDrug_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.addDrug_btn.setFont(font)
        self.addDrug_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.addDrug_btn.setObjectName("addDrug_btn")
        self.deleteDrug_btn = QtWidgets.QPushButton(self.Pharmacy_Page)
        self.deleteDrug_btn.setGeometry(QtCore.QRect(650, 210, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteDrug_btn.sizePolicy().hasHeightForWidth())
        self.deleteDrug_btn.setSizePolicy(sizePolicy)
        self.deleteDrug_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.deleteDrug_btn.setFont(font)
        self.deleteDrug_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.deleteDrug_btn.setObjectName("deleteDrug_btn")
        self.filterDrug_btn = QtWidgets.QPushButton(self.Pharmacy_Page)
        self.filterDrug_btn.setGeometry(QtCore.QRect(650, 280, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterDrug_btn.sizePolicy().hasHeightForWidth())
        self.filterDrug_btn.setSizePolicy(sizePolicy)
        self.filterDrug_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.filterDrug_btn.setFont(font)
        self.filterDrug_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.filterDrug_btn.setObjectName("filterDrug_btn")
        self.pPresc_btn = QtWidgets.QPushButton(self.Pharmacy_Page)
        self.pPresc_btn.setGeometry(QtCore.QRect(650, 360, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pPresc_btn.sizePolicy().hasHeightForWidth())
        self.pPresc_btn.setSizePolicy(sizePolicy)
        self.pPresc_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pPresc_btn.setFont(font)
        self.pPresc_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.pPresc_btn.setObjectName("pPresc_btn")
        self.drugs_table = QtWidgets.QTableWidget(self.Pharmacy_Page)
        self.drugs_table.setGeometry(QtCore.QRect(20, 120, 600, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drugs_table.sizePolicy().hasHeightForWidth())
        self.drugs_table.setSizePolicy(sizePolicy)
        self.drugs_table.setMinimumSize(QtCore.QSize(600, 500))
        self.drugs_table.setSizeIncrement(QtCore.QSize(600, 500))
        self.drugs_table.setStyleSheet("background-color: white;")
        self.drugs_table.setObjectName("drugs_table")
        self.drugs_table.setColumnCount(0)
        self.drugs_table.setRowCount(0)
        self.pharmacy_edit_info_btn = QtWidgets.QPushButton(self.Pharmacy_Page)
        self.pharmacy_edit_info_btn.setGeometry(QtCore.QRect(680, 440, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pharmacy_edit_info_btn.sizePolicy().hasHeightForWidth())
        self.pharmacy_edit_info_btn.setSizePolicy(sizePolicy)
        self.pharmacy_edit_info_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pharmacy_edit_info_btn.setFont(font)
        self.pharmacy_edit_info_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.pharmacy_edit_info_btn.setObjectName("pharmacy_edit_info_btn")
        self.phar_exit_btn = QtWidgets.QPushButton(self.Pharmacy_Page)
        self.phar_exit_btn.setGeometry(QtCore.QRect(680, 520, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phar_exit_btn.sizePolicy().hasHeightForWidth())
        self.phar_exit_btn.setSizePolicy(sizePolicy)
        self.phar_exit_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.phar_exit_btn.setFont(font)
        self.phar_exit_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.phar_exit_btn.setObjectName("phar_exit_btn")
        self.PageStack.addWidget(self.Pharmacy_Page)
        self.Dr_Page = QtWidgets.QWidget()
        self.Dr_Page.setObjectName("Dr_Page")
        self.dr_approve_btn = QtWidgets.QPushButton(self.Dr_Page)
        self.dr_approve_btn.setGeometry(QtCore.QRect(650, 20, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dr_approve_btn.sizePolicy().hasHeightForWidth())
        self.dr_approve_btn.setSizePolicy(sizePolicy)
        self.dr_approve_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.dr_approve_btn.setFont(font)
        self.dr_approve_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.dr_approve_btn.setObjectName("dr_approve_btn")
        self.dr_delete_btn = QtWidgets.QPushButton(self.Dr_Page)
        self.dr_delete_btn.setGeometry(QtCore.QRect(650, 80, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dr_delete_btn.sizePolicy().hasHeightForWidth())
        self.dr_delete_btn.setSizePolicy(sizePolicy)
        self.dr_delete_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.dr_delete_btn.setFont(font)
        self.dr_delete_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.dr_delete_btn.setObjectName("dr_delete_btn")
        self.drug_history_btn = QtWidgets.QPushButton(self.Dr_Page)
        self.drug_history_btn.setGeometry(QtCore.QRect(650, 330, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drug_history_btn.sizePolicy().hasHeightForWidth())
        self.drug_history_btn.setSizePolicy(sizePolicy)
        self.drug_history_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.drug_history_btn.setFont(font)
        self.drug_history_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.drug_history_btn.setObjectName("drug_history_btn")
        self.dr_sendmessage_btn = QtWidgets.QPushButton(self.Dr_Page)
        self.dr_sendmessage_btn.setGeometry(QtCore.QRect(650, 540, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dr_sendmessage_btn.sizePolicy().hasHeightForWidth())
        self.dr_sendmessage_btn.setSizePolicy(sizePolicy)
        self.dr_sendmessage_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.dr_sendmessage_btn.setFont(font)
        self.dr_sendmessage_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.dr_sendmessage_btn.setObjectName("dr_sendmessage_btn")
        self.dr_appmnts_table = QtWidgets.QTableWidget(self.Dr_Page)
        self.dr_appmnts_table.setGeometry(QtCore.QRect(20, 110, 600, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dr_appmnts_table.sizePolicy().hasHeightForWidth())
        self.dr_appmnts_table.setSizePolicy(sizePolicy)
        self.dr_appmnts_table.setMinimumSize(QtCore.QSize(600, 500))
        self.dr_appmnts_table.setMaximumSize(QtCore.QSize(600, 500))
        self.dr_appmnts_table.setStyleSheet("background-color: white;")
        self.dr_appmnts_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dr_appmnts_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.dr_appmnts_table.setAlternatingRowColors(True)
        self.dr_appmnts_table.setObjectName("dr_appmnts_table")
        self.dr_appmnts_table.setColumnCount(5)
        self.dr_appmnts_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.dr_appmnts_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dr_appmnts_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dr_appmnts_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dr_appmnts_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dr_appmnts_table.setHorizontalHeaderItem(4, item)
        self.dr_appmnts_table.horizontalHeader().setCascadingSectionResizes(True)
        self.dr_appmnts_table.horizontalHeader().setDefaultSectionSize(120)
        self.dr_appmnts_table.horizontalHeader().setMinimumSectionSize(30)
        self.dr_appmnts_table.horizontalHeader().setSortIndicatorShown(True)
        self.dr_appmnts_table.horizontalHeader().setStretchLastSection(True)
        self.dr_appmnts_table.verticalHeader().setVisible(False)
        self.dr_appmnts_table.verticalHeader().setStretchLastSection(False)
        self.dr_exit_btn = QtWidgets.QPushButton(self.Dr_Page)
        self.dr_exit_btn.setGeometry(QtCore.QRect(650, 660, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dr_exit_btn.sizePolicy().hasHeightForWidth())
        self.dr_exit_btn.setSizePolicy(sizePolicy)
        self.dr_exit_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.dr_exit_btn.setFont(font)
        self.dr_exit_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.dr_exit_btn.setObjectName("dr_exit_btn")
        self.dr_addfree_btn = QtWidgets.QPushButton(self.Dr_Page)
        self.dr_addfree_btn.setGeometry(QtCore.QRect(650, 140, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dr_addfree_btn.sizePolicy().hasHeightForWidth())
        self.dr_addfree_btn.setSizePolicy(sizePolicy)
        self.dr_addfree_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.dr_addfree_btn.setFont(font)
        self.dr_addfree_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.dr_addfree_btn.setObjectName("dr_addfree_btn")
        self.dr_delfree_btn = QtWidgets.QPushButton(self.Dr_Page)
        self.dr_delfree_btn.setGeometry(QtCore.QRect(650, 200, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dr_delfree_btn.sizePolicy().hasHeightForWidth())
        self.dr_delfree_btn.setSizePolicy(sizePolicy)
        self.dr_delfree_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.dr_delfree_btn.setFont(font)
        self.dr_delfree_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.dr_delfree_btn.setObjectName("dr_delfree_btn")
        self.pre_drug_btn = QtWidgets.QPushButton(self.Dr_Page)
        self.pre_drug_btn.setGeometry(QtCore.QRect(650, 270, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pre_drug_btn.sizePolicy().hasHeightForWidth())
        self.pre_drug_btn.setSizePolicy(sizePolicy)
        self.pre_drug_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pre_drug_btn.setFont(font)
        self.pre_drug_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.pre_drug_btn.setObjectName("pre_drug_btn")
        self.pre_test_btn = QtWidgets.QPushButton(self.Dr_Page)
        self.pre_test_btn.setGeometry(QtCore.QRect(650, 400, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pre_test_btn.sizePolicy().hasHeightForWidth())
        self.pre_test_btn.setSizePolicy(sizePolicy)
        self.pre_test_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pre_test_btn.setFont(font)
        self.pre_test_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.pre_test_btn.setObjectName("pre_test_btn")
        self.dr_emergency_btn = QtWidgets.QPushButton(self.Dr_Page)
        self.dr_emergency_btn.setGeometry(QtCore.QRect(650, 600, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dr_emergency_btn.sizePolicy().hasHeightForWidth())
        self.dr_emergency_btn.setSizePolicy(sizePolicy)
        self.dr_emergency_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.dr_emergency_btn.setFont(font)
        self.dr_emergency_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.dr_emergency_btn.setObjectName("dr_emergency_btn")
        self.pre_test_btn_2 = QtWidgets.QPushButton(self.Dr_Page)
        self.pre_test_btn_2.setGeometry(QtCore.QRect(650, 460, 256, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pre_test_btn_2.sizePolicy().hasHeightForWidth())
        self.pre_test_btn_2.setSizePolicy(sizePolicy)
        self.pre_test_btn_2.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pre_test_btn_2.setFont(font)
        self.pre_test_btn_2.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.pre_test_btn_2.setObjectName("pre_test_btn_2")
        self.dr_edit_info_btn = QtWidgets.QPushButton(self.Dr_Page)
        self.dr_edit_info_btn.setGeometry(QtCore.QRect(210, 650, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dr_edit_info_btn.sizePolicy().hasHeightForWidth())
        self.dr_edit_info_btn.setSizePolicy(sizePolicy)
        self.dr_edit_info_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.dr_edit_info_btn.setFont(font)
        self.dr_edit_info_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.dr_edit_info_btn.setObjectName("dr_edit_info_btn")
        self.PageStack.addWidget(self.Dr_Page)
        self.Messages = QtWidgets.QWidget()
        self.Messages.setObjectName("Messages")
        self.messsage_txt = QtWidgets.QTextEdit(self.Messages)
        self.messsage_txt.setGeometry(QtCore.QRect(140, 520, 371, 171))
        self.messsage_txt.setStyleSheet("background-color: white; color: black;")
        self.messsage_txt.setObjectName("messsage_txt")
        self.sendmessage_btn = QtWidgets.QPushButton(self.Messages)
        self.sendmessage_btn.setGeometry(QtCore.QRect(530, 580, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendmessage_btn.sizePolicy().hasHeightForWidth())
        self.sendmessage_btn.setSizePolicy(sizePolicy)
        self.sendmessage_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.sendmessage_btn.setFont(font)
        self.sendmessage_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.sendmessage_btn.setObjectName("sendmessage_btn")
        self.message_table = QtWidgets.QTableWidget(self.Messages)
        self.message_table.setGeometry(QtCore.QRect(140, 10, 600, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_table.sizePolicy().hasHeightForWidth())
        self.message_table.setSizePolicy(sizePolicy)
        self.message_table.setMinimumSize(QtCore.QSize(600, 500))
        self.message_table.setMaximumSize(QtCore.QSize(600, 500))
        self.message_table.setStyleSheet("background-color: white;")
        self.message_table.setObjectName("message_table")
        self.message_table.setColumnCount(4)
        self.message_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.message_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.message_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.message_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.message_table.setHorizontalHeaderItem(3, item)
        self.message_table.horizontalHeader().setDefaultSectionSize(149)
        self.message_table.horizontalHeader().setMinimumSectionSize(50)
        self.message_table.horizontalHeader().setStretchLastSection(True)
        self.receiverid_txt = QtWidgets.QTextEdit(self.Messages)
        self.receiverid_txt.setGeometry(QtCore.QRect(530, 520, 201, 51))
        self.receiverid_txt.setStyleSheet("background-color: white; color: black;")
        self.receiverid_txt.setObjectName("receiverid_txt")
        self.msg_back_btn = QtWidgets.QPushButton(self.Messages)
        self.msg_back_btn.setGeometry(QtCore.QRect(530, 640, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg_back_btn.sizePolicy().hasHeightForWidth())
        self.msg_back_btn.setSizePolicy(sizePolicy)
        self.msg_back_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.msg_back_btn.setFont(font)
        self.msg_back_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.msg_back_btn.setObjectName("msg_back_btn")
        self.PageStack.addWidget(self.Messages)
        self.PatientPage = QtWidgets.QWidget()
        self.PatientPage.setObjectName("PatientPage")
        self.Patient_ReserveAppointment = QtWidgets.QPushButton(self.PatientPage)
        self.Patient_ReserveAppointment.setGeometry(QtCore.QRect(670, 120, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Patient_ReserveAppointment.sizePolicy().hasHeightForWidth())
        self.Patient_ReserveAppointment.setSizePolicy(sizePolicy)
        self.Patient_ReserveAppointment.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.Patient_ReserveAppointment.setFont(font)
        self.Patient_ReserveAppointment.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.Patient_ReserveAppointment.setObjectName("Patient_ReserveAppointment")
        self.P_ShowPrescription = QtWidgets.QPushButton(self.PatientPage)
        self.P_ShowPrescription.setGeometry(QtCore.QRect(670, 190, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P_ShowPrescription.sizePolicy().hasHeightForWidth())
        self.P_ShowPrescription.setSizePolicy(sizePolicy)
        self.P_ShowPrescription.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.P_ShowPrescription.setFont(font)
        self.P_ShowPrescription.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.P_ShowPrescription.setObjectName("P_ShowPrescription")
        self.P_SendMessage = QtWidgets.QPushButton(self.PatientPage)
        self.P_SendMessage.setGeometry(QtCore.QRect(670, 290, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P_SendMessage.sizePolicy().hasHeightForWidth())
        self.P_SendMessage.setSizePolicy(sizePolicy)
        self.P_SendMessage.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.P_SendMessage.setFont(font)
        self.P_SendMessage.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.P_SendMessage.setObjectName("P_SendMessage")
        self.P_Exit = QtWidgets.QPushButton(self.PatientPage)
        self.P_Exit.setGeometry(QtCore.QRect(670, 510, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P_Exit.sizePolicy().hasHeightForWidth())
        self.P_Exit.setSizePolicy(sizePolicy)
        self.P_Exit.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.P_Exit.setFont(font)
        self.P_Exit.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.P_Exit.setObjectName("P_Exit")
        self.P_AppointmentsTable = QtWidgets.QTableWidget(self.PatientPage)
        self.P_AppointmentsTable.setGeometry(QtCore.QRect(40, 80, 600, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P_AppointmentsTable.sizePolicy().hasHeightForWidth())
        self.P_AppointmentsTable.setSizePolicy(sizePolicy)
        self.P_AppointmentsTable.setMinimumSize(QtCore.QSize(600, 500))
        self.P_AppointmentsTable.setMaximumSize(QtCore.QSize(600, 500))
        self.P_AppointmentsTable.setStyleSheet("background-color: white;")
        self.P_AppointmentsTable.setAlternatingRowColors(True)
        self.P_AppointmentsTable.setObjectName("P_AppointmentsTable")
        self.P_AppointmentsTable.setColumnCount(5)
        self.P_AppointmentsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.P_AppointmentsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.P_AppointmentsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.P_AppointmentsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.P_AppointmentsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.P_AppointmentsTable.setHorizontalHeaderItem(4, item)
        self.P_AppointmentsTable.horizontalHeader().setDefaultSectionSize(120)
        self.P_AppointmentsTable.horizontalHeader().setSortIndicatorShown(True)
        self.P_AppointmentsTable.verticalHeader().setVisible(False)
        self.P_ShowBedInfo = QtWidgets.QPushButton(self.PatientPage)
        self.P_ShowBedInfo.setEnabled(True)
        self.P_ShowBedInfo.setGeometry(QtCore.QRect(670, 360, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P_ShowBedInfo.sizePolicy().hasHeightForWidth())
        self.P_ShowBedInfo.setSizePolicy(sizePolicy)
        self.P_ShowBedInfo.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.P_ShowBedInfo.setFont(font)
        self.P_ShowBedInfo.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.P_ShowBedInfo.setObjectName("P_ShowBedInfo")
        self.patient_edit_info_btn_2 = QtWidgets.QPushButton(self.PatientPage)
        self.patient_edit_info_btn_2.setGeometry(QtCore.QRect(670, 440, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patient_edit_info_btn_2.sizePolicy().hasHeightForWidth())
        self.patient_edit_info_btn_2.setSizePolicy(sizePolicy)
        self.patient_edit_info_btn_2.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.patient_edit_info_btn_2.setFont(font)
        self.patient_edit_info_btn_2.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.patient_edit_info_btn_2.setObjectName("patient_edit_info_btn_2")
        self.PageStack.addWidget(self.PatientPage)
        self.LabPage = QtWidgets.QWidget()
        self.LabPage.setObjectName("LabPage")
        self.Lab_Table = QtWidgets.QTableWidget(self.LabPage)
        self.Lab_Table.setGeometry(QtCore.QRect(50, 60, 600, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lab_Table.sizePolicy().hasHeightForWidth())
        self.Lab_Table.setSizePolicy(sizePolicy)
        self.Lab_Table.setMinimumSize(QtCore.QSize(600, 500))
        self.Lab_Table.setMaximumSize(QtCore.QSize(600, 500))
        self.Lab_Table.setStyleSheet("background-color: white;")
        self.Lab_Table.setAlternatingRowColors(True)
        self.Lab_Table.setObjectName("Lab_Table")
        self.Lab_Table.setColumnCount(4)
        self.Lab_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Lab_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Lab_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Lab_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Lab_Table.setHorizontalHeaderItem(3, item)
        self.Lab_Table.horizontalHeader().setCascadingSectionResizes(False)
        self.Lab_Table.horizontalHeader().setDefaultSectionSize(149)
        self.Lab_Table.horizontalHeader().setSortIndicatorShown(True)
        self.Lab_Table.horizontalHeader().setStretchLastSection(True)
        self.Lab_Table.verticalHeader().setVisible(False)
        self.lab_send_result_btn = QtWidgets.QPushButton(self.LabPage)
        self.lab_send_result_btn.setGeometry(QtCore.QRect(680, 170, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_send_result_btn.sizePolicy().hasHeightForWidth())
        self.lab_send_result_btn.setSizePolicy(sizePolicy)
        self.lab_send_result_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lab_send_result_btn.setFont(font)
        self.lab_send_result_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.lab_send_result_btn.setObjectName("lab_send_result_btn")
        self.lab_exit_btn = QtWidgets.QPushButton(self.LabPage)
        self.lab_exit_btn.setGeometry(QtCore.QRect(680, 430, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_exit_btn.sizePolicy().hasHeightForWidth())
        self.lab_exit_btn.setSizePolicy(sizePolicy)
        self.lab_exit_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lab_exit_btn.setFont(font)
        self.lab_exit_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.lab_exit_btn.setObjectName("lab_exit_btn")
        self.lab_edit_info_btn_2 = QtWidgets.QPushButton(self.LabPage)
        self.lab_edit_info_btn_2.setGeometry(QtCore.QRect(680, 300, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_edit_info_btn_2.sizePolicy().hasHeightForWidth())
        self.lab_edit_info_btn_2.setSizePolicy(sizePolicy)
        self.lab_edit_info_btn_2.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lab_edit_info_btn_2.setFont(font)
        self.lab_edit_info_btn_2.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.lab_edit_info_btn_2.setObjectName("lab_edit_info_btn_2")
        self.PageStack.addWidget(self.LabPage)
        self.Complete_Info_Page = QtWidgets.QWidget()
        self.Complete_Info_Page.setObjectName("Complete_Info_Page")
        self.gridLayout = QtWidgets.QGridLayout(self.Complete_Info_Page)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_5 = QtWidgets.QFrame(self.Complete_Info_Page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(300, 600))
        self.frame_5.setSizeIncrement(QtCore.QSize(200, 500))
        self.frame_5.setStyleSheet("background-color: #11999e;\n"
"border-radius: 10px")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.edit_dob = QtWidgets.QTextEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_dob.sizePolicy().hasHeightForWidth())
        self.edit_dob.setSizePolicy(sizePolicy)
        self.edit_dob.setMinimumSize(QtCore.QSize(200, 50))
        self.edit_dob.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edit_dob.setFont(font)
        self.edit_dob.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;")
        self.edit_dob.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edit_dob.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.edit_dob.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.edit_dob.setTabChangesFocus(True)
        self.edit_dob.setObjectName("edit_dob")
        self.verticalLayout_12.addWidget(self.edit_dob, 0, QtCore.Qt.AlignHCenter)
        self.edit_address = QtWidgets.QTextEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_address.sizePolicy().hasHeightForWidth())
        self.edit_address.setSizePolicy(sizePolicy)
        self.edit_address.setMinimumSize(QtCore.QSize(200, 50))
        self.edit_address.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edit_address.setFont(font)
        self.edit_address.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;")
        self.edit_address.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edit_address.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.edit_address.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.edit_address.setTabChangesFocus(True)
        self.edit_address.setObjectName("edit_address")
        self.verticalLayout_12.addWidget(self.edit_address, 0, QtCore.Qt.AlignHCenter)
        self.edit_zipcode = QtWidgets.QTextEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_zipcode.sizePolicy().hasHeightForWidth())
        self.edit_zipcode.setSizePolicy(sizePolicy)
        self.edit_zipcode.setMinimumSize(QtCore.QSize(200, 50))
        self.edit_zipcode.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edit_zipcode.setFont(font)
        self.edit_zipcode.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;")
        self.edit_zipcode.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edit_zipcode.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.edit_zipcode.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.edit_zipcode.setTabChangesFocus(True)
        self.edit_zipcode.setObjectName("edit_zipcode")
        self.verticalLayout_12.addWidget(self.edit_zipcode, 0, QtCore.Qt.AlignHCenter)
        self.edit_sex = QtWidgets.QTextEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_sex.sizePolicy().hasHeightForWidth())
        self.edit_sex.setSizePolicy(sizePolicy)
        self.edit_sex.setMinimumSize(QtCore.QSize(200, 50))
        self.edit_sex.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edit_sex.setFont(font)
        self.edit_sex.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;")
        self.edit_sex.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edit_sex.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.edit_sex.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.edit_sex.setTabChangesFocus(True)
        self.edit_sex.setObjectName("edit_sex")
        self.verticalLayout_12.addWidget(self.edit_sex, 0, QtCore.Qt.AlignHCenter)
        self.edit_height = QtWidgets.QTextEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_height.sizePolicy().hasHeightForWidth())
        self.edit_height.setSizePolicy(sizePolicy)
        self.edit_height.setMinimumSize(QtCore.QSize(200, 50))
        self.edit_height.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edit_height.setFont(font)
        self.edit_height.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;")
        self.edit_height.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edit_height.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.edit_height.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.edit_height.setTabChangesFocus(True)
        self.edit_height.setObjectName("edit_height")
        self.verticalLayout_12.addWidget(self.edit_height, 0, QtCore.Qt.AlignHCenter)
        self.edit_weight = QtWidgets.QTextEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_weight.sizePolicy().hasHeightForWidth())
        self.edit_weight.setSizePolicy(sizePolicy)
        self.edit_weight.setMinimumSize(QtCore.QSize(200, 50))
        self.edit_weight.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edit_weight.setFont(font)
        self.edit_weight.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;")
        self.edit_weight.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edit_weight.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.edit_weight.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.edit_weight.setTabChangesFocus(True)
        self.edit_weight.setObjectName("edit_weight")
        self.verticalLayout_12.addWidget(self.edit_weight, 0, QtCore.Qt.AlignHCenter)
        self.update_info_btn = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_info_btn.sizePolicy().hasHeightForWidth())
        self.update_info_btn.setSizePolicy(sizePolicy)
        self.update_info_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.update_info_btn.setFont(font)
        self.update_info_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 2px solid #fff;\n"
"    background-color: #96dae4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"}")
        self.update_info_btn.setObjectName("update_info_btn")
        self.verticalLayout_12.addWidget(self.update_info_btn, 0, QtCore.Qt.AlignHCenter)
        self.back_btn = QtWidgets.QPushButton(self.frame_5)
        self.back_btn.setStyleSheet("QPushButton{color:white;}\n"
"QPushButton:hover{color: blue;}")
        self.back_btn.setObjectName("back_btn")
        self.verticalLayout_12.addWidget(self.back_btn)
        self.verticalLayout_11.addLayout(self.verticalLayout_12)
        self.gridLayout_8.addWidget(self.frame_5, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 2, 0, 1, 1)
        self.PageStack.addWidget(self.Complete_Info_Page)
        self.gridLayout_9.addWidget(self.PageStack, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.PageStack.setCurrentIndex(7)
        self.selected_role.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.user_lbl.setText(_translate("MainWindow", "Username"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.pass_lbl.setText(_translate("MainWindow", "Password"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.passwd_forgot_btn.setText(_translate("MainWindow", "Forgot Password?"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.signup_btn.setText(_translate("MainWindow", "New here? Sign up!"))
        self.register_lbl.setText(_translate("MainWindow", "Register"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "E-Mail"))
        self.label_3.setText(_translate("MainWindow", "Phone Number"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.label_6.setText(_translate("MainWindow", "Role"))
        self.selected_role.setItemText(0, _translate("MainWindow", "Select role"))
        self.selected_role.setItemText(1, _translate("MainWindow", "Doctor"))
        self.selected_role.setItemText(2, _translate("MainWindow", "Nurse"))
        self.selected_role.setItemText(3, _translate("MainWindow", "Patient"))
        self.selected_role.setItemText(4, _translate("MainWindow", "Pharmacist"))
        self.selected_role.setItemText(5, _translate("MainWindow", "Accountant"))
        self.selected_role.setItemText(6, _translate("MainWindow", "Reception"))
        self.selected_role.setItemText(7, _translate("MainWindow", "Laboratory"))
        self.submit_btn.setText(_translate("MainWindow", "Submit"))
        self.register_back_btn.setText(_translate("MainWindow", "Back"))
        self.AdminPanel.setText(_translate("MainWindow", "Adminstration Panel"))
        self.approve_user_btn.setText(_translate("MainWindow", "Approve User"))
        self.delete_user_btn.setText(_translate("MainWindow", "Delete User"))
        self.add_user_btn.setText(_translate("MainWindow", "Add New User"))
        self.admin_exit_btn.setText(_translate("MainWindow", "Exit"))
        self.label_7.setText(_translate("MainWindow", "Enter your email here, we will send you a new password."))
        self.recovery_submit_btn.setText(_translate("MainWindow", "Submit"))
        self.delete_freetime_btn.setText(_translate("MainWindow", "Delete Free Time"))
        self.add_freetime_btn.setText(_translate("MainWindow", "Add Free Time"))
        self.clear_time_btn.setText(_translate("MainWindow", "Delete Appointment"))
        self.reception_edit_info_btn.setText(_translate("MainWindow", "Edit Info"))
        self.reception_exit_btn.setText(_translate("MainWindow", "Exit"))
        self.addDrug_btn.setText(_translate("MainWindow", "Add"))
        self.deleteDrug_btn.setText(_translate("MainWindow", "Delete"))
        self.filterDrug_btn.setText(_translate("MainWindow", "Filter"))
        self.pPresc_btn.setText(_translate("MainWindow", "Process Prescription"))
        self.pharmacy_edit_info_btn.setText(_translate("MainWindow", "Edit Info"))
        self.phar_exit_btn.setText(_translate("MainWindow", "Exit"))
        self.dr_approve_btn.setText(_translate("MainWindow", "Approve Appointment"))
        self.dr_delete_btn.setText(_translate("MainWindow", "Delete Appointment"))
        self.drug_history_btn.setText(_translate("MainWindow", "Patient Drug Usage History"))
        self.dr_sendmessage_btn.setText(_translate("MainWindow", "Send Private Message"))
        self.dr_appmnts_table.setSortingEnabled(True)
        item = self.dr_appmnts_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Appointment ID"))
        item = self.dr_appmnts_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PatientID"))
        item = self.dr_appmnts_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time"))
        item = self.dr_appmnts_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dr ID"))
        item = self.dr_appmnts_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        self.dr_exit_btn.setText(_translate("MainWindow", "Exit"))
        self.dr_addfree_btn.setText(_translate("MainWindow", "Add Free Time"))
        self.dr_delfree_btn.setText(_translate("MainWindow", "Delete Time"))
        self.pre_drug_btn.setText(_translate("MainWindow", "Prescribe Drug"))
        self.pre_test_btn.setText(_translate("MainWindow", "Prescribe Test"))
        self.dr_emergency_btn.setText(_translate("MainWindow", "Emergency Situation"))
        self.pre_test_btn_2.setText(_translate("MainWindow", "Show Test Result"))
        self.dr_edit_info_btn.setText(_translate("MainWindow", "Edit Info"))
        self.messsage_txt.setPlaceholderText(_translate("MainWindow", "Message"))
        self.sendmessage_btn.setText(_translate("MainWindow", "Send"))
        item = self.message_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sender ID"))
        item = self.message_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Receiver ID"))
        item = self.message_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Text"))
        item = self.message_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date"))
        self.receiverid_txt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p></body></html>"))
        self.receiverid_txt.setPlaceholderText(_translate("MainWindow", "Reciever ID"))
        self.msg_back_btn.setText(_translate("MainWindow", "Back"))
        self.Patient_ReserveAppointment.setText(_translate("MainWindow", "Reserve Appointment"))
        self.P_ShowPrescription.setText(_translate("MainWindow", "Show Prescription"))
        self.P_SendMessage.setText(_translate("MainWindow", "Send Message"))
        self.P_Exit.setText(_translate("MainWindow", "Exit"))
        item = self.P_AppointmentsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Appointment ID"))
        item = self.P_AppointmentsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Patient ID"))
        item = self.P_AppointmentsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time"))
        item = self.P_AppointmentsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dr ID"))
        item = self.P_AppointmentsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        self.P_ShowBedInfo.setText(_translate("MainWindow", "Show Bed Status"))
        self.patient_edit_info_btn_2.setText(_translate("MainWindow", "Edit Info"))
        item = self.Lab_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Test ID"))
        item = self.Lab_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Dr ID"))
        item = self.Lab_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Patient ID"))
        item = self.Lab_Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Result"))
        self.lab_send_result_btn.setText(_translate("MainWindow", "Set Diagnose Report"))
        self.lab_exit_btn.setText(_translate("MainWindow", "Exit"))
        self.lab_edit_info_btn_2.setText(_translate("MainWindow", "Edit Info"))
        self.label_5.setText(_translate("MainWindow", "Edit Profile"))
        self.edit_dob.setPlaceholderText(_translate("MainWindow", "Date of Birth"))
        self.edit_address.setPlaceholderText(_translate("MainWindow", "Address"))
        self.edit_zipcode.setPlaceholderText(_translate("MainWindow", "Postal Code"))
        self.edit_sex.setPlaceholderText(_translate("MainWindow", "Sex"))
        self.edit_height.setPlaceholderText(_translate("MainWindow", "Height"))
        self.edit_weight.setPlaceholderText(_translate("MainWindow", "Weight"))
        self.update_info_btn.setText(_translate("MainWindow", "Update"))
        self.back_btn.setText(_translate("MainWindow", "Back"))

