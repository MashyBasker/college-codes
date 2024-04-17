import socket
import pickle

port = 5000
portClient = 8000
host = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((host, portClient))
client.connect((host, port))

try:
    while True:
        data = input("Enter URL and depth: ")
        client.send(data.encode())
        if data == "quit":
            break
        try:
            all_links = pickle.loads(client.recv(32768))
            print("Data received from server:")
            for l in all_links:
                for a in  l:
                    print(f"Visited {a}")
        except pickle.UnpicklingError as e:
             print(f"Error in Unpickling {e}")

except KeyboardInterrupt:
    print("KeyboardInterrupt: Connection terminated by user")

finally:
    print("Connection closed")
    client.close()

