"""
socket通信とは・・・TCP/IP通信をプログラムから利用するための入り口となるのがソケット。
"""
import http.server
import socketserver

with socketserver.TCPServer(('127.0.0.1', 8000),
            http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()