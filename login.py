import smtplib

import user_management
import manager
import doctor
import patient
import laboratory

enter_db = user_management.database_admin()
enter_cursor = enter_db.cursor()

user_db = user_management.database_admin()

user_id = None


def get_db():
    return user_db


def manager_login(ui):
    sql = "SELECT email,phone,username FROM Registrations"
    enter_cursor.execute(sql)
    pending_list = enter_cursor.fetchall()
    manager.fill_table(ui.tableWidget, pending_list)
    ui.PageStack.setCurrentIndex(2)


def doctor_login(id, ui):
    global user_id
    doctor.set_dr_id(id)
    user_id = id
    enter_db.commit()
    sql = "SELECT * From Appointments WHERE DrID = %s ORDER BY AppointmentID"
    enter_cursor.execute(sql, id)
    appointments = enter_cursor.fetchall()
    manager.fill_table(ui.dr_appmnts_table, appointments)
    ui.PageStack.setCurrentIndex(6)


# def nurse_login():


def patient_login(id, ui):
    global user_id
    patient.set_patient_id(id)
    user_id = id
    enter_db.commit()
    sql = "SELECT * From Appointments WHERE PatientID = %s OR PatientID IS NULL ORDER BY AppointmentID"
    enter_cursor.execute(sql, id)
    appointments = enter_cursor.fetchall()
    manager.fill_table(ui.P_AppointmentsTable, appointments)
    ui.PageStack.setCurrentIndex(8)


def laboratory_login(id, ui):
    global user_id
    user_id = id
    laboratory.set_lab_id(id)
    sql = "SELECT * FROM Test"
    enter_cursor.execute(sql)
    tests = enter_cursor.fetchall()
    manager.fill_table(ui.Lab_Table, tests)
    ui.PageStack.setCurrentIndex(9)


def pharmacy_login(id, ui):
    global user_id
    user_id = id
    sql = "SELECT * FROM Drugs"
    enter_cursor.execute(sql)
    appointments = enter_cursor.fetchall()
    manager.fill_table(ui.drugs_table, appointments)
    ui.PageStack.setCurrentIndex(5)


def accountant_login(id, ui):
    global user_id
    user_id = id
    pass

def reception_login(id, ui):
    global user_id
    user_id = id
    sql = "SELECT * FROM Appointments"
    enter_cursor.execute(sql)
    appointments = enter_cursor.fetchall()
    manager.fill_table(ui.reception_table, appointments)
    ui.PageStack.setCurrentIndex(4)


def login(user, passwd, ui):

    print("enter id")
    username = user
    print("enter password")
    password = passwd

    enter_db.commit()
    if username == "admin" and password == "admin":
        manager_login(ui)

    elif username[0] == "d":
        sql = " select * from Doctors where ID= %s and Password = %s"
        val = (username, password,)
        print(val)
        res = enter_cursor.execute(sql, val)
        if res == 0:
            print("id or password is not correct !")
        else:
            doctor_login(username, ui)

    # elif username[0] == "n":
    #     sql = " select * from Nurses where ID= %s and Password = %s"
    #     val = (username, password)
    #     res = enter_cursor.execute(sql, val)
    #     if res == 0:
    #         print("id or password is not correct !")
    #     else:
    #         nurse_login()

    elif username[0] == "p":
        sql = " select * from Patients where ID= %s and Password = %s"
        val = (username, password)
        res = enter_cursor.execute(sql, val)
        if res == 0:
            print("id or password is not correct !")
        else:
            patient_login(username, ui)

    elif username[0] == "l":
        sql = " select * from Laboratory where ID= %s and Password = %s"
        val = (username, password)
        res = enter_cursor.execute(sql, val)
        if res == 0:
            print("id or password is not correct !")
        else:
            laboratory_login(username, ui)

    elif username[0] == "h":
        sql = " select * from Pharmacy where ID= %s and Password = %s"
        val = (username, password)
        res = enter_cursor.execute(sql, val)
        if res == 0:
            print("id or password is not correct !")
        else:
            pharmacy_login(username, ui)

    elif username[0] == "a":
        sql = " select * from Accountant where ID= %s and Password = %s"
        val = (username, password)
        res = enter_cursor.execute(sql, val)
        if res == 0:
            print("id or password is not correct !")
        else:
            accountant_login(username, ui)

    elif username[0] == "r":
        sql = " select * from Reception where ID= %s and Password = %s"
        val = (username, password)
        res = enter_cursor.execute(sql, val)
        if res == 0:
            print("id or password is not correct !")
        else:
            reception_login(username, ui)


def forgot_password(email):

    sql = "select Password FROM Doctors where Email = %s"
    res = enter_cursor.execute(sql, email)
    if res > 0:
        result = enter_cursor.fetchone()
        password_mail(email, result)

    sql = "select Password FROM Nurses where Email = %s"
    res = enter_cursor.execute(sql, email)
    if res > 0:
        result = enter_cursor.fetchone()
        password_mail(email, result)

    sql = "select Password FROM Accountant where Email = %s"
    res = enter_cursor.execute(sql, email)
    if res > 0:
        result = enter_cursor.fetchone()
        password_mail(email, result)

    sql = "select Password FROM Reception where Email = %s"
    res = enter_cursor.execute(sql, email)
    if res>0 :
        result = enter_cursor.fetchone()
        password_mail(email, result)

    sql = "select Password FROM Laboratory where Email = %s"
    res = enter_cursor.execute(sql, email)
    if res>0 :
        result = enter_cursor.fetchone()
        password_mail(email, result)

    sql = "select Password FROM Pharmacy where Email = %s"
    res = enter_cursor.execute(sql, email)
    if res > 0:
        result = enter_cursor.fetchone()
        password_mail(email, result)

    sql = "select Password FROM Patients where Email = %s"
    res = enter_cursor.execute(sql, email)
    if res > 0:
        result = enter_cursor.fetchone()
        password_mail(email, result)

def password_mail(email, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("ali.goldani97@gmail.com", "13760000")
    msg = "\nYour password is : %s! \n" % (password)
    server.sendmail("ali.goldani97@gmail.com", str(email), msg)
    server.quit()
