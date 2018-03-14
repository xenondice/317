import socket
import json
import requests

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


test = requests.get('https://api.github.com/user')
