from functools import partial

from PyQt5 import QtWidgets

import login
import ui
import register
import manager


def btn_clicked(ui):
    username_in = ui.username.toPlainText()
    pass_in = ui.password.toPlainText()
    login.login(username_in, pass_in, ui)


def forgot_clicked(ui):
    ui.PageStack.setCurrentIndex(3)


def password_recovery(ui):
    email_in = ui.recovery_email.toPlainText()
    login.forgot_password(email_in)
    ui.PageStack.setCurrentIndex(0)


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


def approve_pending_user(ui):
    email_in = ui.selected_email.toPlainText()
    manager.approve(email_in)
    ui.tableWidget.clear()
    manager.fill_pending_user_table(ui)


def delete_pending_user(ui):
    email_in = ui.selected_email.toPlainText()
    manager.delete(email_in)
    ui.tableWidget.clear()
    manager.fill_pending_user_table(ui)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.PageStack.setCurrentIndex(0)

    ui.login_btn.clicked.connect(partial(btn_clicked, ui))

    ui.passwd_forgot_btn.clicked.connect(partial(forgot_clicked, ui))

    ui.recovery_submit_btn.clicked.connect(partial(password_recovery, ui))

    ui.signup_btn.clicked.connect(partial(signup_clicked, ui))

    ui.submit_btn.clicked.connect(partial(submit_register_form, ui))

    ui.approve_user_btn.clicked.connect(partial(approve_pending_user, ui))

    ui.delete_user_btn.clicked.connect(partial(delete_pending_user, ui))

    # ui.tableWidget.clearContents()

    sys.exit(app.exec_())
