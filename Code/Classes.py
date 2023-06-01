#Imports Begin
import mysql.connector
#Imports End

#Classes Begin
class DataBase:
    def __init__(self, host:str, user:str, passwd:str, name:str, connector ):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.name = name
        self.connector = mysql.connector.connect(host = self.host, user = self.user, passwd = self.passwd, database = self.name)
    def cursorCreate(connector):
        return connector.cursor()
    def dbcommit(connector):
        return connector.commit()

class People:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        print("User Created")
    def insertInfo(name:str, age:int, db):
        cursor = db.cursor()
        sql = "INSERT INTO tb_01 (name,age) VALUES ( %s, %s)"
        cursor.execute(sql, (name, age))
        db.commit()
        return (print("Data commited to DB !"))
    
    #People End

#Classes End

#Vars Begin
db_01 = DataBase
db_01.__init__(self = db_01, host="localhost",user="root",passwd="2dHHetKQ4cFDkr",name="db_1", connector=db_01)
db_cursor = db_01.cursorCreate(db_01.connector)
sql_use = "USE db_01"

#Vars End

#Program Begin

#Program End