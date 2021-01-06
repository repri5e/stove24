from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Server (BaseHTTPRequestHandler):
  
  def do_GET (self):
    self.wfile.write(bytes("Hello world", "utf-8"))
   
httpd = HTTPServer(("", int(os.environ['PORT'])), Server)
httpd.serve_forever()
