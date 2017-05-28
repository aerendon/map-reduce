#!env/bin/python3

from termcolor import colored
import json
import sys
import zmq

import ffile
import fmapper

# mapper data
mapper = json.dumps({'ip': '', 'port': ''})
mapper = json.loads(mapper)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket_send = context.socket(zmq.REQ)


def get_id(my_ip, socket):
    global mapper
    mapper['ip'], mapper['port'] = my_ip.split(':')
    socket.bind('tcp://*:' + mapper['port'])


def main():
    global mapper, socket
    
    ffile.clear()
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

        fmapper.mapper_info(mapper)
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

        except KeyboardInterrupt:
            print('')

            print(colored('See you later', 'yellow'))
            exit(0)


if __name__ == '__main__':
    main()