import datetime
import pymysql


# ///////////////////////////////////// database connection \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# ----------------------- ++ main ++ -----------------------------
def database_admin():
    db = pymysql.connect(host="localhost",
                         user="root",
                         passwd="")

    cursor = db.cursor()
    cursor.execute("USE DB_Hospital")
    return db


# ----------------------- ++ doctor ++ -----------------------------

def database_doctor():
    db = pymysql.connect(host="localhost",
                         user="root",
                         passwd="")
    cursor = db.cursor()
    cursor.execute("USE DB_Hospital")
    return db


# ----------------------- ++ doctor ++ -----------------------------

def database_patient():
    db = pymysql.connect(host="localhost",
                         user="root",
                         passwd="")
    cursor = db.cursor()
    cursor.execute("USE DB_Hospital")
    return db


# ----------------------- ++ doctor ++ -----------------------------

def database_accountant():
    db = pymysql.connect(host="localhost",
                         user="root",
                         passwd="")
    cursor = db.cursor()
    cursor.execute("USE DB_Hospital")
    return db


# ----------------------- ++ doctor ++ -----------------------------

def database_receptionist():
    db = pymysql.connect(host="localhost",
                         user="root",
                         passwd="")
    cursor = db.cursor()
    cursor.execute("USE DB_Hospital")
    return db


# ----------------------- ++ doctor ++ -----------------------------

def database_laboratory():
    db = pymysql.connect(host="localhost",
                         user="root",
                         passwd="")
    cursor = db.cursor()
    cursor.execute("USE DB_Hospital")
    return db


# ----------------------- ++ doctor ++ -----------------------------

def database_accountant():
    db = pymysql.connect(host="localhost",
                         user="root",
                         passwd="")
    cursor = db.cursor()
    cursor.execute("USE DB_Hospital")
    return db


# ----------------------- ++ doctor ++ -----------------------------

def database_nurse():
    db = pymysql.connect(host="localhost",
                         user="root",
                         passwd="")
    cursor = db.cursor()
    cursor.execute("USE DB_Hospital")
    return db


def profile_update(id, ui, cursor, db):
    # print("please enter the following informations :")
    # year = int(input('Enter a year'))
    # month = int(input('Enter a month'))
    # day = int(input('Enter a day'))
    # date1 = datetime.date(year, month, day)
    #
    # Address = input("Address : ")
    # PostalCode = input("PostalCode : ")
    # DoB = date1
    # sex = input("sex : ")
    # height = input("height : ")
    # weight = input("weight : ")

    date_of_birth = ui.edit_dob.toPlainText()
    address = ui.edit_address.toPlainText()
    zipcode = ui.edit_zipcode.toPlainText()
    sex = ui.edit_sex.toPlainText()
    height = ui.edit_height.toPlainText()
    weight = ui.edit_weight.toPlainText()

    if id[0] == 'd':
        table = "Doctors"
    elif id[0] == 'p':
        table = "Patients"
    elif id[0] == 'l':
        table = "Laboratory"
    elif id[0] == 'h':
        table = "Pharmacy"
    # elif id[0] == 'n':
    #     table = "Nurses"
    elif id[0] == 'r':
        table = "Reception"
    elif id[0] == 'a':
        table = "Accountant"

    sql = "update %s" % table
    sql = sql + " set Address=%s , PostalCode=%s , DoB = %s , Sex=%s , Height=%s , Weight=%s where  ID = %s"
    cursor.execute(sql, (address, zipcode, date_of_birth, sex, height, weight, id))
    db.commit()
