import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import(connection)
import os
import pyttsx3
import menulib
def BOOKING2():
    try:
        print("","*"*79,"\n\t\t\tPlaces with price list\n","*"*79)
        menulib.MYSPEAKER("WELCOME IN BOOKING MENU.",1)
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

        Bcode=input("Enter Place code (eg:AA,BB,....) :")
        ser=input("Enter your name :")
        Bno_booking=int(input("Enter number of tickes to book :"))
        b=int(input("Would you like to confirm Booking ?\n\t\t\tPRESS(1,2)\t[1]-Yes\t[2]-No\t :"))
        

        query2=("SELECT * FROM User where Uname=%s")
        rec_srch1=(ser,)
        Cursor.execute(query2,rec_srch1)
        for(Uname,Umob,Uaddress,Ugml,Upass,Date_of_Registration)in Cursor:
            Bname=Uname
            Bmob=Umob
            ser=Bname
            
        query3=("SELECT * FROM Brochure WHERE CODE=%s")
        rec_srch=(Bcode,)
        Cursor.execute(query3,rec_srch)
        for(SR,CODE,PLACE,CHARGES)in Cursor:
            Bplace=PLACE
            Bcharges=CHARGES

        Btotal=Bcharges*Bno_booking
        Do_booking=date.today()
        
        def book():
            
            a=("INSERT INTO bookrecord VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
            val=(Bname,Bmob,Bcode,Bplace,Bcharges,Do_booking,Bno_booking,Btotal)
            Cursor.execute(a,val)
            cnx.commit()
            Cursor.close()
            cnx.close()
            
            print("Record inserted successfully.")
            menulib.MYSPEAKER("Record inserted successfully.",1)
        def againbook():
            menulib.MYSPEAKER("WELCOME AGAIN IN BOOKING MODULE.",1)
            c=int(input("Would you like to Again Booking ?\n\t\t\tPRESS(1,2)\t[1]-Yes\t[2]-No\t :"))
            if(c==1):
                BOOKING2()                
            else:
                x=input("Press any key to move previous menu ")
                menulib.MENU2()
            cnx.commit()
        if (b==1):
            if Bcode == 'AA':
                book()
                againbook()
            elif Bcode =='BB':
                book()
                againbook()
            elif Bcode =='CC':
                book()
                againbook()
            elif Bcode =='DD':
                book()
                againbook()
            elif Bcode =='EE':
                book()
                againbook()
            elif Bcode == 'FF':
                book()
                againbook()
            elif Bcode == 'GG':
                book()
                againbook()
            elif Bcode == 'HH':
                book()
                againbook()
            elif Bcode == 'II':
                book()
                againbook()
            elif Bcode == 'JJ':
                book()
                againbook()
            else:
                print("\tWrong Code Choice.....")
                print("\tYou have been Loggedout Successfully")
                x = input("\tPress any key to continue.......")
        else:
            print("\tTicket booking cancled due to invalid choice.")
            x = input("\tPress any key to continue...")
            menulib.MAINMENU()
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()
    except NameError:
        print("ENTERED NAME NOT VALID.......\n\t\tENTER YOUR NAME TO COMPLETE BOOKING")
        x=input("\tPRESS ANY KEY TO CONTINUE.....")
        BOOKING2()

def CHECKPKG():
    try:
        print("","*"*79,"\n\t\t\tTicket Booked Histry\n","*"*79)
        menulib.MYSPEAKER("WELCOME IN Ticket Booked Histry.",1)
        os.system('cls')
        cnx=mysql.connector.connect(user='root',password='banti',host='localhost',database='Tourdemo')
        Cursor=cnx.cursor()
        
        ser=input("Enter name to see booking histry :")
        query2=("SELECT * FROM Bookrecord where Bname=%s")
        rec_srch1=(ser,)
        Cursor.execute(query2,rec_srch1)
    
        print("-"*80)
        for(Bname,Bmob,Bcode,Bplace,Bcharges,Do_booking,Bno_booking,Btotal)in Cursor:
            print("\tNAME :-\t\t   ",Bname,"\n","\tMOBILE NO.:-\t   ",Bmob,"\n","\tCODE :-\t\t   ",Bcode,"\n","\tPLACE :-\t   ",Bplace,"\n","\tCHARGES :-\t   ",Bcharges,"\n","\tDate of Booking :- ",Do_booking,"\n\tNumber of ticket :-",Bno_booking,"\n","\tTotal :-\t   ",Btotal)
            print("-"*80)

        cnx.commit()
        Cursor.close()
        cnx.close()
        x=input("Press any key to move previous menu .....")
        menulib.MENU2()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()

def PRINTTICKET():
        try:
            print("","*"*79,"\n\t\t\tTicket Print Menu\n","*"*79)
            menulib.MYSPEAKER("WELCOME IN TICKET PRINT MENU.",1)
            os.system('cls')
            cnx=mysql.connector.connect(user='root',password='banti',host='localhost',database='Tourdemo')
            Cursor=cnx.cursor()
            
            ser=input("Enter name to see booking histry :")
            cod=input("Enter Place Code : ")
            
            query1=("SELECT * FROM Bookrecord where Bname=%s AND Bcode=%s")
            rec_srch1=(ser,cod,)
            Cursor.execute(query1,rec_srch1)
            print("-"*80)

            for(Bname,Bmob,Bcode,Bplace,Bcharges,Do_booking,Bno_booking,Btotal)in Cursor:
                print("\tName :-\t\t  ",Bname,"\n","\tMobile no. :-\t  ",Bmob,"\n","\tCode :-\t\t  ",Bcode,"\n","\tPlace :-\t  ",Bplace,"\n","\tCost of Fair :-   ",Bcharges,"\n","\tDate of booking :-",Do_booking,"\n\tNumber of ticket:-",Bno_booking,"\n","\tTotal :-\t  ",Btotal)
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

def CANCLETICKET():
        try:
            print("","*"*79,"\n\t\t\tTICKET CANCEL MENU\n","*"*79)
            menulib.MYSPEAKER("WELCOME IN TICKET CANCEL MENU.",1)
            os.system('cls')
            cnx=mysql.connector.connect(user='root',password='banti',host='localhost',database='Tourdemo')
            Cursor=cnx.cursor()

            se=input("Enter name to See booking for further deletion process :")
            co=input("Enter Place Code : ")
            
            query1=("SELECT * FROM Bookrecord WHERE Bname=%s AND Bcode=%s")
            rec_srch0=(se,co,)
            Cursor.execute(query1,rec_srch0,)
            print("-"*80)

            for(Bname,Bmob,Bcode,Bplace,Bcharges,Do_booking,Bno_booking,Btotal)in Cursor:
                print("\tName :-\t\t  ",Bname,"\n","\tMobile no. :-\t  ",Bmob,"\n","\tCode :-\t\t  ",Bcode,"\n","\tPlace :-\t  ",Bplace,"\n","\tCost of Fair :-   ",Bcharges,"\n","\tDate of booking :-",Do_booking,"\n\tNumber of ticket:-",Bno_booking,"\n","\tTotal :-\t  ",Btotal)
                print("-"*80)
                
            ser=input("Enter name to Cancel booking :")
            cod=input("Enter Place Code : ")
            tot=int(input("Enter number of ticket that u want to cancel :"))

            query2=("DELETE FROM Bookrecord where Bname=%s AND Bcode=%s AND Bno_booking=%s")
            rec_srch1=(ser,cod,tot,)
            Cursor.execute(query2,rec_srch1)
            print("-"*80)
            cnx.commit()
            Cursor.close()
            cnx.close()
            
            
            print("\t\tTicket Cancle Completed")
            menulib.MYSPEAKER("YOUR TICKET CANCELED THANK YOU.",1)
            x=input("\t\tPress any key to continue.......")
            menulib.MENU2()
                            
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            cnx.close()

def CHPASS():
    try:
        print("","*"*79,"\n\t\t\tPASSWORD CHANGE MENU\n","*"*79)
        menulib.MYSPEAKER("WELCOME IN CHANGE PASSWORD MENU.",1)
        os.system('cls')
        cnx=mysql.connector.connect(user='root',password='banti',host='localhost',database='Tourdemo')
        Cursor=cnx.cursor()

        n=input("Enter Your email to Change Password :")
        op=input("Enter old Password :")
        np=input("New Password :")
        
        query1=("SELECT * FROM User where Ugml=%s AND Upass=%s")
        rec_srch=(n,op,)
        Cursor.execute(query1,rec_srch,)
        print("-"*80)
        
        for(Uname,Umob,Uaddress,Ugml,Upass,Date_of_Registration)in Cursor:
            Cgml=Ugml
            print(Cgml)
            Cpass=Upass
            print(Upass)
        if(Cgml==n and Cpass==op):
            query2=("UPDATE User SET Upass=%s where Ugml=%s AND Upass=%s")
            rec_srch1=(np,n,op)
            Cursor.execute(query2,rec_srch1)
            print("-"*80)
            print("\n\tPassword updated successfully.")
            cnx.commit()
            Cursor.close()
            cnx.close()
            x=input("\tPress any key to continue...... ")
            menulib.MENU2()
        else:
            print("The email or Password You entered does not matched with saved database...!")
            menulib.MYSPEAKER("The email or Password You entered does not matched with OUR database...!.",1)
            x=input("Press any key to go in previous menu ")
            menulib.MENU2()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()

def SHOWBRECORD():
    try:
        print("","*"*79,"\n\t\tTICKET BOOKED RECORD\n","*"*79)
        os.system('cls')
        cnx=mysql.connector.connect(user='root',password='banti',host='localhost',database='Tourdemo')
        Cursor=cnx.cursor()
        query1=("SELECT * FROM Bookrecord")
        Cursor.execute(query1)
        for(Bname,Bmob,Bcode,Bplace,Bcharges,Do_booking,Bno_booking,Btotal)in Cursor:
            print("\tUSER NAME :-\t\t",Bname,"\n","\tMOBILE NO. :-\t\t",Bmob,"\n","\tCODE :-\t\t\t",Bcode,"\n","\tPLACE :-\t\t",Bplace,"\n","\tBOOKING CHARGE :-  \t",Bcharges,"\n","\tDATE OF BOOKING :-\t",Do_booking,"\n","\tNUMBER OF TICKETS :-\t",Bno_booking,"\n","\tTOTAL :-\t\t",Btotal)
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

def LOGOUT():
    print("","*"*79,"\n\t\t\tlOGOUT MENU\n","*"*79)
    menulib.MYSPEAKER("WELCOME IN LOGOUT MENU.",1)
    os.system('cls')
    cnx=mysql.connector.connect(user='root',password='banti',host='localhost',database='Tourdemo')
    Cursor=cnx.cursor()
    print("\tHello user you are Logout succssfully")
    menulib.MYSPEAKER("THANK YOU FOR USING OUR SERVICES YOU ARE LOGGED OUT SUCCESSFULLY.",1)
    x=input("Press any key to continue :")
    cnx.commit()
    Cursor.close()
    cnx.close()
    menulib.MAINMENU()

