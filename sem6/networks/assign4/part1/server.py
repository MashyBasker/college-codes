import socket

port = 5000
host = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
print("socket bound to port",port)

server.listen(2)
print("Socket is listening...")

conn, addr = server.accept()
print("Established connection with", addr)

def sum_of_sqr(n):
    s = 0
    for i in range(1, n+1):
        print(i)
        s += i*i
    return s

while True:
    data = conn.recv(2048)
    if data.decode() == 'quit':
        break
    n = int(data.decode())
    s = sum_of_sqr(n)
    conn.send(str(s).encode())

print("connection closed by client")
conn.close()
