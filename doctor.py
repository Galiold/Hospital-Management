import datetime
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
    sql = "SELECT Patients.Email, Appointments.Time FROM Patients, Appointments WHERE Patients.ID = Appointments.PatientID AND AppointmentID = %s"
    cursor.execute(sql, appointmentID)
    result = cursor.fetchone()
    email = result[0]
    appointment_time = result[1]
    sql = "update Appointments set PatientID = NULL where AppointmentID = %s"
    cursor.execute(sql, appointmentID)
    db.commit()
    msg = "\nSorry, your appointment at %s is canceled." % appointment_time
    send_mail(email, msg)


def delete_freetime(appointmentID, cursor, db):
    sql = "delete from Appointments where AppointmentID = %s"
    cursor.execute(sql, appointmentID)
    db.commit()


def add_free_time(cursor, db, time, DrID):
    sql = "insert into Appointments (Time , DrID) values (%s,%s)"
    cursor.execute(sql, (time, DrID))
    db.commit()


def show_drug_usage_history(patient_id, cursor):
    cursor.execute(
        "SELECT DISTINCT Name FROM Prescription, Drugs, Appointments WHERE Prescription.DrugID = Drugs.ID AND Prescription.AppointmentID = Appointments.AppointmentID AND PatientID = %s",
        patient_id)
    return cursor.fetchall()


def request_lab_test():
    pass


def send_message(content, receiver_id, cursor, db):
    sql = "insert into Messages (SenderID,ReceiverID,Text,Date) values (%s,%s,%s,%s)"
    cursor.execute(sql, (dr_id, receiver_id, content, datetime.datetime.today().strftime('%Y-%m-%d')))
    db.commit()
    # else:
    # sql = "insert into Messages (SenderID,ReceiverID,Text,Date,reply) values (%s,%s,%s,%s,%s)"
    # cursor.execute(sql, (dr_id, receiver_id, content, datetime.datetime.today().strftime('%Y-%m-%d'), reply))


def get_messages(cursor):
    sql = "select SenderID, ReceiverID, Text, Date FROM Messages where ReceiverID = %s OR SenderID = %s ORDER BY Date"
    cursor.execute(sql, (dr_id, dr_id))
    result = cursor.fetchall()
    return result


def prescribe_test(patient_id, cursor, db):
    sql = "insert into Test (DrID, patientID) values (%s,%s)"
    cursor.execute(sql, (dr_id, patient_id))
    db.commit()


def prescribe_drug(appointment_id, drug_name, cursor, db):
    sql = "select ID from Drugs where Name = %s"
    cursor.execute(sql, drug_name)
    drud_id = cursor.fetchall()
    sql2 = "insert into Prescription (AppointmentID, DrugID) values (%s,%s)"
    cursor.execute(sql2, (appointment_id, drud_id))
    db.commit()


def send_mail(email, msg):
    print(0)
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    print(1)
    server.starttls()
    print(2)
    server.login("holmes_sh98@yahoo.com", "H0lmesofPast")
    print(3)
    server.sendmail("holmes_sh98@yahoo.com", str(email), str(msg))
    print(4)
    server.quit()
