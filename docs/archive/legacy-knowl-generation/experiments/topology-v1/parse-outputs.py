import re
import os

output_dir = "/Users/ryanpersson/anki/code/blog/tmp/v1-topology/knowls"
os.makedirs(output_dir, exist_ok=True)

# Read sessions file
with open("/Users/ryanpersson/anki/code/blog/tmp/v1-topology/sessions.txt") as f:
    sessions = [s.strip() for s in f.readlines() if s.strip()]

print(f"Found {len(sessions)} sessions")

# Multiple patterns to handle GPT output format variations
patterns = [
    r'\*\*`?([a-z0-9-]+\.md)`?\*\*\s*\n+```markdown\n(---\n.*?)\n```',
    r'## `([a-z0-9-]+\.md)`\s*\n+```markdown\n(---\n.*?)\n```',
    r'###? `([a-z0-9-]+\.md)`\s*\n+```markdown\n(---\n.*?)\n```',
]

def fix_content(body):
    """Fix common GPT output issues."""
    # Fix triple braces to double braces
    body = re.sub(r'\{\{\{<', r'{{<', body)
    body = re.sub(r'>\}\}\}', r'>}}', body)
    # Fix malformed shortcodes
    body = re.sub(r'\{< knowl', r'{{< knowl', body)
    body = re.sub(r' >\}', r' >}}', body)
    # Remove .md from knowl id references
    body = re.sub(r'knowl id="([a-z0-9-]+)\.md"', r'knowl id="\1"', body)
    # Fix escaped asterisks in LaTeX
    body = re.sub(r'\\\*', r'*', body)
    # Clean LaTeX from YAML description
    def clean_desc(match):
        desc = match.group(1)
        desc = re.sub(r'\\\\+[a-zA-Z]*', '', desc)
        desc = re.sub(r'\\[a-zA-Z]+', '', desc)
        desc = re.sub(r'\\[^a-zA-Z]', '', desc)
        desc = re.sub(r'\$[^$]*\$', '', desc)
        desc = re.sub(r'\s+', ' ', desc).strip()
        return f'description: "{desc}"'
    body = re.sub(r'^description:\s*"([^"]*)"', clean_desc, body, flags=re.MULTILINE)
    return body

created = []

for session in sessions:
    path = os.path.expanduser(f"~/.oracle/sessions/{session}/output.log")
    print(f"\nProcessing {session}...")
    
    try:
        with open(path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"  Warning: Session file not found: {path}")
        continue
    
    session_count = 0
    for pattern in patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        for filename, body in matches:
            slug = filename[:-3]
            
            if slug in created:
                continue
            
            body = fix_content(body)
            
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'w') as f:
                f.write(body + '\n')
            
            created.append(slug)
            session_count += 1
    
    print(f"  Extracted {session_count} knowls")

print(f"\n=== Summary ===")
print(f"Total knowls created: {len(created)}")
print(f"Output directory: {output_dir}")
