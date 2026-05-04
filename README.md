# Law Wiki Bidding v2

Knowledge base về Luật Đấu thầu Việt Nam, xây dựng theo pattern LLM Wiki.

## Nội dung

Wiki này bao gồm:
- **Luật Đấu thầu 2023** (hợp nhất Luật 22/2023, 57/2024, 90/2025)
- 10 chương, 98 điều
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

- **v1.0.0** (2026-05-04): Phiên bản đầu tiên
  - 100+ articles
  - 10 chapters
  - 17 concepts
  - Cross-references đầy đủ

## License

MIT
