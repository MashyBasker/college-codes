import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = "files"

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        file_path = os.path.join(DIRECTORY, self.path[1:])
        if os.path.isdir(file_path):
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b'Directory listing is not allowed')
        elif not os.path.exists(file_path):
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'File not found')
        else:
            with open(file_path, 'rb') as f:
                content = f.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(content)

    def do_PUT(self):
        try:
            path = os.path.join(DIRECTORY, self.path[1:])
            content_length = int(self.headers['Content-Length'])
            with open(path, 'wb') as f:
                f.write(self.rfile.read(content_length))
            self.send_response(201)
            self.end_headers()
            self.wfile.write(b'File uploaded successfully')
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

    def do_DELETE(self):
        try:
            path = os.path.join(DIRECTORY, self.path[1:])
            os.remove(path)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'File deleted successfully')
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server started at port", PORT)
    httpd.serve_forever()
