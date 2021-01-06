from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Server (BaseHTTPRequestHandler):
  
  def do_GET (self):
    self.send_response(200)
    
    self.wfile.write(bytes("Hello world", "utf-8"))

    self.end_headers()
   
httpd = HTTPServer(("", int(os.environ['PORT'])), Server)
httpd.serve_forever()
