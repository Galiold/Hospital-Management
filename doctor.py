import smtplib


dr_id = None


def set_dr_id(id):
    global dr_id
    dr_id = id


def approve_appointment(appointmentID, cursor, db):
    sql = "UPDATE Appointments SET Status = 1 WHERE AppointmentID = %s"
    cursor.execute(sql, appointmentID)
    db.commit()


def delete_apponitment(appointmentID, cursor, db):
    sql = "update Appointments set PatientID = NULL where AppointmentID = %s"
    cursor.execute(sql, appointmentID)
    db.commit()


def delete_freetime(appointmentID, cursor, db):
    sql = "delete from Appointments where AppointmentID = %s"
    cursor.execute(sql, appointmentID)
    db.commit()
    # send email to the patient


def add_free_time(cursor, db, time, DrID):
    sql = "insert into Appointments (Time , DrID) values (%s,%s)"
    cursor.execute(sql, (time, DrID))
    db.commit()


def show_drug_usage_history(patient_id, cursor):
    cursor.execute("SELECT DISTINCT Name FROM Prescription, Drugs, Appointments WHERE Prescription.DrugID = Drugs.ID AND "
                    "Prescription.AppointmentID = Appointments.AppointmentID AND PatientID = %s)", patient_id)
    return cursor.fetchall()


def request_lab_test():
    pass


def send_private_message():
    pass


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
