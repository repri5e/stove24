from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Server(BaseHTTPRequestHandler):
  
  def do_GET(self):
    print("Got get request")
    
    self.send_response(200)
    self.end_headers()
    self.wfile.write(bytes("Hello world", "utf-8"))
    
    print("Response sent")

print("Launching server...")
httpd = HTTPServer(("", int(os.environ['PORT'])), Server)
httpd.serve_forever()
