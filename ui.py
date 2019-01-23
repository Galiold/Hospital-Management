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
        MainWindow.resize(1154, 1005)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #303841;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
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
        self.username.setStyleSheet("border: 2px solid #fff;\n"
"color: #fff; margin:0;")
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
        self.verticalLayout_4.setContentsMargins(-1, 10, -1, 30)
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
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
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
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
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
        self.reception_table.setGeometry(QtCore.QRect(50, 130, 650, 650))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reception_table.sizePolicy().hasHeightForWidth())
        self.reception_table.setSizePolicy(sizePolicy)
        self.reception_table.setMinimumSize(QtCore.QSize(650, 650))
        self.reception_table.setStyleSheet("background-color: white;")
        self.reception_table.setObjectName("reception_table")
        self.reception_table.setColumnCount(0)
        self.reception_table.setRowCount(0)
        self.delete_freetime_btn = QtWidgets.QPushButton(self.Reception_Page)
        self.delete_freetime_btn.setGeometry(QtCore.QRect(870, 300, 113, 32))
        self.delete_freetime_btn.setObjectName("delete_freetime_btn")
        self.add_freetime_btn = QtWidgets.QPushButton(self.Reception_Page)
        self.add_freetime_btn.setGeometry(QtCore.QRect(870, 510, 113, 32))
        self.add_freetime_btn.setObjectName("add_freetime_btn")
        self.clear_time_btn = QtWidgets.QPushButton(self.Reception_Page)
        self.clear_time_btn.setGeometry(QtCore.QRect(850, 350, 161, 32))
        self.clear_time_btn.setObjectName("clear_time_btn")
        self.PageStack.addWidget(self.Reception_Page)
        self.Pharmacy_Page = QtWidgets.QWidget()
        self.Pharmacy_Page.setObjectName("Pharmacy_Page")
        self.addDrug_btn = QtWidgets.QPushButton(self.Pharmacy_Page)
        self.addDrug_btn.setGeometry(QtCore.QRect(830, 300, 256, 50))
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
        self.deleteDrug_btn.setGeometry(QtCore.QRect(830, 390, 256, 50))
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
        self.filterDrug_btn.setGeometry(QtCore.QRect(830, 500, 256, 50))
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
        self.pPresc_btn.setGeometry(QtCore.QRect(830, 600, 256, 50))
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
        self.drugs_table.setGeometry(QtCore.QRect(100, 130, 650, 650))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drugs_table.sizePolicy().hasHeightForWidth())
        self.drugs_table.setSizePolicy(sizePolicy)
        self.drugs_table.setMinimumSize(QtCore.QSize(650, 650))
        self.drugs_table.setStyleSheet("background-color: white;")
        self.drugs_table.setObjectName("drugs_table")
        self.drugs_table.setColumnCount(0)
        self.drugs_table.setRowCount(0)
        self.PageStack.addWidget(self.Pharmacy_Page)
        self.gridLayout.addWidget(self.PageStack, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1154, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.PageStack.setCurrentIndex(5)
        self.selected_role.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.user_lbl.setText(_translate("MainWindow", "Username"))
        self.pass_lbl.setText(_translate("MainWindow", "Password"))
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
        self.AdminPanel.setText(_translate("MainWindow", "Adminstration Panel"))
        self.approve_user_btn.setText(_translate("MainWindow", "Approve User"))
        self.delete_user_btn.setText(_translate("MainWindow", "Delete User"))
        self.add_user_btn.setText(_translate("MainWindow", "Add New User"))
        self.label_7.setText(_translate("MainWindow", "Enter your email here, we will send you a new password."))
        self.recovery_submit_btn.setText(_translate("MainWindow", "Submit"))
        self.delete_freetime_btn.setText(_translate("MainWindow", "Delete Free Time"))
        self.add_freetime_btn.setText(_translate("MainWindow", "Add Free Time"))
        self.clear_time_btn.setText(_translate("MainWindow", "Delete Appointment"))
        self.addDrug_btn.setText(_translate("MainWindow", "Add"))
        self.deleteDrug_btn.setText(_translate("MainWindow", "Delete"))
        self.filterDrug_btn.setText(_translate("MainWindow", "Filter"))
        self.pPresc_btn.setText(_translate("MainWindow", "Process Prescription"))

