import socket

port = 5000
host = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
print("socket bound to port",port)

server.listen(2)
print("Socket is listening...")

conn, addr = server.accept()
print("Established connection with", addr)

def postfix_eval(expr: str):
    ops = ['+', '-', '*', '/', '%']
    stack = []
    for e in expr:
        if e not in ops:
            stack.append(e)
        else :
            a = stack.pop()
            b = stack.pop()
            
            if e == '+':
                res = int(a) + int(b)
            elif e == '-':
                res = int(b) - int(a)
            elif e == '*':
                res = int(a) * int(b)
            elif e == '/':
                res = int(b) / int(a)
            elif e == '%':
                res = int(b) % int(a)
            
            stack.append(res)
    return stack[0]
while True:
    data = conn.recv(2048)
    if data.decode() == 'quit':
        break
    k = postfix_eval(data.decode())
    # print("Output of postfix expression",postfix_eval(data.decode()))
    conn.send(str(k).encode())

print("connection closed by client")
conn.close()