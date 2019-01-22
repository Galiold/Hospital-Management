import sys
import pymysql
import tkinter
# import Secretary as s
import datetime
import smtplib
import doctor
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# ///////////////////////////////////// database connection \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# ----------------------- ++ main ++ -----------------------------

# main_db = pymysql.connect(host="159.89.45.112",
#                           user="root",
#                           passwd="cb3eac4fa4776281fd60e9ab3d34cc2ac32b327e38ffa77c")

# main_db = pymysql.connect(host="localhost",
#                           user="root",
#                           passwd="Serv3rforDB")
#
# main_cursor = main_db.cursor()
# main_cursor.execute("USE DB_Hospital")
#
#
# # ----------------------- ++ doctor ++ -----------------------------
# def database_doctor():
#     doctor_db = pymysql.connect(host="localhost",
#                                 user="root",
#                                 passwd="Serv3rforDB")
#     doctor_cursor = doctor_db.cursor()
#     doctor_cursor.execute("USE DB_Hospital")
#     return doctor_db
#

# /////////////////////////////////////// Tools \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# def add_row(cursor, tablename, rowdict):
#     # XXX tablename not sanitized
#     # XXX test for allowed keys is case-sensitive
#
#     # filter out keys that are not column names
#     cursor.execute("describe %s" % tablename)
#     allowed_keys = set(row[0] for row in cursor.fetchall())
#     keys = allowed_keys.intersection(rowdict)
#
#     # if len(rowdict) > len(keys):
#     #     unknown_keys = set(rowdict) - allowed_keys
#     #     print >> sys.stderr, "skipping keys:", ", ".join(unknown_keys)
#
#     columns = ", ".join(keys)
#     values_template = ", ".join(["%s"] * len(keys))
#
#     sql = "insert into %s (%s) values (%s)" % (
#         tablename, columns, values_template)
#     values = tuple(rowdict[key] for key in keys)
#     cursor.execute(sql, values)


def profile_update(table, id):
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

    sql = "update %s" % (table)
    sql = sql + " set Address=%s , PostalCode=%s , DoB = %s , Sex=%s , Height=%s , Weight=%s where  ID = %s"
    main_cursor.execute(sql, (Address, PostalCode, DoB, sex, height, weight, id))
    main_db.commit()


# # def register():
# #     print("enter in the following order : role - email - phone - username - password")
# #     print('''
# #             Roles :
# #             Doctor ---> d
# #             Nurse  ---> n
# #             Patient---> p
# #             Lab    ---> l
# #             Pharmacy ---> ph
# #             Accountant ---> a
# #             Reception ---> r
# #             ''')
# #     instance_insert = {
# #         # sql column    variable value
# #         'role': input(),
# #         'email': input(),
# #         'phone': input(),
# #         'username': input(),
# #         'password': input(),
#     }
#     add_row(main_cursor, "Registrations", instance_insert)
#     main_db.commit()
#     return instance_insert["email"]


def send_mail(id: object, password: object) -> object:
    print(0)
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    print(1)
    server.starttls()
    print(2)
    server.login("holmes_sh98@yahoo.com", "H0lmesofPast")
    print(3)
    msg = "\n YOUR id is %s and your password is : %s ! \n" % (id, password)
    server.sendmail("holmes_sh98@yahoo.com", "goldani.ali@aol.com", msg)
    print(4)
    server.quit()

    # HTML Mail
#     sender = "holmes_sh98@yahoo.com"
#     receiver = "goldani.ali@aol.com"
#
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = "Registration Confirmed!"
#     msg['From'] = sender
#     msg['To'] = receiver
#
#     msg.preamble = "Your id is ", id, "and your password is:", password, " !"
#     html = """/
#     <head>
#     <style>
#         .dialog{
#             width: 500px;
#             height: 200px;
#             background-color: darkblue;
#             border-radius: 10px;
#             box-shadow: 5px 5px  20px gray, -5px -5px 20px gray;
#             margin: auto;
#             position: absolute;
#             top: 50%;
#             left: 50%;
#             margin-right: -50%;
#             transform: translate(-50%, -50%);
#             padding: 0px;
#         }
#         .dialog p{
#             font-family: Futura;
#             color: white;
#             position: absolute;
#             top: 45%;
#             left: 50%;
#             margin-right: -50%;
#             transform: translate(-50%, -50%)
#         }
#     </style>
# </head>
# <body>
#     <div class="dialog">
#         <p align="center">Your id is<br><id>id</id><br>and your password is<br><passwword>password</passwword></p>
#     </div>
# </body>
# </html>
#     """
#
#     html_body = MIMEText(html, 'html')
#
#     msg.attach(html_body)
#
#     print(0)
#     server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
#     print(1)
#     server.starttls()
#     print(2)
#     server.login("holmes_sh98@yahoo.com", "H0lmesofPast")
#     print(3)
#     server.sendmail(sender, [receiver], msg.as_string())
#     print(4)
#     server.quit()


# ////////////////////////////////// approvals \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def approve_doctor(sql, result):
    main_cursor.execute("select increment from Doctors order by ID desc ")
    last_id = main_cursor.fetchone()
    if last_id is None:
        id = "d1"
    else:
        increment = int(last_id[0]) + 1
        id = 'd' + str(increment)
    send_mail(id, result[3])
    val = (id, result[2], result[3], result[4], result[5])
    main_cursor.execute(sql, val)
    main_db.commit()
    main_cursor.execute("delete from Registrations where username = %s", username)
    main_db.commit()


def approve_nurse(sql, result):
    main_cursor.execute("select increment from Nurses order by ID desc ")
    last_id = main_cursor.fetchone()
    if last_id is None:
        id = "n1"
    else:
        increment = int(last_id[0]) + 1
        id = 'n' + str(increment)
    val = (id, result[2], result[3], result[4], result[5])
    main_cursor.execute(sql, val)
    main_db.commit()
    main_cursor.execute("delete from Registrations where username = %s", username)
    main_db.commit()


def approve_patient(sql, result):
    main_cursor.execute("select increment from Patients order by ID desc ")
    last_id = main_cursor.fetchone()
    if last_id is None:
        id = "p1"
    else:
        increment = int(last_id[0]) + 1
        id = 'p' + str(increment)
    val = (id, result[2], result[3], result[4], result[5])
    main_cursor.execute(sql, val)
    main_db.commit()
    main_cursor.execute("delete from Registrations where username = %s", username)
    main_db.commit()


def approve_laboratory(sql, result):
    main_cursor.execute("select increment from Laboratory order by ID desc ")
    last_id = main_cursor.fetchone()
    if last_id is None:
        id = "l1"
    else:
        increment = int(last_id[0]) + 1
        id = 'l' + str(increment)
    val = (id, result[2], result[3], result[4], result[5])
    main_cursor.execute(sql, val)
    main_db.commit()
    main_cursor.execute("delete from Registrations where username = %s", username)
    main_db.commit()


def approve_pharmacy(sql, result):
    main_cursor.execute("select increment from Pharmacy order by ID desc ")
    last_id = main_cursor.fetchone()
    if last_id is None:
        id = "h1"
    else:
        increment = int(last_id[0]) + 1
        id = 'h' + str(increment)
    val = (id, result[2], result[3], result[4], result[5])
    main_cursor.execute(sql, val)
    main_db.commit()
    main_cursor.execute("delete from Registrations where username = %s", username)
    main_db.commit()


def approve_accountant(sql, result):
    main_cursor.execute("select increment from Accountant order by ID desc ")
    last_id = main_cursor.fetchone()
    if last_id is None:
        id = "a1"
    else:
        increment = int(last_id[0]) + 1
        id = 'a' + str(increment)
    val = (id, result[2], result[3], result[4], result[5])
    main_cursor.execute(sql, val)
    main_db.commit()
    main_cursor.execute("delete from Registrations where username = %s", username)
    main_db.commit()


def approve_reception(sql, result):
    main_cursor.execute("select increment from Reception order by ID desc ")
    last_id = main_cursor.fetchone()
    if last_id is None:
        id = "r1"
    else:
        increment = int(last_id[0]) + 1
        id = 'r' + str(increment)
    val = (id, result[2], result[3], result[4], result[5])
    main_cursor.execute(sql, val)
    main_db.commit()
    main_cursor.execute("delete from Registrations where username = %s", username)
    main_db.commit()


# ////////////////////////////////// Manager Functions \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def approve(email):
    main_cursor.execute("SELECT * FROM Registrations WHERE email=%s", email)
    result = main_cursor.fetchone()

    if result[1] == 'd':
        sql = "insert into Doctors (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        approve_doctor(sql, result)
    elif result[1] == "n":
        sql = "insert into Nurses (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        approve_nurse(sql, result)
    elif result[1] == "p":
        sql = "insert into Patients (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        approve_patient(sql, result)

    elif result[1] == "l":
        sql = "insert into Laboratory (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        approve_laboratory(sql, result)

    elif result[1] == "h":
        sql = "insert into Pharmacy (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        approve_pharmacy(sql, result)

    elif result[1] == "a":
        sql = "insert into Accountant (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        approve_accountant(sql, result)

    elif result[1] == "r":
        sql = "insert into Reception (ID,Email,Phone,Username,Password) values (%s,%s,%s,%s,%s)"
        approve_reception(sql, result)


# ////////////////////////////////// Login Functions  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def manager_login():
    while True:
        name = "Arman"  # query to get the name
        print("------------- Managers Panel ---------------")
        print("welcome %s \n" % (name,))
        print('''
        1. list of unapproved registrations
        2, create account for other users
        3.exit
        ''')
        choice = input()

        if int(choice) == 1:
            sql = "SELECT email,phone,username FROM Registrations"
            main_cursor.execute(sql)
            result = main_cursor.fetchall()
            print(result)

            print("\n enter the email that you want to approve or ZERO to exit")
            email = input()
            approve(email)
        elif int(choice) == 2:
            email = register()
            approve(email)
        elif int(choice) == 3:
            break


def doctor_login(id):
    doctor_db = database_doctor()
    doctor_cursor = doctor_db.cursor()

    while True:
        print("------------- Doctor Panel ---------------")
        print('''
        1. See appointments
        2. Cancel appointment
        3. Show patient's drug usage history
        4. change/complete your profile info
        5. exit
        ''')
        choice = input()

        if int(choice) == 1:
            doctor.show_appointments(doctor_cursor, id)
        elif int(choice) == 2:
            doctor.cancel_appointment(doctor_cursor, doctor_db)
        elif int(choice) == 3:
            doctor.show_drug_usage_history(doctor_cursor)
        if int(choice) == 4:
            profile_update("Doctors", id)
        elif int(choice) == 5:
            break


def nurse_login():
    while True:
        print("------------- Nurse Panel ---------------")
        print('''
        1. change/complete your profile info
        2. exit
        ''')
        choice = input()

        if int(choice) == 1:
            profile_update("Doctors", id)
        elif int(choice) == 2:
            break


def patient_login():
    while True:
        name = "Arman"  # query to get the name
        print("------------- Patient Panel ---------------")
        print('''
        1. change/complete your profile info
        2. exit
        ''')
        choice = input()

        if int(choice) == 1:
            profile_update("Doctors", id)
        elif int(choice) == 2:
            break


def laboratory_login():
    while True:
        name = "Arman"  # query to get the name
        print("------------- Laboratory Panel ---------------")
        print('''
        1. change/complete your profile info
        2. exit
        ''')
        choice = input()

        if int(choice) == 1:
            profile_update("Doctors", id)
        elif int(choice) == 2:
            break


def pharmacy_login():
    while True:
        name = "Arman"  # query to get the name
        print("------------- Pharmacy Panel ---------------")
        print('''
        1. change/complete your profile info
        2. exit
        ''')
        choice = input()

        if int(choice) == 1:
            profile_update("Doctors", id)
        elif int(choice) == 2:
            break


def accountant_login():
    while True:
        name = "Arman"  # query to get the name
        print("------------- Accountant Panel ---------------")
        print('''
        1. change/complete your profile info
        2. exit
        ''')
        choice = input()

        if int(choice) == 1:
            profile_update("Doctors", id)
        elif int(choice) == 2:
            break


def reception_login():
    while True:
        name = "Arman"  # query to get the name
        print("------------- Reception Panel ---------------")
        print('''
        1. change/complete your profile info
        2. exit
        ''')
        choice = input()

        if int(choice) == 1:
            profile_update("Doctors", id)
        elif int(choice) == 2:
            break


# /////////////////////////////////// main program and menu \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
while True:

    print("----- Menu -----")
    print('''
    1. registration
    2. login
    3. exit
    ''')

    choice = input()

    if int(choice) == 1:
        register()

    elif int(choice) == 2:
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
            if res == 0:
                print("id or password is not correct !")
            else:
                doctor_login(username)

        elif username[0] == "n":
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

        elif username[0] == "l":
            sql = " select * from Laboratory where ID= %s and Password = %s"
            val = (username, password)
            res = main_cursor.execute(sql, val)
            if res == 0:
                print("id or password is not correct !")
            else:
                laboratory_login()

        elif username[0] == "h":
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

        elif username[0] == "r":
            sql = " select * from Reception where ID= %s and Password = %s"
            val = (username, password)
            res = main_cursor.execute(sql, val)
            if res == 0:
                print("id or password is not correct !")
            else:
                reception_login()

    if int(choice) == 3:
        main_db.close()
        exit()
