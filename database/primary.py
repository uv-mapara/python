import sqlite3

def connection():
    x=sqlite3.connect('data2.db')
    return x

def table(x):
    x.execute('''CREATE TABLE STUDENT(NAME TEXT,ROLLNUMBER int)''')
    
def insert(x):
    num=int(input("how many student:"))
    for i in range(num):
        name=input("Enter name:")
        roll=int(input("Enter roll number:"))
        x.execute("insert into STUDENT(NAME,ROLLNUMBER) values(?,?)",(name,roll))
    
obj=connection()
table(obj)
insert(obj)
obj.commit()
obj.close()