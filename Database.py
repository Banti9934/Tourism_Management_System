"""
DATABASE NAME : Tourdemo
TABLES :user,Brochure,Bookrecord
"""
import mysql.connector
from datetime import date
def DatabaseCreate():
    cnx = mysql.connector.connect(user='root', password='banti', host='localhost')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE DATABASE IF NOT EXISTS Tourdemo")
    Cursor.execute("")
    Cursor.close()
    cnx.close()

def TablesCreate():
    cnx = mysql.connector.connect(user='root', password='banti', host='localhost', database='Tourdemo')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE TABLE IF NOT EXISTS User(Uname varchar(30), Umob bigint, Uaddress varchar(30), Ugml varchar(30) PRIMARY KEY, Upass varchar(10), Date_of_Regestration Date)")
    Cursor.execute("CREATE TABLE IF NOT EXISTS Brochure(SR int PRIMARY KEY,CODE varchar(2),PLACE varchar(50),CHARGES bigint)")
    Cursor.execute("CREATE TABLE IF NOT EXISTS Bookrecord(Bname varchar(30), Bmob bigint,Bcode varchar(2),Bplace varchar(50),Bcharges int, Do_booking Date,Bno_booking int,Btotal float)")
    Cursor.close()
    cnx.close()

def Insert():
     cnx = mysql.connector.connect(user='root', password='banti', host='localhost', database='Tourdemo')
     Cursor = cnx.cursor()
     Cursor.execute("select count(*) from Brochure")
     k=(list(Cursor))
     for i in k:
         m=(i[0])
     if m==0:
         Cursor.execute("insert into Brochure values(1,'AA','Bihar Tourism Pack',10000)")
         Cursor.execute("insert into Brochure values(2,'BB','Uttar Pradesh Pack',10000)")
         Cursor.execute("insert into Brochure values(3,'CC','J&K and Ladakh Pack',15000)")
         Cursor.execute("insert into Brochure values(4,'DD','Gujrat Tourism Pack',16000)")
         Cursor.execute("insert into Brochure values(5,'EE','Madhya Pradesh Pack',12000)")
         Cursor.execute("insert into Brochure values(6,'FF','Ooty Tourism pack',13000)")
         Cursor.execute("insert into Brochure values(7,'GG','Hydrabad Tourism pack',14000)")
         Cursor.execute("insert into Brochure values(8,'HH','Nainital Tourism pack',8000)")
         Cursor.execute("insert into Brochure values(9,'II','Darjeeling Pack',12000)")
         Cursor.execute("insert into Brochure values(10,'JJ','Andman & Nicobar',24000)")
     cnx.commit()
     Cursor.close()
     cnx.close()

'''def Insert1():
    cnx = mysql.connector.connect(user='root', password='banti', host='localhost', database='Tourdemo')
    Cursor = cnx.cursor()
    dat=date.today()
    Cursor.execute("select count(*) from user")
    l=(list(Cursor))
    for j in l:
        n=(j[0])
    if n==0:
        nm='demo'
        mb=9999999999
        ads='demo'
        uml='demo@gmail.com'
        p='1'
        Qry=("INSERT INTO User VALUES(%s,%s,%s,%s,%s,%s)")
        data=(nm,mb,ads,uml,p,dat)
        Cursor.execute(Qry,data)
        cnx.commit()
        #Cursor.execute("INSERT INTO User VALUES('demo',0000000000,'demo','demo@gmail.com','1','99-02-16' ")'''
     
'''

def AddPrimary():
     cnx = mysql.connector.connect(user='root', password='banti', host='localhost', database='Tourdemo')
     Cursor = cnx.cursor()
     Cursor.execute("alter table member add primary key(mno)")
     Cursor.close()
     cnx.close()'''
