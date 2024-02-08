#!/usr/bin/python3
import socket
import threading

PORT1 = 1331 
PORT2 = 1332

def create_client(port):
    s = socket.socket()
    s.connect(('127.0.0.1', port))
    print(f"✔️  Client at port {port} successfully connected")
    return s

def run_client(s):
    while True:
        msg = s.recv(2048).decode()
        username, message =  msg.split("] ")
        #print(message)
        if msg == 'exit':
            break
        else:
            n = len(message)
            a = ''
            if n % 2 == 0:
                for i in range(n):
                    if i % 2 == 0:
                        a += message[i]
            else:
                for i in range(n):
                    if i % 2 == 1:
                        a += message[i]
            print(username + "] "+a)
    s.close()

s1 = create_client(PORT1)
s2 = create_client(PORT2)

thread1 = threading.Thread(target=run_client, args=(s1,))
thread2 = threading.Thread(target=run_client, args=(s2,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()


