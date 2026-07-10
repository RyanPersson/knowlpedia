#!/usr/bin/env python3
"""Parse oracle session outputs and create knowl files."""
import re
import os

section = "measure-theory"
output_dir = f"/Users/ryanpersson/anki/code/blog/content/{section}"

# Read sessions
with open("/Users/ryanpersson/anki/code/blog/tmp/phase1-measure/sessions.txt") as f:
    sessions = [s.strip() for s in f.readlines() if s.strip()]

print(f"Found {len(sessions)} sessions")

# Patterns for extracting knowls
patterns = [
    r'\*\*`?([a-z0-9-]+\.md)`?\*\*\s*\n+```markdown\n(---\n.*?)\n```',
    r'## `([a-z0-9-]+\.md)`\s*\n+```markdown\n(---\n.*?)\n```',
]

def fix_content(body):
    """Fix common GPT output issues."""
    # Fix triple braces to double braces
    body = re.sub(r'\{\{\{<', r'{{<', body)
    body = re.sub(r'>\}\}\}', r'>}}', body)
    # Fix single braces
    body = re.sub(r'(?<!\{)\{< knowl', r'{{< knowl', body)
    body = re.sub(r' >\}(?!\})', r' >}}', body)
    # Remove .md from knowl id references
    body = re.sub(r'knowl id="([a-z0-9-]+)\.md"', r'knowl id="\1"', body)
    # Clean LaTeX from YAML description
    def clean_desc(match):
        desc = match.group(1)
        desc = re.sub(r'\\[a-zA-Z]+', '', desc)
        desc = re.sub(r'\$[^$]*\$', '', desc)
        desc = re.sub(r'\s+', ' ', desc).strip()
        return f'description: "{desc}"'
    body = re.sub(r'^description:\s*"([^"]*)"', clean_desc, body, flags=re.MULTILINE)
    return body

created = []
for session in sessions:
    path = os.path.expanduser(f"~/.oracle/sessions/{session}/output.log")
    print(f"Processing {session}...")

    with open(path, 'r') as f:
        content = f.read()

    for pattern in patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        for filename, body in matches:
            if filename in [f + '.md' for f in created]:
                continue  # Skip duplicates

            body = fix_content(body)
            filepath = os.path.join(output_dir, filename)

            with open(filepath, 'w') as f:
                f.write(body + '\n')
            created.append(filename[:-3])
            print(f"  Created: {filename}")

print(f"\n=== Created {len(created)} knowl files ===")
print("Slugs:", ", ".join(sorted(created)))
