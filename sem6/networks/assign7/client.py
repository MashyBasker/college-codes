import socket
# Function to take dataword and polynomial as input from the user
def get_input():
    dataword = input("Enter the dataword: ")
    polynomial = input("Enter the polynomial: ")
    return dataword, polynomial
# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Server address and port
server_address = ('localhost', 12345)

try:
    # Connect to the server
    client_socket.connect(server_address)
    print(f'Connected to {server_address}')
    # Get dataword and polynomial input from the user
    dataword, polynomial = get_input()
    # Send dataword and polynomial to the server
    client_socket.send(f'{dataword},{polynomial}'.encode())
    print(f'Data sent to {server_address}: {dataword}, {polynomial}')
# Receive the result from the server
    result = client_socket.recv(1024).decode()
    print(f'Result from {server_address}: {result}')
finally:
# Close the connection
    client_socket.close()