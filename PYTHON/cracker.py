import socket
import re
import sys

def connection(ip,user,password):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Trying' + ip + ':' + user + ':' + password)
    sock.connect(('192.168.0.4',21))

    data = sock.recv(1024)
    sock.send('User' + user * '\r\n')

    data = sock.recv(1024) 

    # Unfinished
