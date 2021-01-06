from http.server import HTTPServer, BaseHTTPRequestHandler

class Server (BaseHTTPRequestHandler):
  
  def do_GET (self):
    if self.path == "/":
      self.send_response(200)
    else:
      self.send_response(404)
    
    self.end_headers()
    self.wfile.write(bytes("Hello world", "utf-8"))
   
httpd = HTTPSServer(("localhost", 8080), Server)
httpd.serve_forever()
