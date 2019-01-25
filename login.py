import smtplib

import user_management
import manager
import doctor
import patient
import laboratory

admin_db = user_management.database_admin()
admin_cursor = admin_db.cursor()

doctor_db = user_management.database_doctor()
doctor_cursor = doctor_db.cursor()


def manager_login(ui):
    sql = "SELECT email,phone,username FROM Registrations"
    admin_cursor.execute(sql)
    pending_list = admin_cursor.fetchall()
    manager.fill_table(ui.tableWidget, pending_list)
    ui.PageStack.setCurrentIndex(2)


def doctor_login(id, ui):
    doctor.set_dr_id(id)
    print(doctor.dr_id)
    sql = "SELECT * From Appointments WHERE DrID = %s ORDER BY AppointmentID"
    doctor_cursor.execute(sql, id)
    appointments = doctor_cursor.fetchall()
    manager.fill_table(ui.dr_appmnts_table, appointments)
    ui.PageStack.setCurrentIndex(6)


def nurse_login():
    while True:
        print("------------- Nurse Panel ---------------")
        print('''
        1. change/complete your profile info
        2. exit
        ''')
        choice = input()

        if int(choice) == 1:
            profile_update("Doctors", id)
        elif int(choice) == 2:
            break


def patient_login(id, ui):
    patient.set_patient_id(id)
    sql = "SELECT * From Appointments WHERE PatientID = %s OR PatientID IS NULL ORDER BY AppointmentID"
    admin_cursor.execute(sql, id)
    appointments = admin_cursor.fetchall()
    manager.fill_table(ui.P_AppointmentsTable, appointments)
    ui.PageStack.setCurrentIndex(8)


def laboratory_login(ui):
    laboratory.set_lab_id(id)
    sql = "SELECT * FROM Test"
    admin_cursor.execute(sql)
    tests = admin_cursor.fetchall()
    manager.fill_table(ui.Lab_Table, tests)
    ui.PageStack.setCurrentIndex(9)


def pharmacy_login(ui):
    sql = "SELECT * FROM Drugs"
    admin_cursor.execute(sql)
    appointments = admin_cursor.fetchall()
    manager.fill_table(ui.drugs_table, appointments)
    ui.PageStack.setCurrentIndex(5)
    # while True:
    #     name = "Arman"  # query to get the name
    #     print("------------- Pharmacy Panel ---------------")
    #     print('''
    #     1. change/complete your profile info
    #     2. exit
    #     ''')
    #     choice = input()
    #
    #     if int(choice) == 1:
    #         profile_update("Doctors", id)
    #     elif int(choice) == 2:
    #         break


def accountant_login():
    while True:
        name = "Arman"  # query to get the name
        print("------------- Accountant Panel ---------------")
        print('''
        1. change/complete your profile info
        2. exit
        ''')
        choice = input()

        if int(choice) == 1:
            profile_update("Doctors", id)
        elif int(choice) == 2:
            break


def reception_login(ui):
    sql = "SELECT * FROM Appointments"
    admin_cursor.execute(sql)
    appointments = admin_cursor.fetchall()
    manager.fill_table(ui.reception_table, appointments)
    ui.PageStack.setCurrentIndex(4)


def login(user, passwd, ui):

    print("enter id")
    username = user
    print("enter password")
    password = passwd

    if username == "admin" and password == "admin":
        manager_login(ui)

    elif username[0] == "d":
        sql = " select * from Doctors where ID= %s and Password = %s"
        val = (username, password,)
        print(val)
        res = admin_cursor.execute(sql, val)
        if res == 0:
            print("id or password is not correct !")
        else:
            doctor_login(username, ui)

    elif username[0] == "n":
        sql = " select * from Nurses where ID= %s and Password = %s"
        val = (username, password)
        res = admin_cursor.execute(sql, val)
        if res == 0:
            print("id or password is not correct !")
        else:
            nurse_login()

    elif username[0] == "p":
        sql = " select * from Patients where ID= %s and Password = %s"
        val = (username, password)
        res = admin_cursor.execute(sql, val)
        if res == 0:
            print("id or password is not correct !")
        else:
            patient_login(username, ui)

    elif username[0] == "l":
        sql = " select * from Laboratory where ID= %s and Password = %s"
        val = (username, password)
        res = admin_cursor.execute(sql, val)
        if res == 0:
            print("id or password is not correct !")
        else:
            laboratory_login(ui)

    elif username[0] == "h":
        sql = " select * from Pharmacy where ID= %s and Password = %s"
        val = (username, password)
        res = admin_cursor.execute(sql, val)
        if res == 0:
            print("id or password is not correct !")
        else:
            pharmacy_login(ui)

    elif username[0] == "a":
        sql = " select * from Accountant where ID= %s and Password = %s"
        val = (username, password)
        res = admin_cursor.execute(sql, val)
        if res == 0:
            print("id or password is not correct !")
        else:
            accountant_login()

    elif username[0] == "r":
        sql = " select * from Reception where ID= %s and Password = %s"
        val = (username, password)
        res = admin_cursor.execute(sql, val)
        if res == 0:
            print("id or password is not correct !")
        else:
            reception_login(ui)


def forgot_password(email):

    sql = "select Password FROM Doctors where Email = %s"
    res = admin_cursor.execute(sql, email)
    if res > 0:
        result = admin_cursor.fetchone()
        password_mail(result)

    sql = "select Password FROM Nurses where Email = %s"
    res = admin_cursor.execute(sql, email)
    if res > 0:
        result = admin_cursor.fetchone()
        password_mail(result)

    sql = "select Password FROM Accountant where Email = %s"
    res = admin_cursor.execute(sql, email)
    if res > 0:
        result = admin_cursor.fetchone()
        password_mail(result)

    sql = "select Password FROM Reception where Email = %s"
    res = admin_cursor.execute(sql, email)
    if res>0 :
        result = admin_cursor.fetchone()
        password_mail(result)

    sql = "select Password FROM Laboratory where Email = %s"
    res = admin_cursor.execute(sql, email)
    if res>0 :
        result = admin_cursor.fetchone()
        password_mail(result)

    sql = "select Password FROM Pharmacy where Email = %s"
    res = admin_cursor.execute(sql, email)
    if res > 0:
        result = admin_cursor.fetchone()
        password_mail(result)

    sql = "select Password FROM Patients where Email = %s"
    res = admin_cursor.execute(sql, email)
    if res>0 :
        result = admin_cursor.fetchone()
        password_mail(result)

def password_mail(password):
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.starttls()
    server.login("holmes_sh98@yahoo.com", "H0lmesofPast")
    msg = "\n your password is : %s ! \n" % (password)
    server.sendmail("holmes_sh98@yahoo.com", "goldani.ali@aol.com", msg)
    server.quit()