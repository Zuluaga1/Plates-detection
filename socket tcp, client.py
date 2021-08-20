# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 13:13:26 2021

@author: esteb
"""
import socket

HOST = '192.168.100.9'  # The server's hostname or IP address
PORT = 10840       # The port used by the server

#ENCENDER SENSORES
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'0')
    data = s.recv(1024)

