#!/usr/bin/env python3
#@jockemedlinux

import socket

target_host = "127.0.0.1"
target_port = 9999

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

c.sendto(b'Hello handsome!', (target_host, target_port))

data, addr = c.recvfrom(4096)

print(data.decode())
c.close()