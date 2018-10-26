#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
import webbrowser

class VirtBrowseHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        webbrowser.open(post_data.decode('UTF-8'))
        self.send_response(HTTPStatus.OK)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=VirtBrowseHandler):
    server_address = ('', 12105)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()
