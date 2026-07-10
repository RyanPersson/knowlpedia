#!/usr/bin/env python3
"""
Automatically process Oracle session outputs and create knowl files.
Usage: python3 process-outputs.py [sessions-file]
"""
import re
import os
import sys
import glob

CONTENT_DIR = "/Users/ryanpersson/anki/code/blog/content/geometry-bundles"
ORACLE_SESSIONS = os.path.expanduser("~/.oracle/sessions")

def fix_content(body):
    """Fix common GPT output issues."""
    # Fix triple braces to double braces
    body = re.sub(r'\{\{\{<', r'{{<', body)
    body = re.sub(r'>\}\}\}', r'>}}', body)
    # Fix malformed shortcodes
    body = re.sub(r'\{< knowl', r'{{< knowl', body)
    body = re.sub(r' >\}([^}])', r' >}}\1', body)
    body = re.sub(r'\{<\/\*', r'{{</*', body)
    body = re.sub(r'\*\/>}([^}])', r'*/>}}\1', body)
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
        desc = re.sub(r'\$[^$]*\$', '', desc)  # Remove inline math
        desc = re.sub(r'\s+', ' ', desc).strip()
        return f'description: "{desc}"'
    body = re.sub(r'^description:\s*"([^"]*)"', clean_desc, body, flags=re.MULTILINE)
    return body

def parse_session(session_path):
    """Parse a single session output file."""
    output_path = os.path.join(session_path, "output.log")
    if not os.path.exists(output_path):
        print(f"  No output.log in {session_path}")
        return []
    
    with open(output_path, 'r', errors='ignore') as f:
        content = f.read()
    
    # Multiple patterns for format variations
    patterns = [
        r'\*\*`?([a-z0-9-]+\.md)`?\*\*\s*\n+```markdown\n(---\n.*?)\n```',  # **`slug.md`**
        r'## `([a-z0-9-]+\.md)`\s*\n+```markdown\n(---\n.*?)\n```',          # ## `slug.md`
        r'###?\s+`?([a-z0-9-]+\.md)`?\s*\n+```markdown\n(---\n.*?)\n```',    # ### slug.md
    ]
    
    results = []
    for pattern in patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        for filename, body in matches:
            results.append((filename, fix_content(body)))
    
    return results

def main():
    sessions_file = sys.argv[1] if len(sys.argv) > 1 else None
    
    if sessions_file and os.path.exists(sessions_file):
        with open(sessions_file, 'r') as f:
            session_names = [s.strip() for s in f if s.strip()]
        session_paths = [os.path.join(ORACLE_SESSIONS, name) for name in session_names]
    else:
        # Find recent sessions
        session_paths = sorted(glob.glob(os.path.join(ORACLE_SESSIONS, "*")), 
                              key=os.path.getmtime, reverse=True)[:15]
    
    print(f"Processing {len(session_paths)} sessions...")
    
    created = []
    skipped = []
    
    for session_path in session_paths:
        if not os.path.isdir(session_path):
            continue
        print(f"  {os.path.basename(session_path)}...")
        results = parse_session(session_path)
        
        for filename, body in results:
            slug = filename.replace('.md', '')
            filepath = os.path.join(CONTENT_DIR, filename)
            
            if os.path.exists(filepath):
                skipped.append(slug)
                continue
            
            # Ensure body ends with newline
            if not body.endswith('\n'):
                body += '\n'
            
            with open(filepath, 'w') as f:
                f.write(body)
            created.append(slug)
    
    print(f"\nCreated: {len(created)}")
    print(f"Skipped (already exist): {len(skipped)}")
    
    # Update _index.md
    if created:
        update_index(created)
    
    return len(created)

def update_index(new_slugs):
    """Add new knowls to _index.md"""
    index_path = os.path.join(CONTENT_DIR, "_index.md")
    with open(index_path, 'r') as f:
        index_content = f.read()
    
    # Find existing slugs in index
    existing = set(re.findall(r'knowl id="([^"]+)"', index_content))
    
    # Add new ones
    new_entries = []
    for slug in sorted(set(new_slugs) - existing):
        title = slug.replace('-', ' ').title()
        new_entries.append(f'- {{{{< knowl id="{slug}" text="{title}" >}}}}')
    
    if new_entries:
        # Append before closing of Definitions section or at end
        additions = '\n'.join(new_entries) + '\n'
        if '## Definitions' in index_content:
            # Find end of definitions section or end of file
            index_content = index_content.rstrip() + '\n' + additions
        else:
            index_content += additions
        
        with open(index_path, 'w') as f:
            f.write(index_content)
        print(f"Added {len(new_entries)} entries to _index.md")

if __name__ == "__main__":
    main()
