import datetime


def edit_drugs(cursor):
    print('''
    1. search by drug id
    2. search by drug name
    3. back
    ''')
    choice = int(input())

    if choice == 1:
        result = search_by_id(cursor)
    elif choice == 2:
        result = search_by_name(cursor)
    elif choice == 3:
        return
    edit(cursor, result)


def edit(cursor, result):
    print(len(result))


def search_by_id(cursor):
    print("please enter drug id")
    id = input()

    sql = "select * from Drugs where ID = %s"
    res = cursor.execute(sql, int(id))

    if res == 0:
        print("not found !")
        return
    result = cursor.fetchall()
    print(result)
    return result


def search_by_name(cursor):
    print("please enter drug name")
    name = input()

    sql = "select * from Drugs where Name = %s"
    res = cursor.execute(sql, name)

    if res == 0:
        print("not found !")
        return
    result = cursor.fetchall()
    print(result)
    return result


def filter(cursor):
    print("drugs that are not epired")
    sql = "select * from Drugs WHERE ExpirationDate > %s "
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    cursor.execute(sql, date)
    result = cursor.fetchall()
    return result


def process_prescription(cursor, prescription_id):
    sql = "SELECT Name FROM (SELECT DrugID FROM Prescription WHERE AppointmentID = %s) as A inner JOIN Drugs as B ON A.DrugID = B.ID"
    cursor.execute(sql, prescription_id)
    return cursor.fetchall()


def delete_drug(drugName, cursor, db):
    sql = "delete from Drugs where Name= %s "
    cursor.execute(sql, drugName)
    db.commit()


def add_drug(drugName, expDate, cursor, db):
    sql = "insert into Drugs (Name,ExpirationDate) values (%s,%s)"
    cursor.execute(sql, (drugName, expDate))
    db.commit()
