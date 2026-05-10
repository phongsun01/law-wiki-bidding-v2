# Law Wiki Bidding - Hướng dẫn cho Claude

## Ngôn ngữ giao tiếp

**QUAN TRỌNG:** Luôn giao tiếp bằng tiếng Việt khi làm việc với repo này.

## Về dự án

Knowledge base về Luật Đấu thầu Việt Nam 2023 (hợp nhất Luật 22/2023, 57/2024, 90/2025), xây dựng theo pattern LLM Wiki.

## Cấu trúc

```
wiki/
├── articles/      # 98 điều luật với concept-based relationships
├── chapters/      # 10 chương
├── concepts/      # 31 khái niệm pháp lý
├── laws/          # Văn bản luật gốc
└── INDEX.md       # Mục lục chính
```

## Schema hiện tại

**Schema v2.3** - Embedded Clause/Point với markdown anchors

### Article frontmatter

```yaml
---
law_id: luat-dau-thau-2023
article_number: 30
title: Phương thức một giai đoạn một túi hồ sơ
chapter: 2
chapter_title: Lựa chọn nhà thầu, nhà đầu tư
effective_date: 2024-01-01
last_amended: 2024-01-01
amendment_history: Luật 22/2023/QH15
status: active
summary: "..."
related_articles: [4, 20, 21, 22, 31, 32]
total_clauses: 3
anchors: [khoan-1, khoan-2, khoan-3]
---
```

### Anchor format

- Khoản: `### Khoản 1. Title {#khoan-1}`
- Điểm: `- **Điểm a.** Content {#khoan-1-diem-a}`

## Quy tắc làm việc

1. **Luôn dùng tiếng Việt** khi giao tiếp
2. **Không tạo file riêng** cho khoản/điểm - embed trong article với anchors
3. **Link format:** `[[dieu-X-slug]]` hoặc `[[dieu-X-slug#khoan-Y]]`
4. **Concept links:** `[[chu-dau-tu]]`, `[[nha-thau]]`, etc.
5. **Related articles:** Dùng integer array `[4, 20, 21]`, không dùng wiki links

## Trạng thái hiện tại

- ✅ Tier 1: Law-level complete
- ✅ Tier 2: Article-level complete (98 articles)
- ✅ Tier 3.1: Concepts complete (31 concepts)
- ✅ Tier 3.2: Related articles complete (all 11 batches)
- ⏳ Post-processing: Chưa bắt đầu
- ⏳ Next steps: Chưa bắt đầu

## Tham khảo

- Guide: `/Users/xitrum/projects/claude-cli/LAW-WIKI-BIDDING/INGEST-LUAT-DAU-THAU-GUIDE.md`
- Prompts: `/Users/xitrum/projects/claude-cli/LAW-WIKI-BIDDING/prompt-*.txt`
- Repository: https://github.com/phongsun01/law-wiki-bidding-v2
