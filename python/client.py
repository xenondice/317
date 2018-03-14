import socket
import json
import requests

ip = 'localhost'
port = '80'
interval = '500'

'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock
    sock.connect((ip, port))
    sock.send
    data = sock.recv(1024)
print('Received', repr(data
'''

print('http://'+ip+':'+port+'/data/'+interval)
test = requests.get('http://' + ip + ':' + port + '/data/' + interval, stream = True)

if test.encoding is None:
    test.encoding = 'ascii'


for line in test.iter_lines():
    # filter out keep-alive new lines
    if line:
        print(json.loads(line)

#localhost:<port>/data/<every-ms>
