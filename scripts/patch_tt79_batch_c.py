#!/usr/bin/env python3
"""
Patch Law articles (Điều 61-98) to add TT-79 guidance links.
Batch C: Articles 61-98
"""

import os
import re

# Mapping: Law article → TT-79 chapters
ARTICLE_TO_TT79 = {
    65: ["documents/tt-79-2025/chuong-03"],
    78: ["documents/tt-79-2025/chuong-02"],
    79: ["documents/tt-79-2025/chuong-02"],
    82: ["documents/tt-79-2025/chuong-01", "documents/tt-79-2025/chuong-03"],
}

WIKI_DIR = "/Users/xitrum/law-wiki-bidding-v2/wiki/articles"

def find_article_file(article_num):
    """Find article file by number."""
    for fname in os.listdir(WIKI_DIR):
        if fname.startswith(f"dieu-{article_num:02d}-") or fname.startswith(f"dieu-{article_num}-"):
            return os.path.join(WIKI_DIR, fname)
    return None

def patch_article(article_num, tt79_chapters):
    """Add 'Văn bản hướng dẫn' section to article file."""
    fpath = find_article_file(article_num)
    if not fpath:
        print(f"⚠️  Article {article_num} file not found")
        return False

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already patched
    if "## Văn bản hướng dẫn" in content:
        print(f"✓  Article {article_num} already patched")
        return True

    # Build guidance section
    guidance_lines = ["", "## Văn bản hướng dẫn", ""]
    for ch in tt79_chapters:
        guidance_lines.append(f"- [[{ch}]]")
    guidance_section = "\n".join(guidance_lines) + "\n"

    # Insert before "## Điều liên quan" or at end
    if "## Điều liên quan" in content:
        content = content.replace("## Điều liên quan", guidance_section + "## Điều liên quan")
    else:
        content = content.rstrip() + "\n" + guidance_section

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓  Patched Article {article_num}")
    return True

def main():
    print("Patching Batch C (Điều 61-98)...")
    success = 0
    for article_num, tt79_chapters in sorted(ARTICLE_TO_TT79.items()):
        if 61 <= article_num <= 98:
            if patch_article(article_num, tt79_chapters):
                success += 1
    print(f"\n✓ Patched {success}/{len([a for a in ARTICLE_TO_TT79 if 61 <= a <= 98])} articles in Batch C")

if __name__ == "__main__":
    main()
