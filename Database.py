import pymysql
import tkinter
import Secretary as s
db = pymysql.connect(host="localhost",
                     user="root",
                     passwd="")

cursor = db.cursor()

cursor.execute("USE Hospital")

db.close()