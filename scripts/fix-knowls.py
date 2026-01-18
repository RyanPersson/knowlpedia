#!/usr/bin/env python3
"""
Fix common GPT output issues in knowl files.

Usage: python3 scripts/fix-knowls.py content/SECTION/

CRITICAL: GPT almost always outputs triple braces {{{< >}}} despite explicit
instructions to use double braces {{< >}}. This script fixes that and other
common issues. Run after every oracle batch.
"""
import re
import os
import sys

def fix_content(content):
    """Fix common GPT output issues."""
    # CRITICAL: Normalize to exactly double braces (GPT outputs triple or more)
    # Match any shortcode with 2+ braces and normalize to exactly 2
    content = re.sub(r'\{{2,}<', '{{<', content)
    content = re.sub(r'>\}{2,}', '>}}', content)
    
    # Single brace shortcodes (use lookahead/lookbehind to avoid matching already-double braces)
    content = re.sub(r'(?<!\{)\{< knowl', '{{< knowl', content)
    content = re.sub(r' >\}(?!\})', ' >}}', content)
    
    # Remove .md from knowl id references
    content = re.sub(r'knowl id="([a-z0-9-]+)\.md"', r'knowl id="\1"', content)
    
    # Fix escaped asterisks in LaTeX
    content = re.sub(r'\\\*', '*', content)
    
    # Clean LaTeX from YAML description
    def clean_desc(match):
        desc = match.group(1)
        desc = re.sub(r'\\\\+[a-zA-Z]*', '', desc)
        desc = re.sub(r'\\[a-zA-Z]+', '', desc)
        desc = re.sub(r'\\[^a-zA-Z]', '', desc)
        desc = re.sub(r'\$[^$]*\$', '', desc)
        desc = re.sub(r'\s+', ' ', desc).strip()
        return f'description: "{desc}"'
    content = re.sub(r'^description:\s*"([^"]*)"', clean_desc, content, flags=re.MULTILINE)
    
    return content

def fix_directory(dir_path):
    """Fix all .md files in a directory."""
    fixed_count = 0
    for filename in os.listdir(dir_path):
        if not filename.endswith('.md'):
            continue
        
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r') as f:
            original = f.read()
        
        fixed = fix_content(original)
        
        if fixed != original:
            with open(filepath, 'w') as f:
                f.write(fixed)
            fixed_count += 1
    
    return fixed_count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/fix-knowls.py content/SECTION/")
        sys.exit(1)
    
    dir_path = sys.argv[1]
    if not os.path.isdir(dir_path):
        print(f"Error: {dir_path} is not a directory")
        sys.exit(1)
    
    fixed = fix_directory(dir_path)
    total = len([f for f in os.listdir(dir_path) if f.endswith('.md')])
    print(f"Fixed {fixed}/{total} files in {dir_path}")
