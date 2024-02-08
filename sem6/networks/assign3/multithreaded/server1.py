#!/usr/bin/python3
import socket
import sys

# defining the data
PORT=1331

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', PORT))
    print(f"✔️  Socket is bound to port {PORT}")
    s.listen(5)
    print("✔️  Socket is listening")
    return s

def run_server(s):
    c, addr = s.accept()
    print(f"Connected to", addr)
    while True:
        msg = input(">>> ")
        msg1 = "[User 1] " + msg 
        c.send(msg1.encode())
        if msg == 'bye':
            break
    s.close()

s = create_socket()
run_server(s)
