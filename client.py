#!env/bin/python3

from termcolor import colored
import json
import sys
import zmq

import fclient
import ffile

#client data
client = json.dumps({'ip': '', 'port': '', 'serverIP': '', 'serverPort': ''})
client = json.loads(client)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket_send = context.socket(zmq.REQ)


def get_id(my_ip, server_ip):
    client['ip'], client['port'] = my_ip.split(':')
    socket.bind('tcp://*:' + client['port'])

    client['serverIP'], client['serverPort'] = server_ip.split(':')


def main():
    global client, socket, socket_send
    my_ip = some_ip = ''

    if len(sys.argv) == 3:
        some_ip = sys.argv[2]
        # print(some_ip)
    elif len(sys.argv) == 2:
        print(colored('ERROR: Server IP missing', 'red', attrs=['bold']))
    else:
        print(colored('ERROR: Client IP and Server IP are missing', 'red', attrs=['bold']))

    if len(sys.argv) >= 2:
        my_ip = sys.argv[1]
        get_id(my_ip, some_ip)  # Arguments to variables python

        try:
            fclient.clear()
            fclient.client_info(client)
            print (colored(
                'Welcome to Map Reduce simulation', 'yellow', attrs=['bold']), colored('Terminal', 'yellow'))
            while True:
                inp = input(colored('$ >> ', 'cyan'))
                inp = inp.split()
                
                if inp[0] == 'help' or inp[0] == '-h':
                    fclient.options()
                elif inp[0] == 'exit':
                    print (colored('See you later', 'yellow'))
                    break
                else:
                    print (colored('Type a correct option', 'red'))

        except KeyboardInterrupt:
            print('')
            print(colored('See you later', 'yellow'))
            exit(0)
    # print(ffile.get_file('quijote.txt'))


if __name__ == '__main__':
    main()