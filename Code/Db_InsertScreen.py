#Imports Begin #
import mysql.connector
from Classes import People, DataBase
from tkinter import *
from Db_ClearScreen import dbClearScreen
import tkinter as tk
#Imports End #

#Vars Begin#
root= tk.Tk()
db_01 = DataBase
db_01.__init__(self = db_01, host="localhost",user="root",passwd="password",name="db_1", connector=db_01)
db_cursor = db_01.cursorCreate(db_01.connector)
sql_use = "USE db_01"
ids = 0
#Vars End#

#Functions Start#
def db_insert(e1:str,e2:int, cursor):
   pep = People
   pep.__init__(pep, e2, e1)
   pep.insertInfo(pep.name, pep.age, db_01.connector)
   clear_fields()

def db_clear():
   root.destroy()
   dbClearScreen()
   

def clear_fields ():
   entry2.delete(0,END)
   entry3.delete(0,END)
#Functions End#

#Program Start#
root.geometry('1080x216')
root.title="Database Insert"
root.update()
windowx = root.winfo_width()
windowy = root.winfo_height()
title = tk.Label(root, text="Welcome to Database Management")
title.place(x= (windowx / 2) - 40, y= windowy / 20)
l2 = tk.Label(root, text="Age:",)
l2.place(x=windowx - (windowx - 20) ,y=(windowy / 4))
l3 = tk.Label(root, text="Name:")
l3.place(x=windowx - (windowx - 20),y=(windowy / 2.5))
root.update()
entry2 = tk.Entry(root, width=int(windowx/6.6) + 3)
entry2.place(x=(l2.winfo_x() * 4), y=((l2.winfo_y()) + 2))
entry3 = tk.Entry(root, width=int(windowx/6.6) + 3)
entry3.place(x=(int(l3.winfo_x()) * 4), y=(l3.winfo_y() + 2))
root.update()
button1 = tk.Button(text='Insert To DB',width="{}".format(int(windowx/33)),command = lambda: db_insert(entry2.get(),entry3.get(),db_cursor))
button2 = tk.Button(text='Manage Data', width="{}".format(int(windowx/33)), command = lambda: db_clear())
button3 = tk.Button(text='Cancel Operation', width="{}".format(int(windowx/33)), command = lambda: clear_fields())
button1.place(x=(windowx - windowx) + 15, y=windowy /1.5 )
button1.update()
button2.place(x=(button1.winfo_x()+button1.winfo_width()) * 1.5 , y=windowy /1.5)
button3.place(x=(button1.winfo_x()+button1.winfo_width()) * 3 , y=windowy /1.5)
root.mainloop()
#Program End#