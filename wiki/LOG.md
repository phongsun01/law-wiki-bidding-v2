## 2026-09-09 - Tier 7: Xây dựng 15 trang Syntheses Tổng hợp thực tiễn (COMPLETE)

**Output:** 15 chuyên đề tổng hợp chuyên sâu tại `wiki/syntheses/`
**Đúc kết từ:** 1.570 tình huống giải đáp thực tế của Cổng TTĐT Chính phủ
**Navigation:** Đã tạo `wiki/syntheses/INDEX.md` và cập nhật `wiki/INDEX.md`
**Chi phí token:** 0 tokens

---

## 2026-09-09 - Tier 6: Ingest 1.570 Q&A Chính phủ (COMPLETE)

**Source:** `raw/qa-chinhphu/` (1570 files)
**Strategy:** Hybrid Technical Ingest (0 Token)
**Output:**
- Đã tạo 1570 trang `wiki/qa/` với liên kết hai chiều
- Đã cập nhật mục 'Tình huống thực tiễn' vào 96 Điều luật
- Đã tạo `wiki/INDEX-QA.md`
- Chi phí token: 0 tokens

---

# Law-Wiki Bidding v2 - Change Log

## 2026-05-14 - Tier 5.2: Ingest Thông tư 80/2025 (COMPLETE)

### TT-80/2025/TT-BTC Ingest

**Date:** 2026-05-14  
**Source:** `/Users/xitrum/Library/CloudStorage/Box-Box/Tai lieu - Phong/Van ban phap luat/TT-80-BTC.md`  
**Strategy:** Single document file (no chapter structure)

**Output:**

1. **Single document file created:**
   - `documents/tt-80-2025.md`
   - Frontmatter: type, category, doc_type, code, title, implements, related_documents
   - Implements: Luật Đấu thầu 2023
   - Related: ND 214/2025, TT 79/2025

2. **Content:**
   - 6 articles (no chapter structure)
   - Mẫu hồ sơ yêu cầu (chỉ định thầu, mua sắm trực tiếp)
   - Mẫu báo cáo đánh giá (đấu thầu không qua mạng)
   - Mẫu báo cáo thẩm định
   - Mẫu kiểm tra hoạt động đấu thầu
   - Báo cáo tình hình thực hiện

**Structure difference:**
- TT-79: hub + 4 chapter files (35 articles)
- TT-80: single document file (6 articles)

**Thống kê:**
- TT-80 pages: 1 (single document)
- Total articles: 6
- Size: 175 lines

**Time:** ~30 minutes  
**Token:** ~15,000 tokens

**Next:** Complete legal document set (Law + ND214 + TT-79 + TT-80)

---

## 2026-05-14 - Tier 5.1: Ingest Thông tư 79/2025 (COMPLETE)

### TT-79/2025/TT-BTC Ingest

**Date:** 2026-05-14  
**Source:** `/Users/xitrum/Library/CloudStorage/Box-Box/Tai lieu - Phong/Van ban phap luat/TT-79-BTC.md`  
**Strategy:** Hub + chapter structure (không tách điều riêng)

**Output:**

1. **Hub file created:**
   - `documents/tt-79-2025.md`
   - Frontmatter: type, category, doc_type, code, title, implements, related_documents
   - Implements: Luật Đấu thầu 2023
   - Related: ND 214/2025

2. **Chapter files created (4):**
   - `documents/tt-79-2025/chuong-01.md` - Quy định chung (Điều 1-10)
   - `documents/tt-79-2025/chuong-02.md` - Cung cấp, đăng tải thông tin (Điều 11-25)
   - `documents/tt-79-2025/chuong-03.md` - Nội dung mẫu hồ sơ đấu thầu (Điều 26-32)
   - `documents/tt-79-2025/chuong-04.md` - Tổ chức thực hiện (Điều 33-35)

3. **Tier 1 - Chapter mapping:**
   - Ch I → Law [1,2,4,52,78,79,82] + ND214 [ch-01, ch-13]
   - Ch II → Law [7,8,52,78,79] + ND214 [ch-01, ch-13]
   - Ch III → Law [5,44,65,82] + ND214 [ch-02, ch-13]
   - Ch IV → ND214 [ch-01, ch-13]

4. **Tier 2 - Article patching (3 batches):**
   - Batch A (Điều 1-30): 6 articles patched
   - Batch B (Điều 31-60): 2 articles patched
   - Batch C (Điều 61-98): 4 articles patched
   - Total: 12 Law articles với TT-79 guidance links

**Bidirectional links:**
- Law articles → TT-79 chapters (via "Văn bản hướng dẫn" section)
- TT-79 chapters → Law articles (via related_law_articles frontmatter)
- TT-79 chapters → ND214 chapters (via related_decree_sections)

**Legal hierarchy:**
- Law (nền) → ND214 (chi tiết Luật) → TT-79 (chi tiết ND214)

**Thống kê:**
- TT-79 pages: 5 (1 hub + 4 chapters)
- Total articles: 35 (across 4 chapters)
- Law articles patched: 12
- Cross-references: ~16 links (Law ↔ TT-79)

**Time:** ~2 hours  
**Token:** ~70,000 tokens

**Next:** Ingest TT-80/2025 (if needed)

---

## 2026-05-03 - Tier 3.1: Extract Concepts (COMPLETE)

### Concept Extraction from Điều 4

**Date:** 2026-05-03 14:35 UTC  
**Source:** [[dieu-4-giai-thich-tu-ngu]] (33 khoản định nghĩa)  
**Strategy:** Manual extraction theo schema v2.3

**Concepts created:** 17/17 planned ✅

### Chủ thể (5 concepts)
1. ✅ [[chu-dau-tu]] - Chủ đầu tư (Khoản 2)
2. ✅ [[nha-thau]] - Nhà thầu (Khoản 26)
3. ✅ [[nha-thau-phu]] - Nhà thầu phụ (Khoản 27)
4. ✅ [[co-quan-co-tham-quyen]] - Cơ quan có thẩm quyền (Khoản 2a)
5. ✅ [[nguoi-co-tham-quyen]] - Người có thẩm quyền (Khoản 24)

### Đối tượng đấu thầu (3 concepts)
6. ✅ [[goi-thau]] - Gói thầu (Khoản 15)
7. ✅ [[hang-hoa]] - Hàng hóa (Khoản 17)
8. ✅ [[xay-lap]] - Xây lắp (Khoản 33)

### Quy trình (3 concepts)
9. ✅ [[dau-thau]] - Đấu thầu (Khoản 8)
10. ✅ [[dau-thau-qua-mang]] - Đấu thầu qua mạng (Khoản 9)
11. ✅ [[he-thong-mang-dau-thau-quoc-gia]] - Hệ thống mạng đấu thầu quốc gia (Khoản 18)

### Hồ sơ (4 concepts)
12. ✅ [[ho-so-moi-thau]] - Hồ sơ mời thầu (Khoản 21)
13. ✅ [[ho-so-du-thau]] - Hồ sơ dự thầu (Khoản 23)
14. ✅ [[ho-so-yeu-cau]] - Hồ sơ yêu cầu (Khoản 22)
15. ✅ [[ho-so-de-xuat]] - Hồ sơ đề xuất (Khoản 23)

### Dịch vụ (2 concepts)
16. ✅ [[dich-vu-tu-van]] - Dịch vụ tư vấn (Khoản 4)
17. ✅ [[dich-vu-phi-tu-van]] - Dịch vụ phi tư vấn (Khoản 5)

**Skipped concepts:**
- ❌ ben-moi-thau (Khoản 1) - Không focus vào đầu tư
- ❌ nha-dau-tu (Khoản 25) - Không focus vào đầu tư

**Content structure per concept:**
- Định nghĩa (trích nguyên văn từ Điều 4)
- Vai trò/Chức năng (nếu là chủ thể)
- Quyền hạn (nếu có)
- Trách nhiệm (nếu có)
- Điều liên quan (cross-references)
- Ví dụ áp dụng (case studies)
- Phân biệt (so sánh với concepts tương tự)

**Stats:**
- Total concepts: 17
- Total words: ~15,000 words
- Avg length: ~940 words/concept
- Cross-references: ~80 wiki links
- Time: ~30 minutes

**Next:** Tier 3.2 - Find related articles dựa trên concept graph

---

## 2026-05-03 - Schema v2.3 Migration (COMPLETE)

### Migration from v2.0 to v2.3

**Date:** 2026-05-03 10:05 UTC (initial), 10:20 UTC (fixed re-run)  
**Script:** `/Users/xitrum/projects/claude-cli/LAW-WIKI-BIDDING/scripts/migrate-to-v2.3.py`  
**Strategy:** Automated migration with regex parsing (no LLM calls)

**Changes:**
- Added markdown anchors to khoản: `### Khoản 1. Title {#khoan-1}`
- Added markdown anchors to điểm: `- **Điểm a.** Content {#khoan-1-diem-a}`
- Added frontmatter field: `total_clauses`
- Added frontmatter field: `anchors` array
- Updated citation field with `anchor` property

**Bug fix (10:20 UTC):**
- Fixed regex pattern to support both `Khoản 1.` and `Khoản 1:` formats
- Re-ran migration: 69 → 85 articles migrated

**Final Results:**
- ✅ Migrated: 85 articles (with khoản/điểm structure)
- ⚠️  Skipped: 15 articles (no khoản - single paragraph articles)
- ✅ Clause anchors: 1,017
- ✅ Point anchors: 404
- ✅ Total anchors: 1,421
- ✅ Malformed anchors: 0
- ✅ Backup created: `wiki.backup.v2.0.20260503_170555`

**Performance:**
- Execution time: ~10 seconds (each run)
- Token cost: 0 (pure Python regex)
- Files processed: 100
- Success rate: 85% (85/100)

**Validation:**
```bash
# Anchor count
grep -roh '{#khoan-' wiki/articles/*.md | wc -l  # 1,017
grep -roh '{#khoan-.*-diem-' wiki/articles/*.md | wc -l  # 404

# Malformed check
grep -oh '{#[^}]*}' wiki/articles/*.md | grep -v '{#khoan-[0-9]' | grep -v 'diem-'  # 0 results
```

**Example anchor links:**
- `[[dieu-23-chi-dinh-thau#khoan-1-diem-a]]` - Jump to điểm a khoản 1
- `[[dieu-3-ap-dung-luat#khoan-7-diem-g]]` - Jump to điểm g khoản 7

**Current state:**
- Articles (85): Schema v2.3 ✅ (with embedded anchors)
- Articles (15): Schema v2.0 (no khoản structure - correct)
- Chapters (10): Old schema (wiki links)
- Law (1): Old schema (type, category, name)

---

## 2026-05-01 - Tier 1: Law-level Pass (COMPLETE)

### Ingest Luật Đấu thầu Hợp nhất - Tier 1

**Source:** `/Users/xitrum/Library/CloudStorage/Box-Box/Tai lieu - Phong/Van ban phap luat/luat-22-25-90.md`  
**Target:** `/Users/xitrum/law-wiki-bidding-v2/`  
**Strategy:** 3-tier ingest theo schema v2.0

**Tier 1 Output:**

1. **Law file created:**
   - `laws/luat-dau-thau-2023.md`
   - Frontmatter: type, category, code, issued_by, issued_date, effective_date, replaces, amended_by
   - Structure: 10 chương, 98 điều
   - Văn bản liên quan: NĐ 214/2025, TT 79/2025, TT 80/2025
   - Note: Bộ Kế hoạch và Đầu tư → Bộ Tài chính

2. **Chapter files created (10):**
   - `chapters/chuong-1-quy-dinh-chung.md` (Điều 1-8)
   - `chapters/chuong-2-hinh-thuc-phuong-thuc.md` (Điều 9-30)
   - `chapters/chuong-3-ke-hoach.md` (Điều 31-42)
   - `chapters/chuong-4-quy-trinh-thu-tuc.md` (Điều 43-54)
   - `chapters/chuong-5-mua-sam-tap-trung.md` (Điều 55-62)
   - `chapters/chuong-6-phuong-phap-danh-gia.md` (Điều 63-76)
   - `chapters/chuong-7-hop-dong.md` (Điều 77-84)
   - `chapters/chuong-8-trach-nhiem.md` (Điều 85-90)
   - `chapters/chuong-9-quan-ly-nha-nuoc.md` (Điều 91-95)
   - `chapters/chuong-10-dieu-khoan-thi-hanh.md` (Điều 96-98)

3. **INDEX.md created:**
   - Laws section (1 law)
   - Chapters section (10 chapters)
   - Articles index structure (98 điều grouped by chapter)
   - Statistics

4. **LOG.md created:**
   - This file

**Thống kê:**
- Laws: 1 ✅
- Chapters: 10 ✅
- Articles: 0 (98 planned for Tier 2)
- Total pages: 11

**Time:** ~10 minutes  
**Token:** ~5,000 tokens

**Next:** Tier 2 - Article-level pass (98 điều in 10 batches)

---

**Version:** 2.0  
**Created:** 2026-05-01  
**Schema:** law-wiki-bidding-schema-v2.md

---

## 2026-05-01 to 2026-05-02 - Tier 2: Article-level Pass (COMPLETE)

### Ingest 100 Articles - Batches 1-10

**Strategy:** Batch processing theo chương, 10 batches × ~10 điều

**Tier 2 Output:**

1. **Article files created (100):**
   - Batch 1: Điều 1-19 (Chương I) - 19 articles ✅
   - Batch 2: Điều 20-29 + 29a, 29b (Chương II Mục 1) - 12 articles ✅
   - Batch 3: Điều 30-39 (Chương II Mục 2) - 10 articles ✅
   - Batch 4: Điều 40-49 (Chương III-IV) - 10 articles ✅
   - Batch 5: Điều 50-60 (Chương IV-VI) - 11 articles ✅
   - Batch 6: Điều 61-70 (Chương VI-VII) - 10 articles ✅
   - Batch 7: Điều 71-80 (Chương VII-VIII) - 10 articles ✅
   - Batch 8: Điều 81-88 (Chương VIII) - 8 articles ✅
   - Batch 9: Điều 89-94 (Chương IX) - 6 articles ✅
   - Batch 10: Điều 95-98 (Chương X) - 4 articles ✅

2. **Frontmatter fields (11 per article):**
   - law_id, article_number, title, chapter, chapter_title
   - effective_date, last_amended, amendment_history
   - status, summary, related_articles

3. **Naming convention:**
   - Format: `dieu-{num}-{slug}.md`
   - Example: `dieu-20-hinh-thuc-lua-chon.md`

4. **Cross-references added:**
   - Minimum 3 wiki links per article (schema v2.0 requirement)
   - Batch 9-10 articles enhanced with internal links
   - Hierarchical links: Article → Chapter → Law

5. **Chapter files updated:**
   - All 10 chapter files updated with article lists
   - Fixed duplicate chapter naming issues

6. **Quality checks:**
   - Lint: 0 broken links
   - Lint: 0 orphan pages
   - Lint: All articles meet minimum 3 wiki-link requirement
   - Obsidian config: `raw/` folder excluded from graph

**Thống kê:**
- Laws: 1 ✅
- Chapters: 10 ✅
- Articles: 100 ✅ (98 base + dieu-29a + dieu-29b)
- Total pages: 111
- Wiki links: ~350+
- Coverage: 100%

**Time:** ~6 hours (10 batches)  
**Token:** ~50,000 tokens

**Issues fixed:**
- Removed 8 misplaced files from root directory
- Fixed chapter numbering conflicts (chuong-8 vs chuong-9)
- Added wiki links to Batch 9-10 articles for schema compliance

**Next:** Tier 3 - Deep cross-reference pass + concept extraction

---

**Last updated:** 2026-05-02 01:08 UTC
