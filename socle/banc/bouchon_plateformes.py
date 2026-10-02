#!/usr/bin/env python3
"""Bouchon des interfaces de plateformes, pour faire tourner publier.py
sans acces reseau sortant. Accepte /mastodon et /facebook, refuse /linkedin
pour qu'un echec reel soit mesure."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json, itertools
compteur = itertools.count(1000)
class H(BaseHTTPRequestHandler):
    def do_POST(self):
        n = int(self.headers.get('Content-Length', 0)); corps = self.rfile.read(n)
        if self.path.startswith('/linkedin'):
            self.send_response(403); self.send_header('Content-Type','application/json')
            self.end_headers(); self.wfile.write(b'{"error":"application non approuvee par la plateforme"}'); return
        self.send_response(201); self.send_header('Content-Type','application/json'); self.end_headers()
        self.wfile.write(json.dumps({"id": f"dist-{next(compteur)}", "recu": len(corps)}).encode())
    def log_message(self, *a): pass
HTTPServer(('127.0.0.1', 8899), H).serve_forever()
