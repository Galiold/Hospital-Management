import pymysql

# doctor_db = pymysql.connect(host="localhost",
#                             user="root",
#                             passwd="Serv3rforDB")
#
# doctor_cursor = doctor_db.cursor()
# doctor_cursor.execute("USE DB_Hospital")


# def show_doctor_menu():
#     print("=========== Doctor Menu ============")
#     print("1.\tSee appointments")
#     print("2.\tCancel appointment")
#     print("3.\tShow patient's drug usage history")
#
#     choice = input()
#
#     if int(choice) == 1:
#         show_appointments()
#     elif int(choice) == 2:
#         cancel_appointment()
#     elif int(choice) == 3:
#         show_drug_usage_history()


def show_appointments(cursor):
    cursor.execute("SELECT * FROM Appointments")
    print("ID\tPatient ID\tTime\tDr ID\tStatus")
    print("--------------------------------------------------")
    for appointment in cursor.fetchall():
        print(appointment[4], appointment[0], appointment[1], appointment[2], appointment[3], sep="\t|\t")
        print("--------------------------------------------------")


def cancel_appointment(cursor, db):
    print("Enter the appointmet's ID:")
    appointment_id = input()
    cursor.execute("DELETE FROM Appointments WHERE Appointments.ID = %s", int(appointment_id))
    db.commit()
    # send email to the patient


def show_drug_usage_history(cursor):
    print("Enter the patient's ID:")
    patient_id = input()
    cursor.execute("SELECT DISTINCT Drugs.Name FROM Prescription, Drugs WHERE Prescription.DrugID = Drugs.ID AND"
                          " Prescription.AppointmentID = (SELECT ID FROM Appointments WHERE PatientID = %s)",
                          patient_id)
    for drug in cursor.fetchall():
        print(drug[0])


def send_private_message():
    pass
