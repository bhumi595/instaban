from termcolor import colored
from fun.option2 import *
from fun.secondmain import *
import time

def fistoptionn():
    password=input(colored("Enter Password:","yellow"))
    if password == "C":
        mainop()
        optionsecond()
    else:
        print(colored("Wrong Password!","red"))
        time.sleep(1)
        wrongpassworda()
