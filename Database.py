import pymysql
import tkinter

db = pymysql.connect(host="localhost",
                     user="root",
                     passwd="Serv3rforDB")

cursor = db.cursor()

cursor.execute("USE Q4_2")
cursor.execute("SELECT * FROM ComputerProduct")

for i in cursor.fetchall():
    print (i[0], i[1], i[2])

root = tkinter.Tk()

label = tkinter.Label(root, text="Hello World!", padx=10, pady=10)
label.pack(
)
root.mainloop()


db.close()