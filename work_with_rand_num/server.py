from http.server import HTTPServer, CGIHTTPRequestHandler


def run(server_class=HTTPServer, handler_class=CGIHTTPRequestHandler):
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, handler_class)
    print('Server is running.')
    httpd.serve_forever()
    
    
run()