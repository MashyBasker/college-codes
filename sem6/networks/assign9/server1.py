import socket
import random

ip = "0.0.0.0"
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, port))
print(f"[INFO] Server socket bound to {port}")

server.listen(100)
print("[INFO] Server socket is listening...")

conn, addr = server.accept()
print("[INFO] Received connection from", addr)

def generate_random_mac():
    return "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255))

def read_arp(ip: str):
    arp_list = open("./arp.txt").read().split("\n")
    for a in arp_list:
        temp= a.split(" ")
        ip_addr = temp[0]
        mac_addr = temp[1] 
        print(f'{ip_addr} and {mac_addr}')
        if ip_addr == ip:
           return mac_addr
    random_mac = generate_random_mac()
    print("[ERR] IP address not found in ARP Table")
    with open('arp.txt', 'a') as f:
        f.write(f"{ip} {random_mac}\n")
    return "error"



client_ip = addr[0]
mac_to_return = read_arp(client_ip)
conn.send(mac_to_return.encode())
print("Connection closed by server")
conn.close()


