import smtplib

from PyQt5.QtWidgets import QTableWidgetItem
# from PyQt5.uic.properties import QtGui
import user_management

admin_db = user_management.database_admin()
admin_cursor = admin_db.cursor()


def fill_pending_user_table(ui):
    sql = "SELECT email,phone,username FROM Registrations"
    admin_cursor.execute(sql)
    pending_list = admin_cursor.fetchall()
    if len(pending_list) > 0:
        ui.tableWidget.setRowCount(len(pending_list))
        ui.tableWidget.setColumnCount(len(pending_list[0]))
        for i in range(len(pending_list)):
            for j in range(len(pending_list[0])):
                ui.tableWidget.setItem(i, j, QTableWidgetItem(str(pending_list[i][j])))
    else:
        pass


def clear_table(ui):
    while ui.tableWidget.rowCount() > 0:
        ui.tableWidget.removeRow(0)


def send_mail(id: object, password: object):
    # print(0)
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    # print(1)
    server.starttls()
    # print(2)
    server.login("holmes_sh98@yahoo.com", "H0lmesofPast")
    # print(3)
    msg = "\n YOUR id is %s and your password is : %s ! \n" % (id, password)
    server.sendmail("holmes_sh98@yahoo.com", "goldani.ali@aol.com", msg)
    # print(4)
    server.quit()


def approve_doctor(sql, result, email):
    admin_cursor.execute("select increment from Doctors order by increment desc ")
    last_id = admin_cursor.fetchone()
    if last_id is None:
        id = "d1"
    else:
        increment = int(last_id[0]) + 1
        id = 'd' + str(increment)
    send_mail(id, result[3])
    val = (id, result[2], result[3], result[4], result[5])
    admin_cursor.execute(sql, val)
    admin_db.commit()
    admin_cursor.execute("delete from Registrations where email = %s", email)
    admin_db.commit()


def approve_nurse(sql, result, email):
    admin_cursor.execute("select increment from Nurses order by ID desc ")
    last_id = admin_cursor.fetchone()
    if last_id is None:
        id = "n1"
    else:
        increment = int(last_id[0]) + 1
        id = 'n' + str(increment)
    val = (id, result[2], result[3], result[4], result[5])
    admin_cursor.execute(sql, val)
    admin_db.commit()
    admin_cursor.execute("delete from Registrations where email = %s", email)
    admin_db.commit()


def approve_patient(sql, result, email):
    admin_cursor.execute("select increment from Patients order by ID desc ")
    last_id = admin_cursor.fetchone()
    if last_id is None:
        id = "p1"
    else:
        increment = int(last_id[0]) + 1
        id = 'p' + str(increment)
    val = (id, result[2], result[3], result[4], result[5])
    admin_cursor.execute(sql, val)
    admin_db.commit()
    admin_cursor.execute("delete from Registrations where email = %s", email)
    admin_db.commit()


def approve_laboratory(sql, result, email):
    admin_cursor.execute("select increment from Laboratory order by ID desc ")
    last_id = admin_cursor.fetchone()
    if last_id is None:
        id = "l1"
    else:
        increment = int(last_id[0]) + 1
        id = 'l' + str(increment)
    val = (id, result[2], result[3], result[4], result[5])
    admin_cursor.execute(sql, val)
    admin_db.commit()
    admin_cursor.execute("delete from Registrations where email = %s", email)
    admin_db.commit()


def approve_pharmacy(sql, result, email):
    admin_cursor.execute("select increment from Pharmacy order by ID desc ")
    last_id = admin_cursor.fetchone()
    if last_id is None:
        id = "h1"
    else:
        increment = int(last_id[0]) + 1
        id = 'h' + str(increment)
    val = (id, result[2], result[3], result[4], result[5])
    admin_cursor.execute(sql, val)
    admin_db.commit()
    admin_cursor.execute("delete from Registrations where email = %s", email)
    admin_db.commit()


def approve_accountant(sql, result, email):
    admin_cursor.execute("select increment from Accountant order by ID desc ")
    last_id = admin_cursor.fetchone()
    if last_id is None:
        id = "a1"
    else:
        increment = int(last_id[0]) + 1
        id = 'a' + str(increment)
    val = (id, result[2], result[3], result[4], result[5])
    admin_cursor.execute(sql, val)
    admin_db.commit()
    admin_cursor.execute("delete from Registrations where email = %s", email)
    admin_db.commit()


def approve_reception(sql, result, email):
    admin_cursor.execute("select increment from Reception order by ID desc ")
    last_id = admin_cursor.fetchone()
    if last_id is None:
        id = "r1"
    else:
        increment = int(last_id[0]) + 1
        id = 'r' + str(increment)
    val = (id, result[2], result[3], result[4], result[5])
    admin_cursor.execute(sql, val)
    admin_db.commit()
    admin_cursor.execute("delete from Registrations where email = %s", email)
    admin_db.commit()


# ////////////////////////////////// Manager Functions \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def approve(email):
    admin_cursor.execute("SELECT * FROM Registrations WHERE email=%s", email)
    result = admin_cursor.fetchone()

    if result[1] == 'd':
        sql = "insert into Doctors (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        approve_doctor(sql, result, email)
    elif result[1] == "n":
        sql = "insert into Nurses (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        approve_nurse(sql, result, email)
    elif result[1] == "p":
        sql = "insert into Patients (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        approve_patient(sql, result, email)

    elif result[1] == "l":
        sql = "insert into Laboratory (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        approve_laboratory(sql, result, email)

    elif result[1] == "h":
        sql = "insert into Pharmacy (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        approve_pharmacy(sql, result, email)

    elif result[1] == "a":
        sql = "insert into Accountant (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        approve_accountant(sql, result, email)

    elif result[1] == "r":
        sql = "insert into Reception (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        approve_reception(sql, result, email)


def delete(email):
    sql = "delete from Registrations where email = %s"
    admin_cursor.execute(sql, email)
    admin_db.commit()
