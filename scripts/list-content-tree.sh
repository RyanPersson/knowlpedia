#!/bin/bash
# List all files under content/ in a compact, LLM-friendly format
# Output: tmp/content-tree.txt

OUTPUT="tmp/content-tree.txt"
mkdir -p tmp

{
    echo "# Content Structure ($(date +%Y-%m-%d))"
    echo ""

    total=0
    for dir in content/*/; do
        if [ -d "$dir" ]; then
            section=$(basename "$dir")
            files=$(find "$dir" -maxdepth 1 -name "*.md" ! -name "_index.md" -exec basename {} .md \; | sort)
            count=$(echo "$files" | grep -c .)
            total=$((total + count))

            echo "## $section ($count)"
            echo "$files"
            echo ""
        fi
    done

    echo "---"
    echo "Total: $total knowls across $(ls -d content/*/ | wc -l | tr -d ' ') sections"
} > "$OUTPUT"

echo "Written to $OUTPUT"
wc -l < "$OUTPUT" | xargs -I{} echo "{} lines (was ~1578 with full paths)"
