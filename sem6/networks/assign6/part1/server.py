import socket

host = "127.0.0.1"
port = 5000
buffer = 2048

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind((host,port))
print("UDP server is up and listening...")

while True:
    byteaddresspair = sock.recvfrom(buffer)
    msg = byteaddresspair[0].decode()
    if msg == 'quit':
        break
    print("Message from the client: ", msg)

print("Connection closed by server")
sock.close()

