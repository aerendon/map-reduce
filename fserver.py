#!env/bin/python3

from termcolor import colored
import os
import sys


def clear():
    os.system('clear') # on linux / os x
    # os.system('cls') # on windows


def server_info(server):
    print (colored('#############', 'magenta'))
    print (colored('My IP -->' + server['ip'] + ':' + server['port'], 'magenta'))
    print (colored('#############', 'magenta'))