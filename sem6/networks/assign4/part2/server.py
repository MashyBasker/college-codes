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

def count_ones(val: str):
    c = 0
    for i in val:
        if i == '1': c += 1
    # print("Number of 1s: ", c)
    # print("In binary: ", format(c, 'b'))
    return c
while True:
    data = conn.recv(2048)
    if data.decode() == 'quit':
        break
    # n = int(data.decode())
    c = count_ones(data.decode())
    conn.send(str(c).encode())

print("connection closed by client")
conn.close()