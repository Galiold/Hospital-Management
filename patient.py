import datetime

patient_id = None


def set_patient_id(id):
    global patient_id
    patient_id = id


def p_reserve_appointment(appointment_id, cursor, db):
    sql = "UPDATE Appointments SET PatientID = %s WHERE AppointmentID = %s"
    cursor.execute(sql, (patient_id, appointment_id))
    db.commit


def show_prescription(appointment_id, cursor):
    sql = "SELECT Name FROM(SELECT Appointments.AppointmentID,Appointments.DrID,Appointments.Time,T1.DrugID,T1.Name FROM (Appointments inner JOIN (select AppointmentID,DrugID,Name from Prescription inner JOIN Drugs ON Prescription.DrugID=Drugs.ID) AS T1 ON Appointments.AppointmentID = T1.AppointmentID) WHERE Appointments.PatientID = %s GROUP by T1.AppointmentID , T1.DrugID)AS T3 WHERE AppointmentID=%s"
    cursor.execute(sql, (patient_id, appointment_id))
    result = cursor.fetchall()
    return result


def get_messages(cursor):
    sql = "select SenderID, ReceiverID, Text, Date FROM Messages where ReceiverID = %s OR SenderID = %s ORDER BY Date"
    cursor.execute(sql, (patient_id, patient_id))
    result = cursor.fetchall()
    return result


def p_send_message(content, receiver_id, cursor, db):
    sql = "insert into Messages (SenderID,ReceiverID,Text,Date) values (%s,%s,%s,%s)"
    cursor.execute(sql, (patient_id, receiver_id, content, datetime.datetime.today().strftime('%Y-%m-%d')))
    db.commit()


def p_show_bed_info(cursor, db):
    db.commit()
    sql = "SELECT BedID FROM Beds WHERE PatientID = %s"
    cursor.execute(sql, patient_id)
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        return result
