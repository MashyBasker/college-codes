import socket


def crc_check(dataword, polynomial):
    divisor = polynomial
    data = dataword + '0' * (len(polynomial) - 1)
    print('new dataword : ', data)
    for i in range(len(dataword)):
        if data[i] == '1':
            data = data[:i] + bin(int(data[i:i+len(divisor)], 2) ^ int(divisor, 2))[
                2:].zfill(len(divisor)) + data[i+len(divisor):]
    if int(data[-(len(polynomial)-1):], 2) == 0:
        return "No error detected"
    else:
        return "Error detected"
    
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)
server_socket.listen(1)
print('Server is waiting for a connection...')

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Connected to {client_address}')
    try:
        data = client_socket.recv(1024).decode()
        dataword, polynomial = data.split(',')
        result = crc_check(dataword, polynomial)
        client_socket.send(result.encode())
        print(f'Result sent to {client_address}: {result}')
    finally:
        client_socket.close()
