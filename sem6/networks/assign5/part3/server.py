from bs4 import BeautifulSoup
import requests
import re
import socket
import pickle

def scrape(url):        
    resp = requests.get(url)
    html_doc = resp.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    return [link.get('href') for link in soup.find_all('a', attrs={'href': re.compile("^https://")})]

def crawl(url, depth):
    all_links = []
    links = []
    if url is not None and url.startswith("http"):
        links = scrape(url)
        all_links.append(links)
    for _ in range(1, depth):
        links_to_scrape = all_links[-1]
        links = []
        for l in links_to_scrape:
            if l is not None and l.startswith("http"):
                print(f"Scraping {l}")
                links = scrape(l)
                all_links.append(links)
        print("-"*20)
    return all_links


port = 5000
host = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
print("socket bound to port",port)

server.listen(2)
print("Socket is listening...")

while True:
    conn, addr = server.accept()
    print("Established connection with client")

    try:
        while True:
            url = conn.recv(2048).decode()
            if url == 'quit':
                break
            url, depth = url.split(" ")
            links = crawl(url, int(depth))
            
            serialized = pickle.dumps(links)
            conn.send(serialized)
            conn.send(b'')
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        print("Connection closed by client")
        conn.close()




