#!env/bin/python3

from termcolor import colored


def mapper_info(mapper):
    print (colored('############# MAPPER', 'magenta'))
    print (colored('My IP -->' + mapper['ip'] + ':' + mapper['port'], 'magenta'))
    print (colored('#############', 'magenta'))