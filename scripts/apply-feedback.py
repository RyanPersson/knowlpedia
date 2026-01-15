#!/usr/bin/env python3
"""
Apply feedback tags from the log file to knowl files.
Run after voting session: python3 scripts/apply-feedback.py
"""
import os
import re

FEEDBACK_FILE = "research/flagged-knowls.txt"
CONTENT_DIR = "content"

def add_tag(filepath, new_tag):
    """Add a tag to knowl's YAML front matter"""
    with open(filepath, 'r') as f:
        content = f.read()

    # Check if already has this tag
    if f'"{new_tag}"' in content or f"'{new_tag}'" in content or f'- {new_tag}' in content:
        return False

    # Parse front matter
    if not content.startswith('---'):
        return False

    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

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
    return True

def apply_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        print(f"No feedback file found: {FEEDBACK_FILE}")
        return

    with open(FEEDBACK_FILE, 'r') as f:
        lines = f.readlines()

    if not lines:
        print("Feedback log is empty")
        return

    stats = {'upvoted': 0, 'needs-review': 0, 'skipped': 0, 'not_found': 0}

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Parse: "2025-01-13 22:00:00 | 👍 | section/knowl-id | optional note"
        parts = line.split(' | ')
        if len(parts) < 3:
            continue

        vote_symbol = parts[1]
        path_part = parts[2]

        # Extract section and knowl_id
        if '/' not in path_part:
            continue
        section, knowl_id = path_part.split('/', 1)

        knowl_path = os.path.join(CONTENT_DIR, section, f"{knowl_id}.md")
        tag = 'upvoted' if vote_symbol == '👍' else 'needs-review'

        if os.path.exists(knowl_path):
            if add_tag(knowl_path, tag):
                print(f"  {vote_symbol} {section}/{knowl_id}")
                stats[tag] += 1
            else:
                stats['skipped'] += 1
        else:
            stats['not_found'] += 1

    print(f"\nApplied: {stats['upvoted']} upvoted, {stats['needs-review']} needs-review")
    if stats['skipped']:
        print(f"Skipped (already tagged): {stats['skipped']}")
    if stats['not_found']:
        print(f"Not found: {stats['not_found']}")

if __name__ == '__main__':
    apply_feedback()
