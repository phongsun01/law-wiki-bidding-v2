# Law Wiki Bidding v2

Knowledge base về Luật Đấu thầu Việt Nam, xây dựng theo pattern LLM Wiki.

## Nội dung

Wiki này bao gồm:
- **Luật Đấu thầu 2023** (hợp nhất Luật 22/2023, 57/2024, 90/2025)
- 10 chương, 98 điều
- **Nghị định 214/2025/NĐ-CP** (1 index + 14 chương)
- **Thông tư 79/2025/TT-BTC** (1 index + 4 chương, 35 điều)
- **Thông tư 80/2025/TT-BTC** (1 document, 6 điều)
- **1.570 Tình huống thực tế (Q&A)** trích xuất và chuẩn hóa từ Cổng TTĐT Chính phủ (Bộ KH&ĐT, Bộ Tài chính giải đáp)
- **15 Chuyên đề Tổng hợp thực tiễn (Syntheses)** đúc kết tiền lệ và cẩm nang xử lý
- 35 concepts (khái niệm pháp lý, gồm 4 concept từ NĐ 214)
- Concept-based relationship graph (related_articles)
- Liên kết 3 tầng: Luật ↔ Nghị định/Thông tư ↔ Tình huống thực tiễn (Q&A) & Cẩm nang (Syntheses)
- Phân tích chi tiết các khái niệm, thủ tục, quy trình

## Cấu trúc

`
wiki/
├── INDEX.md              # Mục lục chính toàn bộ wiki
├── INDEX-QA.md           # Mục lục 1.570 tình huống thực tiễn theo Điều luật
├── LOG.md                # Lịch sử thay đổi wiki
├── SCHEMA.md             # Quy chuẩn cấu trúc wiki
├── articles/             # Phân tích từng điều luật (100+ files)
├── chapters/             # 10 chương luật
├── concepts/             # 35 khái niệm pháp lý
├── laws/                 # Văn bản luật gốc
├── documents/            # Văn bản hướng dẫn (NĐ 214, TT 79, TT 80)
├── qa/                   # 1.570 tình huống thực tiễn có liên kết 2 chiều
└── syntheses/            # 15 chuyên đề tổng hợp thực tiễn chuyên sâu
`

## Sử dụng

### 1. Với Hermes Agent

`ash
hermes
/law-wiki-bidding "chủ đầu tư có được tự quyết định chỉ định thầu rút gọn không?"
`

### 2. Với Obsidian

Mở folder này làm vault → Graph View để xem mạng lưới quan hệ giữa Điều luật, Khái niệm và 1.570 tình huống thực tế.

### 3. Query trực tiếp

Đọc wiki/INDEX.md, wiki/INDEX-QA.md hoặc wiki/syntheses/INDEX.md để tìm kiếm thông tin nhanh chóng.

## Phiên bản

- **v2.0.0** (2026-09-09): Triển khai Tầng Thực Tiễn & Cẩm Nang Chuyên Sâu (Q&A & Syntheses)
  - Ingest & liên kết **1.570 bài Q&A thực tế** từ Cổng TTĐT Chính phủ vào wiki/qa/
  - Xây dựng **15 chuyên đề tổng hợp thực tiễn chuyên sâu** tại wiki/syntheses/
  - Ánh xạ liên kết 2 chiều vào 96 Điều luật tại wiki/articles/
  - Tạo mục lục phân loại chuyên đề wiki/INDEX-QA.md và wiki/syntheses/INDEX.md
  - Tối ưu hóa kiến trúc tri thức theo chuẩn Karpathy LLM-Wiki

- **v1.4.0** (2026-05-14): Ingest Thông tư 80/2025/TT-BTC
  - Added wiki/documents/tt-80-2025.md (single document, 6 articles)
  - Covers: mẫu hồ sơ yêu cầu, báo cáo đánh giá, thẩm định, kiểm tra
  - Complete legal document set: Law + ND214 + TT-79 + TT-80

- **v1.3.0** (2026-05-14): Ingest Thông tư 79/2025/TT-BTC
  - Added wiki/documents/tt-79-2025.md (document index)
  - Added 4 chapter files in wiki/documents/tt-79-2025/
  - Patched 12 law articles with TT-79 guidance links
  - Bidirectional links: Law ↔ TT-79 ↔ ND214
  - Legal hierarchy complete: Law (nền) → ND214 (chi tiết Luật) → TT-79 (chi tiết ND214)

- **v1.2.0** (2026-05-12): Ingest Nghị định 214/2025 + Luật↔NĐ linking
  - Added wiki/documents/nd-214-2025.md (document index)
  - Added 14 chapter files in wiki/documents/nd-214-2025/
  - Added 4 concepts from Điều 2 NĐ 214
  - Patched 27 law articles with ## Văn bản hướng dẫn links to NĐ 214

- **v1.1.0** (2026-05-10): Concept-based relationship graph
  - 98 articles với elated_articles field
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