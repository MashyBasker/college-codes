import socket

port = 5000
portClient = 8000
host = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((host, portClient))
client.connect((host, port))

while True:
    data = input("Enter the value 'n': ")
    client.send(data.encode())
    if data == 'quit':
        break
    q = client.recv(2048).decode()
    print(f"Sum of squares: {q}")

print("Connection was closed by server")
client.close()