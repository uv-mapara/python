import sqlite3

def connection():
    x=sqlite3.connect('data.db')
    return x

def table(x):
    x.execute('''CREATE TABLE STUDENT1(NAME TEXT,ROLLNUMBER int)''')
    
def insert(x):
    x.execute("insert into STUDENT1(NAME,ROLLNUMBER) values('UV',3197)")
    
obj=connection()
table(obj)
insert(obj)
obj.commit()
obj.close()
