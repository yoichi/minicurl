import socket

def connect(ip, port):
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.connect((ip, port))
    return s

def write(s, data):
    s.send(data.encode())

def read(s):
    return s.recv(4096).decode()

