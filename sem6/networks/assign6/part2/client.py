import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_address = ('localhost', 9999)

try:
    while True:
        # Message to be sent
        message = input("Enter message to send to server: ")

        # Send data
        print('Sending message to server')
        client_socket.sendto(message.encode(), server_address)

        # Check if client wants to quit
        if message.strip() == 'quit':
            print('Closing connection...')
            break

        # Receive response
        print('Waiting to receive echoed message from server')
        echoed_message, server = client_socket.recvfrom(4096)
        print('Received echoed message:', echoed_message.decode())

finally:
    print('Closing socket')
    client_socket.close()

