from functools import partial
from PyQt5 import QtWidgets

import pharmacy
import user_management
import login
import ui
import register
import manager
import reception
import doctor
import patient
import laboratory

manager_add_user = False

db = user_management.database_admin()
cursor = db.cursor()


# TODO
#   - Fix message for both doctor and patient


# ---------------------- Login Panel ----------------------

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
        cursor.execute(sql)
        pending_list = cursor.fetchall()
        ui.tableWidget.clear()
        manager.fill_table(ui, pending_list)
        ui.PageStack.setCurrentIndex(2)
        manager_add_user = False
    else:
        ui.PageStack.setCurrentIndex(0)


# ---------------------- Manager Panel ----------------------

def add_user_clicked(ui):
    global manager_add_user
    manager_add_user = True
    signup_clicked(ui)


def approve_pending_user(ui):
    a = QtWidgets.QWidget()
    email_in, ok = QtWidgets.QInputDialog.getText(a, 'Dialog', 'Enter email')
    if ok:
        manager.approve(str(email_in), cursor, db)
    sql = "SELECT email,phone,username FROM Registrations"
    cursor.execute(sql)
    pending_list = cursor.fetchall()
    manager.fill_table(ui.tableWidget, pending_list)


def delete_pending_user(ui, app):
    a = QtWidgets.QWidget()
    email_in, ok = QtWidgets.QInputDialog.getText(a, 'Dialog', 'Enter email')
    if ok:
        manager.delete(str(email_in), cursor, db)
    sql = "SELECT email,phone,username FROM Registrations"
    cursor.execute(sql)
    pending_list = cursor.fetchall()
    manager.fill_table(ui.tableWidget, pending_list)


# ---------------------- Reception Panel ----------------------

def delete_free_time(ui):
    a = QtWidgets.QWidget()
    appointmentid_in, ok = QtWidgets.QInputDialog.getText(a, 'Delete Free Time', 'Enter Appointment ID')
    if ok:
        reception.delete_free_time(int(appointmentid_in), cursor, db)
    sql = "SELECT * FROM Appointments"
    cursor.execute(sql)
    appointments = cursor.fetchall()
    print(appointments)
    manager.fill_table(ui.reception_table, appointments)


def delete_appointment(ui):
    a = QtWidgets.QWidget()
    appointmentid_in, ok = QtWidgets.QInputDialog.getText(a, 'Delete Appointment', 'Enter Appointment ID')
    if ok:
        reception.delete_apponitment(int(appointmentid_in), cursor, db)
    sql = "SELECT * FROM Appointments"
    cursor.execute(sql)
    appointments = cursor.fetchall()
    manager.fill_table(ui.reception_table, appointments)


def add_free_time_rec(ui):
    a = QtWidgets.QWidget()
    dr_id_in, dr_ok = QtWidgets.QInputDialog.getText(a, 'Add Free Time', 'Enter Dr ID')
    time_in, time_ok = QtWidgets.QInputDialog.getText(a, 'Add Free Time', 'Enter Time')
    if dr_ok and time_ok:
        reception.add_free_time(str(time_in), str(dr_id_in), cursor, db)
    sql = "SELECT * FROM Appointments"
    cursor.execute(sql)
    appointments = cursor.fetchall()
    manager.fill_table(ui.reception_table, appointments)


# ---------------------- Pharmacy Panel ----------------------
def add_drug(ui):
    a = QtWidgets.QWidget()
    drug_name_in, drug_ok = QtWidgets.QInputDialog.getText(a, 'Add New Drug', 'Enter Drug Name')
    exp_in, exp_ok = QtWidgets.QInputDialog.getText(a, 'Add New Drug', 'Enter Expiration Date')
    if exp_ok and drug_ok:
        pharmacy.add_drug(str(drug_name_in), str(exp_in), cursor, db)
    sql = "SELECT * FROM Drugs"
    cursor.execute(sql)
    drugs = cursor.fetchall()
    manager.fill_table(ui.drugs_table, drugs)


def delete_drug(ui):
    a = QtWidgets.QWidget()
    drug_name_in, drug_ok = QtWidgets.QInputDialog.getText(a, 'Add New Drug', 'Enter Drug Name')
    if drug_ok:
        pharmacy.delete_drug(str(drug_name_in), cursor, db)
    sql = "SELECT * FROM Drugs"
    cursor.execute(sql)
    drugs = cursor.fetchall()
    manager.fill_table(ui.drugs_table, drugs)


def filter_drugs(ui):
    filtered_list = pharmacy.filter(cursor)
    manager.fill_table(ui.drugs_table, filtered_list)


def process_priscription(ui):
    a = QtWidgets.QWidget()
    prescription, pr_ok = QtWidgets.QInputDialog.getText(a, 'Process Prescription', 'Enter Appointment ID')
    if pr_ok:
        drug_name_list = pharmacy.process_prescription(cursor, prescription)

    s = ""
    for drug_name in drug_name_list:
        s = s + str(drug_name[0]) + "\n"

    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText("Prescription's drug list is as follows:")
    msg.setInformativeText(s)
    msg.setWindowTitle("Drug List")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.show()
    retval = msg.exec_()


# ---------------------- Dr Panel ----------------------

def approve_appointment(ui):
    a = QtWidgets.QWidget()
    appointment_id, pr_ok = QtWidgets.QInputDialog.getText(a, 'Approve Appointment', 'Enter Appointment ID')
    if pr_ok:
        doctor.approve_appointment(appointment_id, cursor, db)
    sql = "SELECT * FROM Appointments WHERE DrID = %s ORDER BY AppointmentID"
    cursor.execute(sql, doctor.dr_id)
    appointments = cursor.fetchall()
    manager.fill_table(ui.dr_appmnts_table, appointments)


def delete_appointment_dr(ui):
    a = QtWidgets.QWidget()
    appointment_id, pr_ok = QtWidgets.QInputDialog.getText(a, 'Delete Appointment', 'Enter Appointment ID')
    if pr_ok:
        doctor.delete_apponitment(appointment_id, cursor, db)
    sql = "SELECT * FROM Appointments WHERE DrID = %s ORDER BY AppointmentID"
    cursor.execute(sql, doctor.dr_id)
    appointments = cursor.fetchall()
    manager.fill_table(ui.dr_appmnts_table, appointments)


def add_free_time_dr(ui):
    a = QtWidgets.QWidget()
    time, pr_ok = QtWidgets.QInputDialog.getText(a, 'Add Free Time', 'Enter Time')
    if pr_ok:
        doctor.add_free_time(cursor, db, time, doctor.dr_id)
    sql = "SELECT * FROM Appointments WHERE DrID = %s ORDER BY AppointmentID"
    cursor.execute(sql, doctor.dr_id)
    appointments = cursor.fetchall()
    manager.fill_table(ui.dr_appmnts_table, appointments)


def delete_free_time_dr(ui):
    a = QtWidgets.QWidget()
    appointment_id, pr_ok = QtWidgets.QInputDialog.getText(a, 'Delete Appointment', 'Enter Appointment ID')
    if pr_ok:
        doctor.delete_freetime(appointment_id, cursor, db)
    sql = "SELECT * FROM Appointments WHERE DrID = %s ORDER BY AppointmentID"
    cursor.execute(sql, doctor.dr_id)
    appointments = cursor.fetchall()
    manager.fill_table(ui.dr_appmnts_table, appointments)


def show_drug_history(ui):
    a = QtWidgets.QWidget()
    patient_id, ok = QtWidgets.QInputDialog.getText(a, 'Show Drug Usage History', 'Enter Patient ID')
    if ok:
        drug_name_list = doctor.show_drug_usage_history(str(patient_id), cursor)
        s = ""
        for drug_name in drug_name_list:
            s = s + str(drug_name[0]) + "\n"


    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText("Patient's drug usage history is as follows:")
    msg.setInformativeText(s)
    msg.setWindowTitle("Drug List")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.show()
    retval = msg.exec_()


def send_message_dr(ui):
    messages = patient.get_messages(login.user_id, cursor)
    manager.fill_table(ui.message_table, messages)
    ui.PageStack.setCurrentIndex(7)


def presc_test():
    a = QtWidgets.QWidget()
    patient_id, ok = QtWidgets.QInputDialog.getText(a, 'Prescribe Test', 'Enter Patient ID')
    if ok:
        doctor.prescribe_test(str(patient_id), cursor, db)


def presc_drugs():
    a = QtWidgets.QWidget()
    appointment_id, app_ok = QtWidgets.QInputDialog.getText(a, 'Prescribe Drug', 'Enter Appointment ID')
    if app_ok:
        drug_count, dr_ok = QtWidgets.QInputDialog.getText(a, 'Prescribe Drug', 'Enter Drug Count')
        if dr_ok:
            for i in range(int(drug_count)):
                drug_name, drname_ok = QtWidgets.QInputDialog.getText(a, 'Prescribe Drug', 'Enter Drug Name')
                if drname_ok:
                    doctor.prescribe_drug(appointment_id, drug_name, cursor, db)


def dr_emergency():
    a = QtWidgets.QWidget()
    patient_id, ok = QtWidgets.QInputDialog.getText(a, 'Emergency State', 'Enter Patient ID')
    if ok:
        doctor.bed_assign(patient_id, cursor, db)


def exit_dr_panel(ui):
    pass


# ---------------------- Message Panel ----------------------
def send(ui):
    content = ui.messsage_txt.toPlainText()
    receiverid = ui.receiverid_txt.toPlainText()
    doctor.send_message(content, login.user_id, receiverid, cursor, db)
    messages = patient.get_messages(login.user_id, cursor)
    manager.fill_table(ui.message_table, messages)


# ---------------------- Patient Panel ----------------------
def p_reserve(ui):
    a = QtWidgets.QWidget()
    appointment_id, app_ok = QtWidgets.QInputDialog.getText(a, 'Reserve Appointment', 'Enter Appointment ID')
    if app_ok:
        patient.p_reserve_appointment(appointment_id, cursor, db)
    sql = "SELECT * FROM Appointments WHERE PatientID = %s OR PatientID IS NULL ORDER BY AppointmentID"
    cursor.execute(sql, patient.patient_id)
    appointments = cursor.fetchall()
    manager.fill_table(ui.P_AppointmentsTable, appointments)


def p_send_message(ui):
    messages = patient.get_messages(login.user_id, cursor)
    manager.fill_table(ui.message_table, messages)
    ui.PageStack.setCurrentIndex(7)


def p_show_bed_info():
    result = patient.p_show_bed_info(cursor, db)
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    if result:
        text = "Your bed id is %s." %result
        msg.setText(text)
    else:
        msg.setText("You have no bed.")
    msg.setWindowTitle("Bed info")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.show()
    retval = msg.exec_()


def p_show_prescription(ui):
    a = QtWidgets.QWidget()
    appointment_id, app_ok = QtWidgets.QInputDialog.getText(a, 'Show Prescription', 'Enter Appointment ID')
    if app_ok:
        drug_name_list = patient.show_prescription(appointment_id, cursor)
        s = ""
        for drug_name in drug_name_list:
            s = s + str(drug_name[0]) + "\n"


    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText("Drugs in this appointment")
    msg.setInformativeText(s)
    msg.setWindowTitle("Drug List")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.show()
    retval = msg.exec_()


# ---------------------- Lab Panel ----------------------
def answer_test():
    a = QtWidgets.QWidget()
    test_id, id_ok = QtWidgets.QInputDialog.getText(a, 'Send Diagnose Report', 'Enter Test ID:')
    test_result, res_ok = QtWidgets.QInputDialog.getMultiLineText(a, 'Send Diagnose Report', 'Enter diagnose report below:')
    if id_ok and res_ok:
        laboratory.set_diagnose_report(test_result, test_id, cursor, db)
    sql = "SELECT * FROM Test"
    cursor.execute(sql)
    result = cursor.fetchall()
    manager.fill_table(ui.Lab_Table, result)


# ---------------------- Update Panel ----------------------

def update_info(ui):
    user_management.profile_update(login.user_id, ui, cursor, db)


def update_info_page(ui):
    ui.PageStack.setCurrentIndex(10)


def exit(ui):
    login.user_id = None
    ui.PageStack.setCurrentIndex(0)


def back_to_menu(ui):
    id = login.user_id
    if id[0] == 'd':
        ui.PageStack.setCurrentIndex(6)
    elif id[0] == 'p':
        ui.PageStack.setCurrentIndex(8)
    elif id[0] == 'l':
        ui.PageStack.setCurrentIndex(9)
    elif id[0] == 'h':
        ui.PageStack.setCurrentIndex(5)
    # elif id[0] == 'n':
    #     table = "Nurses"
    elif id[0] == 'r':
        ui.PageStack.setCurrentIndex(4)
    # elif id[0] == 'a':
    #     table = "Accountant"


def back_to_login(ui):
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

    ui.passwd_forgot_btn.clicked.connect(partial(forgot_clicked, ui))

    ui.recovery_submit_btn.clicked.connect(partial(password_recovery, ui))

    ui.signup_btn.clicked.connect(partial(signup_clicked, ui))

    ui.submit_btn.clicked.connect(partial(submit_register_form, ui))

    ui.approve_user_btn.clicked.connect(partial(approve_pending_user, ui))

    ui.delete_user_btn.clicked.connect(partial(delete_pending_user, ui, app))

    ui.add_user_btn.clicked.connect(partial(add_user_clicked, ui))  # adding user as manager

    ui.delete_freetime_btn.clicked.connect(partial(delete_free_time, ui))

    ui.clear_time_btn.clicked.connect(partial(delete_appointment, ui))

    ui.add_freetime_btn.clicked.connect(partial(add_free_time_rec, ui))

    ui.addDrug_btn.clicked.connect(partial(add_drug, ui))

    ui.deleteDrug_btn.clicked.connect(partial(delete_drug, ui))

    ui.filterDrug_btn.clicked.connect(partial(filter_drugs, ui))

    ui.pPresc_btn.clicked.connect(partial(process_priscription, ui))

    ui.dr_approve_btn.clicked.connect(partial(approve_appointment, ui))

    ui.dr_delete_btn.clicked.connect(partial(delete_appointment_dr, ui))

    ui.dr_addfree_btn.clicked.connect(partial(add_free_time_dr, ui))

    ui.drug_history_btn.clicked.connect(partial(show_drug_history, ui))

    ui.dr_sendmessage_btn.clicked.connect(partial(send_message_dr, ui))

    ui.sendmessage_btn.clicked.connect(partial(send, ui))

    ui.pre_test_btn.clicked.connect(presc_test)

    ui.pre_drug_btn.clicked.connect(presc_drugs)

    ui.delete_freetime_btn.clicked.connect(partial(delete_free_time, ui))

    ui.dr_emergency_btn.clicked.connect(dr_emergency)

    ui.P_SendMessage.clicked.connect(partial(p_send_message, ui))

    ui.P_ShowBedInfo.clicked.connect(partial(p_show_bed_info))

    ui.Patient_ReserveAppointment.clicked.connect(partial(p_reserve, ui))

    ui.P_ShowPrescription.clicked.connect(partial(p_show_prescription, ui))

    ui.lab_send_result_btn.clicked.connect(answer_test)

    ui.update_info_btn.clicked.connect(partial(update_info, ui))

    ui.dr_edit_info_btn.clicked.connect(partial(update_info_page, ui))

    ui.patient_edit_info_btn_2.clicked.connect(partial(update_info_page, ui))

    ui.pharmacy_edit_info_btn.clicked.connect(partial(update_info_page, ui))

    ui.lab_edit_info_btn_2.clicked.connect(partial(update_info_page, ui))

    ui.reception_edit_info_btn.clicked.connect(partial(update_info_page, ui))

    ui.admin_exit_btn.clicked.connect(partial(exit, ui))
    ui.dr_exit_btn.clicked.connect(partial(exit, ui))
    ui.phar_exit_btn.clicked.connect(partial(exit, ui))
    ui.P_Exit.clicked.connect(partial(exit, ui))
    ui.lab_exit_btn.clicked.connect(partial(exit, ui))
    ui.reception_exit_btn.clicked.connect(partial(exit, ui))

    ui.back_btn.clicked.connect(partial(back_to_menu, ui))
    ui.msg_back_btn.clicked.connect(partial(back_to_menu, ui))
    ui.register_back_btn.clicked.connect(partial(back_to_login, ui))


    # ui.Lab_Table.resizeRowsToContents()
    # ui.receiverid_txt

    sys.exit(app.exec_())
