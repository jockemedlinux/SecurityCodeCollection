#!/usr/bin/env python3
import socket

target_host = "jockemedlinux.dev"
target_port = 80

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect((target_host,target_port))

c.send(b"GET / HTTP/1.1\r\nHost: jockemedlinux.dev\r\n\r\n")

response = c.recv(4096)

print(response.decode())

c.close()