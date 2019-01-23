import datetime
import pymysql


# ///////////////////////////////////// database connection \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# ----------------------- ++ main ++ -----------------------------
def database_admin():
    admin_db = pymysql.connect(host="localhost",
                               user="root",
                               passwd="")

    admin_cursor = admin_db.cursor()
    admin_cursor.execute("USE DB_Hospital")
    return admin_db


# ----------------------- ++ doctor ++ -----------------------------

def database_doctor():
    doctor_db = pymysql.connect(host="localhost",
                                user="root",
                                passwd="")
    doctor_cursor = doctor_db.cursor()
    doctor_cursor.execute("USE DB_Hospital")
    return doctor_db

# -------------------------------------------------------------------


def profile_update(table, id, cursor, db):
    print("please enter the following informations :")
    year = int(input('Enter a year'))
    month = int(input('Enter a month'))
    day = int(input('Enter a day'))
    date1 = datetime.date(year, month, day)

    Address = input("Address : ")
    PostalCode = input("PostalCode : ")
    DoB = date1
    sex = input("sex : ")
    height = input("height : ")
    weight = input("weight : ")

    sql = "update %s" % table
    sql = sql + " set Address=%s , PostalCode=%s , DoB = %s , Sex=%s , Height=%s , Weight=%s where  ID = %s"
    cursor.execute(sql, (Address, PostalCode, DoB, sex, height, weight, id))
    db.commit()
