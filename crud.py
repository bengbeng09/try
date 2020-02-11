from tkinter import *
import tkinter.messagebox as MessageBox 
import pyodbc
from datetime import datetime

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=COMPLAB503_PC14;'
                      'Database=db_clothing_line;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

def clear():
    e_name.delete(first=0,last=22)
    e_qty.delete(first=0,last=22)
    e_price.delete(first=0,last=22)

def insert():
    name = e_name.get()
    price = e_price.get()
    qty = e_qty.get()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if(name == "" or price == "" or qty == ""):
        MessageBox.showinfo("Insert Status", "All fields are required")
    else:
        cursor.execute("insert into dbo.Products2 (name, price, quantity,timestamp) values('"+name+"','"+price+"','"+qty+"','"+timestamp+"' )")
        cursor.execute("commit")
        clear()
        MessageBox.showinfo("Insert Status", "Inserted Succesfully")
        cursor.close()

def delete():
    name = e_name.get()
    if(name == ""):
        MessageBox.showinfo("Delete Status", "Name field is empty")
    else:
        cursor.execute("delete from dbo.Products2 where name = '"+name+"'")
        cursor.execute("commit")
        clear()
        MessageBox.showinfo("Delete Status", "Sucessfully Deleted")
        cursor.close()

def update():
    name = e_name.get()
    price = e_price.get()
    qty = e_qty.get()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if(name == ""):
        MessageBox.showinfo("Update Status", "Name field is empty")
    else:
        cursor.execute("update dbo.Products2 SET name = '"+name+"', price = '"+price+"', quantity = '"+qty+"', timestamp = '"+timestamp+"' WHERE name = '"+name+"'")
        cursor.execute("commit")
        clear()
        MessageBox.showinfo("Update Status", "Sucessfully Deleted")
        cursor.close()

def find():
    name = e_name.get()
    if(name == ""):
        MessageBox.showinfo("Find Status", "Name field is empty")
    else:
        cursor.execute("select from ")
        cursor.execute("commit")
        clear()
        MessageBox.showinfo("Insert Status", "Sucessfully Deleted")
        cursor.close()


crud = Tk()
crud.geometry("800x500")
crud.title("Inventory System")

name = Label(crud, text = 'Product Name', font = ("bold", 10))
name.place(x=20, y=30)
qty = Label(crud, text = 'Quantity', font = ("bold", 10))
qty.place(x=20, y=60)
price = Label(crud, text = 'Price', font = ("bold", 10))
price.place(x=20, y=90)

e_name = Entry()
e_name.place(x = 150, y = 30)

e_qty = Entry()
e_qty.place(x = 150, y = 60)

e_price = Entry()
e_price.place(x = 150, y = 90)

insert = Button(crud, text = "insert", font = ("italic", 10), bg = "white", command = insert)
insert.place(x = 20, y = 140)

delete = Button(crud, text = "delete", font = ("italic", 10), bg = "white", command = delete)
delete.place(x = 70, y = 140)

update = Button(crud, text = "update", font = ("italic", 10), bg = "white", command = update)
update.place(x = 130, y = 140)

find = Button(crud, text = "find", font = ("italic", 10), bg = "white" )
find.place(x = 190, y = 140)

crud.mainloop()

