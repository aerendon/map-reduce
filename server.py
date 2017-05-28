#!env/bin/python3

from termcolor import colored
import json
import sys
import zmq

import ffile
import fserver

# server data
server = json.dumps({'ip': '', 'port': ''})
server = json.loads(server)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket_send = context.socket(zmq.REQ)


def get_id(my_ip, socket):
    global server
    server['ip'], server['port'] = my_ip.split(':')
    socket.bind('tcp://*:' + server['port'])


def main():
    global server, socket
    
    fserver.clear()
    # print len(sys.argv)
    my_ip = some_ip = ''

    if len(sys.argv) == 3:
        print('Hay alguien ' + sys.argv[2])
        print(my_ip)
        some_ip = sys.argv[2]
    elif len(sys.argv) == 2:
        print('Only 1 argv')
    else:
        print('No argv')

    if len(sys.argv) >= 2:
        my_ip = sys.argv[1]
        get_id(my_ip, socket)  # Arguments to variables python

        fserver.server_info(server)
        try:
            while True:
                #  Wait for next request from client
                print('Waiting Request...')
                message = socket.recv()
                # print (str(message))
                req_json = json.loads(message.decode("utf-8"))
                ffile.printJSON(req_json)
                # #  Do some 'work'
                socket.connect('tcp://' + req_json['from'])

                if req_json['req'] == 'send':
                    socket.send_string('Received ' + req_json['msg']['filename'])

                    mappers = ffile.get_file('mapper.conf')
                    fserver.send_chunk(server, mappers, req_json['msg']['data'])

        except KeyboardInterrupt:
            print('')

            print(colored('See you later', 'yellow'))
            exit(0)


if __name__ == '__main__':
    main()