import socket

host = "127.0.0.1"
port = 5000
buffer = 2048

udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    msg = input("Enter the message you want to send: ")
    if msg == 'quit':
        break
    udp.sendto(str.encode(msg), (host,port))

udp.close()
print("Connection closed by client")




