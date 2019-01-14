import sys
import pymysql
import tkinter
import Secretary as s

db = pymysql.connect(host="localhost",
                     user="root",
                     passwd="")

cursor = db.cursor()
cursor.execute("USE DB_Hospital")


# /////////////////////////////////////// Tools \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def add_row(cursor, tablename, rowdict):
    # XXX tablename not sanitized
    # XXX test for allowed keys is case-sensitive

    # filter out keys that are not column names
    cursor.execute("describe %s" % tablename)
    allowed_keys = set(row[0] for row in cursor.fetchall())
    keys = allowed_keys.intersection(rowdict)

    # if len(rowdict) > len(keys):
    #     unknown_keys = set(rowdict) - allowed_keys
    #     print >> sys.stderr, "skipping keys:", ", ".join(unknown_keys)

    columns = ", ".join(keys)
    values_template = ", ".join(["%s"] * len(keys))

    sql = "insert into %s (%s) values (%s)" % (
        tablename, columns, values_template)
    values = tuple(rowdict[key] for key in keys)
    cursor.execute(sql, values)


# ////////////////////////////////// Manager Functions \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def approve(username):
    cursor.execute("SELECT * FROM Registrations WHERE username=%s", username)
    result = cursor.fetchone()
    if result[1] == 'd':
        cursor.execute("select ID from Doctors order by ID desc ")
        last_id = cursor.fetchone()
        id = 'd'+last_id[0]
        sql = "insert into Doctors (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        val = (id,result[2],result[3],result[4],result[5])
        cursor.execute(sql,val)


# ////////////////////////////////// Login Functions  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def doctor_login():
    name = "Arman"  # query to get the name
    print("------------- Doctors Panel ---------------")
    print("welcome dr.%s" % (name,))


def manager_login():
    while True:
        name = "Arman"  # query to get the name
        print("------------- Managers Panel ---------------")
        print("welcome %s \n" % (name,))
        print('''
        1. list of unapproved registrations
        2.exit
        ''')
        choice = input()

        if int(choice) == 1:
            sql = "SELECT email,phone,username FROM Registrations"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)

            print("\n enter the Username that you want to approve or ZERO to exit")
            username = input()
            approve(username)
        elif int(choice) == 2:
            break

def nurse_login():
    print()

def patient_login():
    print()

def laboratory_login():
    print()

def pharmacy_login():
    print()

def accountant_login():
    print()

def reception_login():
    print()

while True:

    print("----- Menu -----")
    print('''
    1. registration
    2. login
    ''')

    choice = input()

    if int(choice) == 1:
        print("enter in the following order : role - email - phone - username - password")
        print('''
        Roles :
        Doctor ---> d
        Nurse  ---> n
        Patient---> p
        Lab    ---> l
        Pharmacy ---> ph
        Accountant ---> a
        Reception ---> r
        ''')
        instance_insert = {
            # sql column    variable value
            'role': input(),
            'email': input(),
            'phone': input(),
            'username': input(),
            'password': input(),
        }
        add_row(cursor, "Registrations", instance_insert)
        db.commit()

    if int(choice) == 2:
        print("enter id")
        username = input()
        print("enter password")
        password = input()

        val = ["Nurses" ,username, password,]
        sql = " select * from %s where ID= %s and Password = %s"

        if username == "admin" and password == "admin":
            manager_login()
        elif username[0] == "d":
            val[0]="Doctors"
            res = cursor.execute(sql, val)
            if res==0 :
                print("id or password is not correct !")
            else:
                doctor_login()
        elif username[0] == "n" :
            val[0] = "Nurses"
            res = cursor.execute(sql, val)
            if res == 0:
                print("id or password is not correct !")
            else:
                nurse_login()
        elif username[0] == "p":
            val[0] = "Patients"
            res = cursor.execute(sql, val)
            if res == 0:
                print("id or password is not correct !")
            else:
                patient_login()
        elif username[0] == "l" :
            val[0] = "Laboratory"
            res = cursor.execute(sql, val)
            if res == 0:
                print("id or password is not correct !")
            else:
                laboratory_login()
        elif username[0] == "h" :
            val[0] = "Pharmacy"
            res = cursor.execute(sql, val)
            if res == 0:
                print("id or password is not correct !")
            else:
                pharmacy_login()
        elif username[0] == "a":
            val[0] = "Accountant"
            res = cursor.execute(sql, val)
            if res == 0:
                print("id or password is not correct !")
            else:
                accountant_login()
        elif username[0] =="r":
            val[0] = "Reception"
            res = cursor.execute(sql, val)
            if res == 0:
                print("id or password is not correct !")
            else:
                reception_login()




        else:
            if res == 0:
                print("Username or password is not correct")
            else:
                doctor_login()

db.close()
