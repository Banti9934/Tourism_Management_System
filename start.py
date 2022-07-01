import pyttsx3
import start
import menulib
import Database
import brochure
import maskpass  # importing maskpass library


Database.DatabaseCreate()
Database.TablesCreate()
Database.Insert()


def START():   
    c=0
    x=''
    while True:
        menulib.CLEARSCREEN()
        print("","*"*79,"\n\t\t\t","***|| TOURISM MANAGEMENT ||***\n","*"*79)
        print("\t\t\t    ***|| ADMIN LOGIN ||***\n","*"*79)
        menulib.MYSPEAKER("Welcome In TOURISM MANAGEMENT SYSTEM PROJECT",1)
        menulib.MYSPEAKER("This project is made by BANTI KUMAR VERMA",1)
        userDetails={'banti':'123','mac':'258','sun':'321','abinash':'12345'}
        uname=input("Enter your username :")
        if(c<2):
            if uname in userDetails.keys():
                #pas=input("Enter password : ")
                
                while(c<3):
                    pas=maskpass.askpass(prompt="Enter password :",mask="*")
                    if pas in userDetails.values():
                        menulib.MYSPEAKER("WELCOME YOU ARE AUTHORISED TO ACCESS",1)
                        MEN()
                    else:
                        menulib.MYSPEAKER("Wrong Password....!",1)
                        print("\t\tWrong Password....!")
                        c += 1
                        '''
                if pas in userDetails.values():
                        menulib.MYSPEAKER("WELCOME YOU ARE AUTHORISED TO ACCESS",1)
                        MEN()
                else:
                    menulib.MYSPEAKER("Wrong Password....!",1)
                    print("\t\tWrong Password....!")
                    c += 1'''
            else:
                c += 1
                menulib.MYSPEAKER("Wrong Username....!",1)
                print("\t\tWrong Username....!")
        else:
            menulib.MYSPEAKER("sorry You have reached the maximum limit.",1)
            print("\t\tYou have reached the maximum limit.")
            exit()

def MEN():
    while True:
        menulib.CLEARSCREEN()
        print("","*"*79,"\n\t\t\t","***|| TOURISM MANAGEMENT ||***\n","*"*79)
        print("\t\t\t***|| WELCOME IN ADMIN MENU ||***\n","*"*79)
        print("""SELECT YOUR CHOICE------>\n
                    1.GOTO USER MENU
                    2.SEE REGISTERED USER
                    3.SEE BROCHURE
                    4.SEE BOOKRECORD
                    5.EXIT""")
        ch=int(input("SELECT YOUR CHOICE :"))
        if ch==1:
            menulib.MAINMENU()
        elif ch==2:
            menulib.SHOWUSER()
        elif ch==3:
            menulib.PACKAGE()
        elif ch==4:
            brochure.SHOWBRECORD()
        elif ch==5:
            exit()
        else:
            print("INVALID CHOICE.........!")
            x=input("PRESS ANY KEY-------")
