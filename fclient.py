#!env/bin/python3

from termcolor import colored
import os
import sys


def clear():
    os.system('clear') # on linux / os x
    # os.system('cls') # on windows


def client_info(client):
    print (colored('#############', 'magenta'))
    print (colored('My IP -->' + client['ip'] + ':' + client['port'], 'magenta'))
    print (colored('Server IP -->' + client['serverIP'] + ':' + client['serverPort'], 'magenta'))
    print (colored('#############', 'magenta'))

def options():
    print (colored('Options', 'blue', attrs=['bold']))
    print (colored('exit                      ->    Close client connection', 'blue'))
    print (colored('-g, get <sha256>          ->    Get file', 'blue'))
    print (colored('-h, help                  ->    Get help', 'blue'))
    print (colored('ls                        ->    List of my files in DHT', 'blue'))
    print (colored('-rm, remove <sha256>      ->    Remove file from DHT', 'blue'))
    print (colored('-s or send <filename.ext> ->    Send a file', 'blue'))