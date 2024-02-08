import socket

port=50000
host="127.0.0.1"

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
print("socket binded to %s" %(port))

server.listen(2)
print("Socket is listening...")

# Accepting/Establishing connection from client.
conn, addr = server.accept()        
print('Got connection from', addr)

while True:
    recieved_data = conn.recv(2048).decode()
    # print("Message from client: ",recieved_data.decode())
    if recieved_data=='bye':
        break
    else:
        n = len(recieved_data)
        a = ""
        if n % 2 == 0:
            for i in range(n):
                if i % 2 == 0:
                    a += recieved_data[i]
        else:
            for i in range(n):
                if i % 2 == 1:
                    a += recieved_data[i]
        conn.send(a.encode())

print("Connection closed from client")		

#Close the connection with the client
conn.close()