from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        self.do_GET()

    def do_PATCH(self):
        self.do_GET()

    def do_HEAD(self):
        self.do_GET()

    def do_PUT(self):
        self.do_GET()


print("Starting web server")
HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
