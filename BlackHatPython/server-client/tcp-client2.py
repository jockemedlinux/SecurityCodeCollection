#!/usr/bin/env python3
import socket

target_host = "127.0.0.1"
target_port = 9997

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect((target_host,target_port))

c.send(b'Hello guy')
print('You sent: Hello Guy')
response = c.recv(4096)

print(f'Server responden: {response.decode()}')

c.close()