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

while True:
    data = conn.recv(2048)
    if data.decode() == 'quit':
        break
    c = data.decode() == data.decode()[::-1]
    if c == True:
        conn.send("Palindrome".encode())
    else:
        conn.send("Not Palindrome".encode())

print("connection closed by client")
conn.close()
