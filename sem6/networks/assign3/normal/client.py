import socket

port=50000
portClient=8000
host="127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((host, portClient))
client.connect((host, port))
while True:	
	data = input("Enter your message: ")
	client.send(data.encode())
	if data=='bye':
		break
	echoback = client.recv(2048).decode()
	print("Message from server: ", echoback)
		
print("Connection closed from server")
client.close()

