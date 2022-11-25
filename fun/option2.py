from termcolor import colored
from fun.mainfunction import *
from fun.option3 import *
from fun.no import *
from fun.igreport import *

def optionsecond():
    option = input(colored("Choose an Option:","yellow"))
    if option == "1":
        reporterboting()
    elif option == "2":
        about()
    elif option == "9":
        print("9")
    elif option == "99":
        print("99")
    elif option == "999":
        print("999")