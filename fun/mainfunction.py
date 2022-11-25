from fun.logofunction import *
from fun.logo import *
import os
from fun.logo import *
from termcolor import colored

def start():
    os.system("clear")
    logofun()


def clickone():
    print(colored(logo,"red"))


def about():
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


