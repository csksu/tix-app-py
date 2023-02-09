# csksu: tix-app-py
# 2/28/2023
# python helloworld script run in a kubernetes pod.
import http.server
import socketserver

# define the port we'll be listening on...
PORT = 8080
# create http handler...
Handler = http.server.SimpleHTTPRequestHandler

# Function to handle any http request, serve up the 'index.html'
# page, and output "TIX-APP python server: hello."
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
