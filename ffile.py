#!env/bin/python3

import zmq


def get_file(path):
    try:
        data = open(path, 'r').read()
    except:
        data = ''
    return data


def get_filename(path):
    return os.path.basename(path)


def write_file(data):
    file = open('Downloads/' + data['name'], 'wb')
    file.write(fclient.hexToDec(data['data']))
    file.close()
