import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 9999)
print('Starting up on {} port {}'.format(*server_address))
server_socket.bind(server_address)

def transform(data):
    ans = ""
    if len(data) % 2 == 0:
        for i in range(len(data)):
            if i % 2 == 0:
                ans += data[i]
    else:
        for i in range(len(data)):
            if i % 2 == 1:
                ans += data[i]
    return ans

while True:
    print('\nWaiting to receive message from client')
    data, client_address = server_socket.recvfrom(4096)
    
    message = data.decode()
    print('Message:', message)
    
    # Check if the client wants to quit
    if message.strip() == 'quit':
        print('Client requested to close the connection. Closing server...')
        break
    
    # Echo back the received message to the client
    ans = transform(message)
    server_socket.sendto(ans.encode(), client_address)

# Close the server socket
server_socket.close()

