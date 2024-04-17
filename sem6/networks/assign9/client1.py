import socket

client_ip = "127.0.0.7"
port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
client.bind((client_ip, 8000))
client.connect((client_ip, port))

mac = client.recv(2048).decode()
if mac != "error":
    print("The MAC address for this IP address is: ", mac)
    print("Connection closed by client")
else:
    print("[INFO] This IP address was not found in the ARP Table. It has been added")
client.close()
