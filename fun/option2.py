from termcolor import colored
from fun.mainfunction import *
from fun.option3 import *
from fun.no import *
from fun.igreport import *
from fun.logo import  *
from fun.secondmain import *

def logoin():
    os.system("clear")
    print(colored(logo,"blue") + colored(option,"red"))

def optionsecond():
    logoin()
    option = input(colored("Choose an Option:","yellow"))
    if option == "1":
        reporterboting()
    elif option == "2":
        os.system("clear")
        print(colored(logo,'blue') + colored(social_media,'red'))
        print(colored(about1,"green",attrs=['reverse', 'blink']) + (colored(about2,"yellow")) + (colored(about3,"red",attrs=['reverse', 'blink'])) + colored(about4,"blue") )
        what=input(colored("{0}--exit:","yellow"))
        if what=="0":
            os.system("python3 instaban.py")
        else:
            print(colored("[!] Invalid Option, Try Again...","red"))
            os.system("clear")
            os.system("python3 instaban.py")
    elif option == "9":
        update = input(colored("Do you want to update this tool[y/n]:","yellow"))
        if update == "y":
            os.system("cd /home && rm -rf instaban")
            os.system("cd /home && git clone https://github.com/kdo2006/instaban")
            print(colored(updated,"red"))
            os.system("cd /home && cd instaban && python3 instaban.py")
        elif update == "n":
            optionsecond()
        else:
            print(colored("invailed options...!"))
            time.sleep(2)
            optionsecond()
    elif option == "99":
        os.system("cd /home && rm -rf instaban")
    elif option == "999":
        os.system("exit")