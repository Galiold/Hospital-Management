import sys
import pymysql
import tkinter
import Secretary as s
import datetime

# ///////////////////////////////////// database connection \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
main_db = pymysql.connect(host="localhost",
                          user="root",
                          passwd="")

main_cursor = main_db.cursor()
main_cursor.execute("USE DB_Hospital")


# /////////////////////////////////////// Tools \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

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
    main_cursor.execute("SELECT * FROM Registrations WHERE username=%s", username)
    result = main_cursor.fetchone()
    if result[1] == 'd':
        main_cursor.execute("select increment from Doctors order by ID desc ")
        last_id = main_cursor.fetchone()
        if last_id is None :
            id = "d1"
        else:
            increment = int(last_id[0])+1
            id = 'd' + str(increment)
        sql = "insert into Doctors (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        val = (id,result[2],result[3],result[4],result[5])
        main_cursor.execute(sql, val)
        main_db.commit()
        main_cursor.execute("delete from Registrations where username = %s", username)
        main_db.commit()


# ////////////////////////////////// Login Functions  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def doctor_login(id):
    while True:
        name = "Arman"  # query to get the name
        print("------------- Doctors Panel ---------------")
        print('''
        1. complete your profile
        2. exit
        ''')
        choice = input()

        if int(choice)==1:
            print("please enter the following informations :")
            year = int(input('Enter a year'))
            month = int(input('Enter a month'))
            day = int(input('Enter a day'))
            date1 = datetime.date(year, month, day)

            Address= input("Address : ")
            PostalCode= input("PostalCode : ")
            DoB = date1
            sex = input("sex : ")
            height= input("height : ")
            weight = input("weight : ")

            main_cursor.execute("update Doctors set Address=%s , PostalCode=%s , DoB = %s , Sex=%s , Height=%s , Weight=%s where  ID = %s",(Address,PostalCode,DoB,sex,height,weight,id))
            main_db.commit()
        elif int(choice)==2:
            break

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
            main_cursor.execute(sql)
            result = main_cursor.fetchall()
            print(result)

            print("\n enter the Name that you want to approve or ZERO to exit")
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


# /////////////////////////////////// main program and menu \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
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
        add_row(main_cursor, "Registrations", instance_insert)
        main_db.commit()

    if int(choice) == 2:
        print("enter id")
        username = input()
        print("enter password")
        password = input()



        if username == "admin" and password == "admin":
            manager_login()
        elif username[0] == "d":
            sql = " select * from Doctors where ID= %s and Password = %s"
            val = (username, password,)
            print(val)
            res = main_cursor.execute(sql, val)
            if res==0 :
                print("id or password is not correct !")
            else:
                doctor_login(username)

        elif username[0] == "n" :
            sql = " select * from Nurses where ID= %s and Password = %s"
            val = (username, password)
            res = main_cursor.execute(sql, val)
            if res == 0:
                print("id or password is not correct !")
            else:
                nurse_login()

        elif username[0] == "p":
            sql = " select * from Patients where ID= %s and Password = %s"
            val = (username, password)
            res = main_cursor.execute(sql, val)
            if res == 0:
                print("id or password is not correct !")
            else:
                patient_login()

        elif username[0] == "l" :
            sql = " select * from Laboratory where ID= %s and Password = %s"
            val = ( username, password)
            res = main_cursor.execute(sql, val)
            if res == 0:
                print("id or password is not correct !")
            else:
                laboratory_login()

        elif username[0] == "h" :
            sql = " select * from Pharmacy where ID= %s and Password = %s"
            val = (username, password)
            res = main_cursor.execute(sql, val)
            if res == 0:
                print("id or password is not correct !")
            else:
                pharmacy_login()

        elif username[0] == "a":
            sql = " select * from Accountant where ID= %s and Password = %s"
            val = (username, password)
            res = main_cursor.execute(sql, val)
            if res == 0:
                print("id or password is not correct !")
            else:
                accountant_login()

        elif username[0] =="r":
            sql = " select * from Reception where ID= %s and Password = %s"
            val = (username, password)
            res = main_cursor.execute(sql, val)
            if res == 0:
                print("id or password is not correct !")
            else:
                reception_login()


main_db.close()
