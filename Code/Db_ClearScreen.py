#Import Begin#
from tkinter import *
import tkinter as tk
from tkinter.font import Font
from Classes import DataBase
import numpy as np
#Import End#

#Program Start (Used on a function)#
def dbClearScreen():
    #Vars Begin#
    root = tk.Tk()
    db_01 = DataBase
    db_01.__init__(self=db_01, host="localhost", user="root", passwd="password", name="db_1", connector=db_01)
    db_cursor = db_01.cursorCreate(db_01.connector)
    x = 9
    #Vars End#
    
    root.geometry("1080x1080")
    root.title("Database Controller")
    root.update()
    windowx = root.winfo_width()
    windowy = root.winfo_height()
    title = tk.Label(root, text="Check the information bellow and check any necessary changes")
    title.place(x=(windowx /3), y = (windowy / 25))
    label1 = tk.Label(text="Rows",font=("Consola",24))
    label2 = tk.Label(text="Id",font=("Consola",24))
    label3 = tk.Label(text="Age",font=("Consola",24))
    label4 = tk.Label(text="Name",font=("Consola",24))
    label1.place(x=(windowx / 10),y=(windowy / 4))
    label2.place(x=(windowx / 10) + 100,y=(windowy / 4))
    label3.place(x=(windowx / 10) + 150,y=(windowy / 4))
    label4.place(x=(windowx / 10) + 225,y=(windowy / 4))
    sql = "SELECT * FROM tb_01"
    db_cursor.execute(sql)
    var = db_cursor.fetchall() 
    v = np.empty(10, dtype=object)

    for row in var:
        v[x] =tk.Label(text=row, font=("Consola", 20))
        v[x].place(x=(windowx / 10),y=(windowy / x * 3))
        x -= 1

    root.mainloop()
#Program End#