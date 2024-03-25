import http.server, ssl

httpd = http.server.HTTPServer(('localhost', 8080), http.server.SimpleHTTPRequestHandler)
httpd.serve_forever()