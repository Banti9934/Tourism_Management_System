import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import(connection)
import os
import platform
import brochure
import pyttsx3
import maskpass

c=0


def MYSPEAKER(text,gender):
    speaker=pyttsx3.init()
    voices = speaker.getProperty('voices')
    speaker.setProperty('rate', 200)
    speaker.setProperty('voice', voices[gender].id)
    speaker.say(text)
    speaker.runAndWait()

def CLEARSCREEN():
    if platform.system() == "Windows":
        print(os.system("cls"))

        
def MAINMENU():
    print("","*"*79,"\n\t\t*** WELCOME IN TOURISM MANAGEMENT PROJECT *** \n","*"*79)
    MYSPEAKER("WELCOME IN MAIN MENU PLEASE SELECT YOUR CHOICE",0)
    print("""
             1. New User
             2. Login User
             3. Brochure
             4. GOTO MAIN MENU
             5. Exit""")
    choice=int(input("Enter choice between 1 to 4 -------> :"))
    if choice == 1:
        MENUBARREG()
    elif choice == 2:
        MENUBARLOGIN()
    elif choice == 3:
        PACKAGE()
    elif choice == 4:
        return
    elif choice == 4:
        exit()
    else:
        print("Wrong Choice.....Enter Your Choice again")
        x = input("Press any key to continue......")

def MENUBARREG():
    try:
        cnx=mysql.connector.connect(user='root',password='banti',host='localhost',database='Tourdemo')
        Cursor=cnx.cursor()
        while True:
            c=0
            print("","*"*79,"\n\t\t\t *** New User Regestration *** \n","*"*79)
            MYSPEAKER("WELCOME IN USER REGESTRATION MODULE.",1)
            u_id=0
            global Ugml
            global Upass
            Uname=(input("Enter Your name :"))
            Umob=int(input("Enter Mobile number :"))
            Uaddress=input("Enter address :")
            Ugml=(input("Enter your email :"))
            if ".com" in Ugml:
                print("\t\tValid email")
                u_pass=input("Enter ur password :")
                Upass=input("Confirm pasword :")
                if u_pass==Upass:
                    Date_of_Regestration=date.today()
                    Qry=("INSERT INTO User VALUES(%s,%s,%s,%s,%s,%s)")
                    data=(Uname,Umob,Uaddress,Ugml,Upass,Date_of_Regestration)
                    Cursor.execute(Qry,data)
                    cnx.commit()
                    Cursor.close()
                    cnx.close()
                    print("\tRecord Inserted.")
                    MYSPEAKER("YOUR DATA SAVED SUCCESSFULLY.",0)
                    MAINMENU()
                else:
                    print("\t\tPassword should not match")
            else:
                print("\t\tInvalid email")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


        
def MENUBARLOGIN():
    try:
        global c
        if (c<3):
            os.system('cls')
            cnx=mysql.connector.connect(user='root',password='banti',host='localhost',database='Tourdemo')
            Cursor=cnx.cursor()
            print("","*"*79,"\n\t\t\t *** WELCOME IN LOGIN MENU *** \n","*"*79)
            MYSPEAKER("WELCOME IN LOGIN MODULE.",1)
            Lgml=input("Enter your email :")
            query1=("SELECT * FROM User where Ugml=%s")
            rec_srch1=(Lgml,)
            Cursor.execute(query1,rec_srch1)
            for(Uname,Umob,Uaddress,Ugml,Upass,Date_of_Registration)in Cursor:
                temp1=Ugml
                temp2=Upass
            if temp1==Lgml:
                Lpass=maskpass.askpass(prompt="Enter password :",mask="*")
                if temp2==Lpass:
                    MENU2()
                else:
                    print("\t\tWrong Password....!")
                    c += 1
                    MENUBARLOGIN()


                
                '''Lpass=input("Enter password :")
                if temp2==Lpass:
                    cnx.commit()
                    Cursor.close()
                    cnx.close()
                    print("welcome")
                    MENU2()
                else:
                    print("\t\tInvalid password")
                    x=input("press any key to continue ....")
                    c += 1
                    MENUBARLOGIN()'''
            else:
                print("\t\tInvalid username")
                x=input("\t\tpress any key to continue ....")
                c += 1
                MENUBARLOGIN()
        else:
            print("\t\tYou have entered too many time wrong password .....")
            x=input("\t\tPress any key to continue .....")
            MAINMENU()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()
    except UnboundLocalError:
        print("\n\t\tINVALID EMAIL BY USER  .......!")
        x=input("PRESS ANY KEY TO CONTINUE")
        

def MENU2():
    print("","*"*79,"\n\t\t\t*** TOURISM MANAGEMENT SYSTEM ***\n","*"*79)
    MYSPEAKER("WELCOME IN CHOICE BASED MENU",1)
    print("""
            1. BOOK PACKAGE
            2. CHECK PACKAGE
            3. PRINT TICKET
            4. CANCEL TICKET
            5. CHANGE PASSWORD
            6. LOGOUT USER
            7. BROCHURE
            8. EXIT""")
    MYSPEAKER("PLEASE SELECT YOUR CHOICE.",1)
    choice=int(input("Enter your choice -----> "))
    if choice ==1:
        brochure.BOOKING2()
    elif choice ==2:
        brochure.CHECKPKG()
    elif choice ==3:
        brochure.PRINTTICKET()
    elif choice ==4:
        brochure.CANCLETICKET()
    elif choice ==5:
        brochure.CHPASS()
    elif choice == 6:
        brochure.LOGOUT()
    elif choice == 7:
        PACKAGE()
    elif choice == 8:
        exit()
    else:
        print("Wrong Choice.....Enter Your Choice again")
        x = input("Press any key to continue")
def PACKAGE():
    try:
        print("","*"*79,"\n\t\t\tPlaces with price list\n","*"*79)
        MYSPEAKER("WELCOME IN BROCHURE MENU.",1)
        os.system('cls')
        cnx=mysql.connector.connect(user='root',password='banti',host='localhost',database='Tourdemo')
        Cursor=cnx.cursor()
        query1=("SELECT * FROM Brochure")
        Cursor.execute(query1)
        print("SR-\tCODE-\t\tPLACE-\t\t\t\tCHARGES-")
        print("-"*80)
        for(SR,CODE,PLACE,CHARGES)in Cursor:
            print(SR,"\t",CODE,"\t",PLACE,"\t\t\t",CHARGES)
            print("-"*80)
        x=input("Press any key to continue .......")
        return
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()

def SHOWUSER():
        try:
            print("","*"*79,"\n\t\t\tREGISTERED USER\n","*"*79)
            os.system('cls')
            cnx=mysql.connector.connect(user='root',password='banti',host='localhost',database='Tourdemo')
            Cursor=cnx.cursor()
            
            query1=("SELECT * FROM User")
            Cursor.execute(query1,)
            print("-"*80)

            for(Bname,Bmob,Bcode,Bplace,Bcharges,Do_booking,Bno_booking,Btotal)in Cursor:
                print("\tUSERNAME :-\t\t  ",Bname,"\n","\tMobile no. :-\t  ",Bmob,"\n","\tCode :-\t\t  ",Bcode,"\n","\tPlace :-\t  ",Bplace,"\n","\tCost of Fair :-   ",Bcharges,"\n","\tDate of booking :-",Do_booking,"\n\tNumber of ticket:-",Bno_booking,"\n","\tTotal :-\t  ",Btotal)
                print("-"*80)

            print("\t\tTicket Printing in under Process.....")
            menulib.MYSPEAKER("YOUR TICKET HISTRY SENT TO PRINTER.",1)
            x=input("\t\tPress any key to continue.......")
            cnx.commit()
            Cursor.close()
            cnx.close()
            menulib.MENU2()
                            
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            cnx.close()
def SHOWUSER():
    try:
        print("","*"*79,"\n\t\t\tREGISTERED USER\n","*"*79)
        os.system('cls')
        cnx=mysql.connector.connect(user='root',password='banti',host='localhost',database='Tourdemo')
        Cursor=cnx.cursor()
        query1=("SELECT * FROM User")
        Cursor.execute(query1)
        for(Uname,Umob,Uaddress,Ugml,Upass,Date_of_Regestration)in Cursor:
            print("\tUSERNAME :-\t\t",Uname,"\n","\tMOBILE NO. :-\t\t",Umob,"\n","\tADDRESS :-\t\t",Uaddress,"\n","\tEMAIL :-\t\t",Ugml,"\n","\tPASSWORD :- \t\t",Upass,"\n","\tDATE OF REGESTRATION :- ",Date_of_Regestration)
            print("-"*80)
        x=input("Press any key to continue .......")
        return
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


