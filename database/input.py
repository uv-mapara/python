import sqlite3

def connection():
    x=sqlite3.connect('data1.db')
    return x

def table(x):
    x.execute('''CREATE TABLE STUDENT(NAME TEXT,ROLLNUMBER int)''')
    
def insert(x):
    name=input("Enter name:")
    roll=int(input("Enter roll number:"))
    x.execute("insert into STUDENT(NAME,ROLLNUMBER) values(?,?)",(name,roll))
    
obj=connection()
table(obj)
insert(obj)
obj.commit()
obj.close()
