#!env/bin/python3

from termcolor import colored
import codecs
import json
import zmq


def get_file(path):
    try:
        data = open(path, 'r').read()
    except:
        data = ''
    return (data)


def get_filename(path):
    return os.path.basename(path)


def write_file(data):
    file = open('Downloads/' + data['name'], 'wb')
    file.write(fclient.hexToDec(data['data']))
    file.close()


def create_req(req, who, to, msg):
    data = json.dumps({'req': req, 'from': who, 'to': to, 'msg': msg})
    data = json.loads(data)
    return data


def printJSON(varJSON):
    print(colored(json.dumps(varJSON, indent=2, sort_keys=True), 'cyan', attrs=['bold']))
