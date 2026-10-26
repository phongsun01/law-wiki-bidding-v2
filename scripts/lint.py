import sys
import re
from pathlib import Path
import yaml

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"

def run_lint():
    print("=" * 60)
    print("🔍 RUNNING LAW WIKI BIDDING LINTER")
    print("=" * 60)
    
    errors = []
    warnings = []
    
    # Collect all markdown files
    all_files = list(WIKI_DIR.rglob("*.md"))
    file_stems = {}
    file_rel_paths = {}
    
    for f in all_files:
        rel = f.relative_to(WIKI_DIR).as_posix()
        stem = f.stem
        if stem not in file_stems:
            file_stems[stem] = []
        file_stems[stem].append(f)
        rel_no_ext = rel[:-3] if rel.endswith(".md") else rel
        file_rel_paths[rel_no_ext] = f
        file_rel_paths[rel] = f
        
    print(f"Total markdown files indexed: {len(all_files)}")
    
    # 1. Wikilinks and Anchors verification
    wikilink_pattern = re.compile(r"\[\[([^\]\|#]+)(?:#([^\]\|]+))?(?:\|([^\]]+))?\]\]")
    incoming_links = {f: 0 for f in all_files}
    total_wikilinks = 0
    
    for f in all_files:
        content = f.read_text(encoding="utf-8")
        rel_f = f.relative_to(WIKI_DIR).as_posix()
        
        # Check for placeholder wildcards
        if re.search(r"\[\[dieu-\d+[a-z]?-\*", content):
            errors.append(f"[{rel_f}] Contains uncleaned wildcard wikilink: dieu-XX-*")
            
        for m in wikilink_pattern.finditer(content):
            total_wikilinks += 1
            target = m.group(1).strip()
            anchor = m.group(2).strip() if m.group(2) else None
            
            target_clean = target.replace("\\", "/")
            target_stem = Path(target_clean).name
            target_no_ext = target_clean[:-3] if target_clean.endswith(".md") else target_clean
            
            target_file = None
            if target_no_ext in file_rel_paths:
                target_file = file_rel_paths[target_no_ext]
            elif target_clean in file_rel_paths:
                target_file = file_rel_paths[target_clean]
            elif target_stem in file_stems:
                target_file = file_stems[target_stem][0]
                
            if not target_file:
                errors.append(f"[{rel_f}] Broken link: [[{target}]]")
            else:
                incoming_links[target_file] += 1
                if anchor:
                    # Verify anchor
                    target_content = target_file.read_text(encoding="utf-8")
                    anchor_slug = anchor.lower().replace(" ", "-")
                    found = False
                    if f"id='{anchor}'" in target_content or f'id="{anchor}"' in target_content:
                        found = True
                    elif f"name='{anchor}'" in target_content or f'name="{anchor}"' in target_content:
                        found = True
                    elif f"#{anchor}" in target_content or f"{{#{anchor}}}" in target_content:
                        found = True
                    else:
                        for line in target_content.splitlines():
                            if line.startswith("#"):
                                h_text = line.lstrip("#").strip().lower()
                                h_slug = re.sub(r"[^\w\s-]", "", h_text).replace(" ", "-")
                                if anchor_slug in h_slug or anchor in line:
                                    found = True
                                    break
                    if not found:
                        errors.append(f"[{rel_f}] Broken anchor: [[{target}#{anchor}]] in {target_file.name}")

    print(f"Scanned {total_wikilinks} wikilinks across wiki.")
    
    # 2. Check Frontmatter and related_articles
    for f in (WIKI_DIR / "articles").glob("*.md"):
        rel_f = f.relative_to(WIKI_DIR).as_posix()
        txt = f.read_text(encoding="utf-8")
        if not txt.startswith("---"):
            errors.append(f"[{rel_f}] Missing frontmatter")
            continue
        parts = txt.split("---", 2)
        if len(parts) < 3:
            errors.append(f"[{rel_f}] Malformed frontmatter")
            continue
        try:
            fm = yaml.safe_load(parts[1]) or {}
        except Exception as e:
            errors.append(f"[{rel_f}] Invalid YAML frontmatter: {e}")
            continue
            
        # Required article keys
        for key in ["law_id", "article_number", "title", "chapter"]:
            if key not in fm:
                errors.append(f"[{rel_f}] Missing required frontmatter key: {key}")
                
        # related_articles must be list of integers
        rel_arts = fm.get("related_articles")
        if rel_arts is not None:
            if not isinstance(rel_arts, list):
                errors.append(f"[{rel_f}] related_articles must be a list of integers")
            else:
                for x in rel_arts:
                    if not isinstance(x, int):
                        errors.append(f"[{rel_f}] related_articles item '{x}' is not an integer")
                if len(rel_arts) != len(set(rel_arts)):
                    errors.append(f"[{rel_f}] duplicate numbers in related_articles: {rel_arts}")
                    
        # Check tags
        if not fm.get("tags"):
            errors.append(f"[{rel_f}] Missing tags")

    # 3. Check Meaningful Orphans (Articles, Concepts, Chapters, Documents)
    # Note: QA files are allowed to be wikilink-orphans (accessible via related_articles and INDEX-QA)
    allowed_orphan_prefixes = ("qa/", "syntheses/INDEX")
    meaningful_orphans = []
    for f, count in incoming_links.items():
        rel = f.relative_to(WIKI_DIR).as_posix()
        if count == 0:
            if not rel.startswith(allowed_orphan_prefixes) and rel not in ["INDEX.md", "LOG.md", "SCHEMA.md", "INDEX-QA.md"]:
                meaningful_orphans.append(rel)
                
    if meaningful_orphans:
        for o in meaningful_orphans:
            errors.append(f"Meaningful orphan file without incoming wikilink: {o}")

    # 4. Check INDEX.md sync
    index_content = (WIKI_DIR / "INDEX.md").read_text(encoding="utf-8")
    for a in (WIKI_DIR / "articles").glob("*.md"):
        if a.stem not in index_content:
            warnings.append(f"Article {a.stem} not linked in INDEX.md")

    # Output Results
    print("\n" + "=" * 60)
    print("📊 LINT SUMMARY")
    print("=" * 60)
    print(f"Total Errors  : {len(errors)}")
    print(f"Total Warnings: {len(warnings)}")
    
    if warnings:
        print("\n⚠️ WARNINGS:")
        for w in warnings:
            print(f"  - {w}")
            
    if errors:
        print("\n❌ ERRORS FOUND:")
        for e in errors:
            print(f"  - {e}")
        print("\n❌ LINTER FAILED!")
        return 1
    else:
        print("\n✅ ALL CHECKS PASSED! Wiki is clean, robust and consistent.")
        return 0

if __name__ == "__main__":
    sys.exit(run_lint())
