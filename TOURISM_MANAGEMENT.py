import menulib
import start
import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import(connection)
def NEWSTART():
    try:
        cnx=mysql.connector.connect(user='root',password='banti',host='localhost',database='Tourdemo')
        Cursor=cnx.cursor()
        while True:
            menulib.CLEARSCREEN()
            print("","*"*79,"\n\t\t\t***|| TOURISM MANAGEMENT ||***\n","*"*79)
            print("\t\t***|| WELCOME IN TOURISM MANAGEMENT SYSTEM PROJECT ||***\n","*"*79)
            print('''
                    SELECT YOUR PREFENCE\n
                    \t\t1.Admin
                    \t\t2.User
                    \t\t3.Exit
                    ''')
            x=int(input("ENTER YOUR CHOICE :"))
            if x==1:
                start.START()
            elif x==2:
                menulib.MAINMENU()
            elif x==3:
                exit()
            else:
                print("Invalid")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


NEWSTART()
        
