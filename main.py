from functools import partial
from time import sleep

from PyQt5 import QtWidgets

import user_management
import login
import ui
import register
import manager
import reception

manager_add_user = False

admin_db = user_management.database_admin()
admin_cursor = admin_db.cursor()

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
    global manager_add_user
    name_in = ui.name.toPlainText()
    email_in = ui.email.toPlainText()
    phone_in = ui.phone.toPlainText()
    passwd_in = ui.passwd.toPlainText()
    role_in = ui.selected_role.currentText()
    register.register_user(name_in, email_in, phone_in, passwd_in, role_in)
    if manager_add_user is True:
        manager.approve(email_in)
        sql = "SELECT email,phone,username FROM Registrations"
        admin_cursor.execute(sql)
        pending_list = admin_cursor.fetchall()
        ui.tableWidget.clear()
        manager.fill_pending_user_table(ui, pending_list)
        ui.PageStack.setCurrentIndex(2)
        manager_add_user = False
    else:
        ui.PageStack.setCurrentIndex(0)


def add_user_clicked(ui):
    global manager_add_user
    manager_add_user = True
    signup_clicked(ui)


def approve_pending_user(ui):
    a = QtWidgets.QWidget()
    email_in, ok = QtWidgets.QInputDialog.getText(a, 'Dialog', 'Enter email')
    if ok:
        manager.approve(email_in)
    sql = "SELECT email,phone,username FROM Registrations"
    admin_cursor.execute(sql)
    pending_list = admin_cursor.fetchall()
    manager.fill_table(ui.tableWidget, pending_list)


def delete_pending_user(ui, app):
    a = QtWidgets.QWidget()
    email_in, ok = QtWidgets.QInputDialog.getText(a, 'Dialog', 'Enter email')
    if ok:
        manager.delete(str(email_in))
    sql = "SELECT email,phone,username FROM Registrations"
    admin_cursor.execute(sql)
    pending_list = admin_cursor.fetchall()
    manager.fill_table(ui.tableWidget, pending_list)


def delete_free_time(ui):
    a = QtWidgets.QWidget()
    appointmentid_in, ok = QtWidgets.QInputDialog.getText(a, 'Delete Free Time', 'Enter Appointment ID')
    if ok:
        reception.delete_free_time(int(appointmentid_in), admin_cursor, admin_db)
    sql = "SELECT * FROM Appointments"
    admin_cursor.execute(sql)
    appointments = admin_cursor.fetchall()
    print(appointments)
    manager.fill_table(ui.reception_table, appointments)


def delete_appointment(ui):
    a = QtWidgets.QWidget()
    appointmentid_in, ok = QtWidgets.QInputDialog.getText(a, 'Delete Appointment', 'Enter Appointment ID')
    if ok:
        reception.delete_apponitment(int(appointmentid_in), admin_cursor, admin_db)
    sql = "SELECT * FROM Appointments"
    admin_cursor.execute(sql)
    appointments = admin_cursor.fetchall()
    manager.fill_table(ui.reception_table, appointments)


def add_free_time(ui):
    a = QtWidgets.QWidget()
    dr_id_in, dr_ok = QtWidgets.QInputDialog.getText(a, 'Add Free Time', 'Enter Dr ID')
    time_in, time_ok = QtWidgets.QInputDialog.getText(a, 'Add Free Time', 'Enter Time')
    if dr_ok and time_ok:
        reception.add_free_time(str(time_in), str(dr_id_in), admin_cursor, admin_db)
    sql = "SELECT * FROM Appointments"
    admin_cursor.execute(sql)
    appointments = admin_cursor.fetchall()
    manager.fill_table(ui.reception_table, appointments)


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

    ui.delete_user_btn.clicked.connect(partial(delete_pending_user, ui, app))

    ui.add_user_btn.clicked.connect(partial(add_user_clicked, ui))  # adding user as manager

    ui.delete_freetime_btn.clicked.connect(partial(delete_free_time, ui))

    ui.clear_time_btn.clicked.connect(partial(delete_appointment, ui))

    ui.add_freetime_btn.clicked.connect(partial(add_free_time, ui))

    sys.exit(app.exec_())
