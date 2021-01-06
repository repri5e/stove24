from http.server import HTTPServer, BaseHTTPRequestHandler
class Server (BaseHTTPRequestHandler):
  
  def do_GET (self):
    self.send_response(200)
    
    self.end_headers()
    self.wfile.write(bytes("Hello world", "utf-8"))
   
httpd = HTTPServer(("localhost", os.environ['PORT']), Server)
httpd.serve_forever()
