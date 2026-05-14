# Law Wiki Bidding v2

Knowledge base về Luật Đấu thầu Việt Nam, xây dựng theo pattern LLM Wiki.

## Nội dung

Wiki này bao gồm:
- **Luật Đấu thầu 2023** (hợp nhất Luật 22/2023, 57/2024, 90/2025)
- 10 chương, 98 điều
- **Nghị định 214/2025/NĐ-CP** (1 index + 14 chương)
- **Thông tư 79/2025/TT-BTC** (1 index + 4 chương, 35 điều)
- 35 concepts (khái niệm pháp lý, gồm 4 concept từ NĐ 214)
- Concept-based relationship graph (related_articles)
- Liên kết 3 tầng: Luật ↔ Nghị định ↔ Thông tư qua section `Văn bản hướng dẫn`
- Phân tích chi tiết các khái niệm, thủ tục, quy trình

## Cấu trúc

```
wiki/
├── INDEX.md              # Mục lục chính
├── LOG.md                # Lịch sử thay đổi
├── articles/             # Phân tích từng điều luật (100+ files)
├── chapters/             # 10 chương luật
├── concepts/             # Khái niệm pháp lý
├── laws/                 # Văn bản luật gốc
├── documents/            # Văn bản hướng dẫn (NĐ, TT)
├── procedures/           # Quy trình thủ tục
└── syntheses/            # Tổng hợp so sánh
```

## Sử dụng

### 1. Với Hermes Agent

```bash
hermes
/law-wiki-bidding "điều kiện áp dụng chỉ định thầu?"
```

### 2. Với Obsidian

Mở folder này làm vault → Graph View để xem mối quan hệ giữa các khái niệm.

### 3. Query trực tiếp

Đọc `wiki/INDEX.md` để tìm trang liên quan, sau đó đọc các file markdown trong `wiki/`.

## Phiên bản

- **v1.3.0** (2026-05-14): Ingest Thông tư 79/2025/TT-BTC
  - Added `wiki/documents/tt-79-2025.md` (document index)
  - Added 4 chapter files in `wiki/documents/tt-79-2025/`
  - Patched 12 law articles with TT-79 guidance links
  - Bidirectional links: Law ↔ TT-79 ↔ ND214
  - Legal hierarchy complete: Law (nền) → ND214 (chi tiết Luật) → TT-79 (chi tiết ND214)

- **v1.2.0** (2026-05-12): Ingest Nghị định 214/2025 + Luật↔NĐ linking
  - Added `wiki/documents/nd-214-2025.md` (document index)
  - Added 14 chapter files in `wiki/documents/nd-214-2025/`
  - Added 4 concepts from Điều 2 NĐ 214:
    - `chao-gia-truc-tuyen`
    - `dau-thau-ben-vung`
    - `gia-trung-thau`
    - `mua-sam-truc-tuyen`
  - Patched 27 law articles with `## Văn bản hướng dẫn` links to NĐ 214

- **v1.1.0** (2026-05-10): Concept-based relationship graph
  - 98 articles với `related_articles` field
  - 31 concepts (khái niệm pháp lý)
  - Cross-chapter process flow links
  - Điều 4 as central hub (93 connections)

- **v1.0.0** (2026-05-04): Phiên bản đầu tiên
  - 98 articles
  - 10 chapters
  - 31 concepts
  - Cross-references đầy đủ

## License

MIT
