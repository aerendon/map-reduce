#!env/bin/python3

from termcolor import colored
import os
import json
import sys
import zmq

import ffile

context = zmq.Context()


def clear():
    os.system('clear') # on linux / os x
    # os.system('cls') # on windows


def server_info(server):
    print (colored('############# SERVER', 'magenta'))
    print (colored('My IP -->' + server['ip'] + ':' + server['port'], 'magenta'))
    print (colored('#############', 'magenta'))


def send_chunk(server, mappers, data):
    mappers = mappers.split('\n')

    for mapper in mappers:
        socket_send = context.socket(zmq.REQ)
        
        send_server = ffile.create_req('send_server', server['ip'] + ':' + server['port'], mapper, {'origin': server['ip'] + ':' + server['port'], 'data': data})
        
        socket_send.connect('tcp://' + mapper)
        socket_send.send_string(json.dumps(send_server))
        message = socket_send.recv()
        print(colored(message.decode("utf-8"), 'green'))
