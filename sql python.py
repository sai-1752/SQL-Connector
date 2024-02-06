from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="bijd@2490",database="python")
if con:
    print("database is connected")
else:
    print("connection error")

def insert(Name,Age,City):
    res=con.cursor()
    sql="insert into users(Name,Age,City) values (%s,%s,%s)"
    user=(Name,Age,City)
    res.execute(sql,user)
    con.commit()
    print('data insert success')
def update(Name,Age,City,id):
    res=con.cursor()
    sql="update users set Name=%s,Age=%s,City=%s where id=%s"
    user=(Name,Age,City,id)
    res.execute(sql,user)
    con.commit()
    print("data update success")
def select():
    res=con.cursor()
    sql="select id,Name,Age,City from users"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["Name","Age","City"]))

def delete(id):
    res=con.cursor()
    sql="delete from users where id=%s"
    user=(id)
    res.execute(sql,user)
    con.commit()
    print("data deletion success")

while True:
    print("1.insert data")
    print("2.update data")
    print("3.select data")
    print("4.delete data")
    print("5.exit data")
    choice=int(input("enter the choice"))
    if choice==1:
        Name=input('enter the name: ')
        Age=input('enter the age: ')
        City=input('enter the city: ')
        insert(Name,Age,City)
    elif choice==2:
        id=input('enter the id: ')
        Name=input('enter the name: ')
        Age=input('enter the age: ')
        City=input('enter the city: ')
        update(Name,Age,City,id)
    elif choice==3:
        select()
    elif choice==4:
        id=input("enter id to delete: ")
    elif choice==5:
        quit()
    else:
        print("invalid session.please try again!")