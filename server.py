import http.server as hs
import socketserver

PORT = 8001

Handler = hs.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("server at port", PORT)
    httpd.serve_forever()
