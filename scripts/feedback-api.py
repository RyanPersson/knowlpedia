#!/usr/bin/env python3
"""
Feedback API for voting on knowls.
Run alongside hugo server: python3 scripts/feedback-api.py
Listens on port 3001.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import re
from datetime import datetime

FEEDBACK_FILE = "research/flagged-knowls.txt"
CONTENT_DIR = "content"

class FeedbackHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        if self.path in ['/flag', '/vote']:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')

            try:
                data = json.loads(body)
                knowl_id = data.get('knowlId', 'unknown')
                section = data.get('section', 'unknown')
                note = data.get('note', '').strip()
                vote = data.get('vote', 'down')  # 'up' or 'down'

                # Ensure research directory exists
                os.makedirs(os.path.dirname(FEEDBACK_FILE), exist_ok=True)

                # Append to feedback log (tags applied separately via apply-feedback.py)
                with open(FEEDBACK_FILE, 'a') as f:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    vote_symbol = '👍' if vote == 'up' else '👎'
                    line = f"{timestamp} | {vote_symbol} | {section}/{knowl_id}"
                    if note:
                        line += f" | {note}"
                    f.write(line + "\n")

                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'ok', 'knowlId': knowl_id, 'vote': vote}).encode())

                vote_text = '👍 Upvoted' if vote == 'up' else '👎 Downvoted'
                print(f"{vote_text}: {section}/{knowl_id}" + (f" - {note}" if note else ""))

            except Exception as e:
                self.send_response(500)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(str(e).encode())
                print(f"Error: {e}")
        else:
            self.send_response(404)
            self.end_headers()

    def add_tag(self, filepath, new_tag):
        """Add a tag to knowl's YAML front matter"""
        with open(filepath, 'r') as f:
            content = f.read()

        # Check if already has this tag
        if f'"{new_tag}"' in content or f"'{new_tag}'" in content or f'- {new_tag}' in content:
            return

        # Parse front matter
        if not content.startswith('---'):
            return

        parts = content.split('---', 2)
        if len(parts) < 3:
            return

        front_matter = parts[1]
        body = parts[2]

        # Check if tags already exist
        if re.search(r'^tags:', front_matter, re.MULTILINE):
            # Add to existing tags (inline format)
            front_matter = re.sub(
                r'^(tags:\s*\[)([^\]]*)\]',
                lambda m: f'{m.group(1)}{m.group(2)}, "{new_tag}"]' if m.group(2).strip() else f'{m.group(1)}"{new_tag}"]',
                front_matter,
                flags=re.MULTILINE
            )
        else:
            # Add new tags field
            front_matter = front_matter.rstrip() + f'\ntags: ["{new_tag}"]\n'

        new_content = '---' + front_matter + '---' + body

        with open(filepath, 'w') as f:
            f.write(new_content)

    def log_message(self, format, *args):
        # Quiet logging
        pass

if __name__ == '__main__':
    port = 3001
    server = HTTPServer(('localhost', port), FeedbackHandler)
    print(f"Feedback API running on http://localhost:{port}")
    print(f"Votes logged to {FEEDBACK_FILE}")
    print(f"Run 'python3 scripts/apply-feedback.py' to apply tags to knowl files")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down")
