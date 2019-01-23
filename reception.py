import user_management

# reception_db = user_management.database_admin()
# reception_cursor = reception_db.cursor()


def delete_free_time(appointmentID, cursor, db):
    sql = "delete from Appointments where AppointmentID = %s"
    cursor.execute(sql, appointmentID)
    db.commit()


def delete_apponitment(appointmentID, cursor, db):
    sql = "update Appointments set PatientID = NULL where AppointmentID = %s"
    cursor.execute(sql, appointmentID)
    db.commit()


def add_free_time(time, DrID, cursor, db):
    sql = "insert into Appointments (Time , DrID) values (%s,%s)"
    cursor.execute(sql, (time, DrID))
    db.commit()
