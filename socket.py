# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:14:51 2021

@author: esteb
"""

import socket
HOST = '192.168.1.85'  # Standard loopback interface address (localhost)
PORT = 10840        # Port to listen on (non-privileged ports are > 1023)
soc=True
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print("estableciendo conexión con el cliente")
    with conn:
        print('Connected by', addr)
        while soc == True:
            data = conn.recv(1024)
            print(data)
            data = str(data, "utf-8")
            if data != 0:
                soc=False
                placa = data.split(',')
                print(placa[1])
            
"""
for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5.0)
    sensor = 0
    message = '1'
    addr = ("localhost", 10840)

    #start = time.time()
    client_socket.sendto(message.encode(), addr)
    
    try:
        data, server = client_socket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print(f'{data} {pings} {elapsed}')
    except socket.timeout:
        print('REQUEST TIMED OUT')
        """
