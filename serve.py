#!/usr/bin/env python3
"""Simple HTTP server to preview the Keen AI landing page."""

import http.server
import os
import sys

PORT = 8800
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    print(f"\n  🟢 Keen AI — serving at http://localhost:{PORT}\n")
    print(f"  Press Ctrl+C to stop.\n")
    with http.server.HTTPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Stopped.")
            sys.exit(0)
