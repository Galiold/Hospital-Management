from functools import partial

from PyQt5 import QtWidgets

import login
import ui
import register


def btn_clicked(ui):
    username_in = ui.username.toPlainText()
    pass_in = ui.password.toPlainText()
    login.login(username_in, pass_in, ui)


def signup_clicked(ui):
    ui.PageStack.setCurrentIndex(1)


def submit_register_form(ui):
    name_in = ui.name.toPlainText()
    email_in = ui.email.toPlainText()
    phone_in = ui.phone.toPlainText()
    passwd_in = ui.passwd.toPlainText()
    role_in = ui.selected_role.currentText()
    register.register_user(name_in, email_in, phone_in, passwd_in, role_in)
    ui.PageStack.setCurrentIndex(0)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.PageStack.setCurrentIndex(0)

    ui.login_btn.clicked.connect(partial(btn_clicked, ui))

    ui.signup_btn.clicked.connect(partial(signup_clicked, ui))

    ui.submit_btn.clicked.connect(partial(submit_register_form, ui))

    # ui.approve.clicked.connect(partial())
    # ui.selected_role.currentText()
    # signup_page.submit_btn.
    # ui.tableWidget.setItem()
    sys.exit(app.exec_())
