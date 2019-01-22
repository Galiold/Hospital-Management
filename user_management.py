import pymysql


# ///////////////////////////////////// database connection \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# ----------------------- ++ main ++ -----------------------------
def database_admin():
    admin_db = pymysql.connect(host="localhost",
                               user="root",
                               passwd="Serv3rforDB")

    admin_cursor = admin_db.cursor()
    admin_cursor.execute("USE DB_Hospital")
    return admin_db


# ----------------------- ++ doctor ++ -----------------------------


def database_doctor():
    doctor_db = pymysql.connect(host="localhost",
                                user="root",
                                passwd="Serv3rforDB")
    doctor_cursor = doctor_db.cursor()
    doctor_cursor.execute("USE DB_Hospital")
    return doctor_db
