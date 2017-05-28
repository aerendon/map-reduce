# map-reduce

* Python 3.5

## Dependencies
### Python virtualEnv

* Install
```bash
apt-get install python-virtualenv
```

* Create Environment

```bash
mkdir env
virtualenv -p /usr/bin/python3 env
env/bin/pip install -r requirements.txt
```

## Run
### Client
```bash
./client.py <ip:port> <server_ip:server_port>
```

### Server

```bash
./server.py <ip:port>
```