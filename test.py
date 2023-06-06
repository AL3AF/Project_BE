import http.server


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path[1:]
        query_params = parse_qs(parsed_url.query)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        if path == 'students':
            if 'name' in query_params:
                name = query_params['name'][0]
                response = f"Hello, {name}!"
            else:
                response = "Welcome, student!"
        else:
            response = "Page not found"

        self.wfile.write(response.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, MyHandler)
    print('Server running...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Server stopped')
        httpd.server_close()
