import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 9999)
print('Starting up on {} port {}'.format(*server_address))
server_socket.bind(server_address)

def ones(binary):
    return sum([1 for x in binary if x == '1'])

while True:
    print('\nWaiting to receive message from client')
    data, client_address = server_socket.recvfrom(4096)
    
    message = data.decode()
    print('Binary string:', message)
    
    # Check if the client wants to quit
    if message.strip() == 'quit':
        print('Client requested to close the connection. Closing server...')
        break
    
    # Echo back the received message to the client
    c = ones(message)
    server_socket.sendto(str(c).encode(), client_address)

# Close the server socket
server_socket.close()

