# Law Wiki Bidding v2

Knowledge base về Luật Đấu thầu Việt Nam, xây dựng theo pattern LLM Wiki chuẩn cho AI Agent (Hermes / Muse) và Obsidian.

## Nội dung Kho Tri Thức

Wiki này bao gồm:
- **Luật Đấu thầu 2023** (hợp nhất Luật số 22/2023/QH15, Luật số 57/2024/QH15 và Luật số 90/2025/QH15):
  - 10 chương, **100 điều luật chi tiết** (98 điều gốc + Điều 29a, Điều 29b chèn thêm).
- **Hệ thống Văn bản hướng dẫn thi hành (Documents):**
  - **Nghị định 214/2025/NĐ-CP** (1 hub document + 14 chương quy định chi tiết thi hành Luật).
  - **Nghị định 349/2026/NĐ-CP** (toàn văn 28 điều sửa đổi, bổ sung NĐ 214/2025 và NĐ 32/2019; nâng hạn mức chỉ định thầu lên 1 tỷ, 3 tỷ, 5 tỷ đồng).
  - **Nghị định 24/2024/NĐ-CP** (*Status: superseded* - lưu vết lịch sử phục vụ đối chiếu các tình huống cũ).
  - **Thông tư 79/2025/TT-BTC** (1 hub document + 4 chương, 35 điều quy định về Hệ thống mạng đấu thầu quốc gia).
  - **Thông tư 134/2026/TT-BTC** (1 document, 7 điều quy định chi tiết mẫu hồ sơ yêu cầu chỉ định thầu, báo cáo đánh giá, thẩm định, kiểm tra, giám sát hoạt động đấu thầu; sửa đổi TT 79 và thay thế TT 80).
  - **Thông tư 80/2025/TT-BTC** (*Status: superseded* - hết hiệu lực từ ngày 09/09/2026, lưu vết lịch sử).
- **Khái niệm & Nguyên tắc Pháp lý cốt lõi (Concepts):**
  - **38 concepts** (31 khái niệm pháp lý gốc + 4 khái niệm từ Điều 2 NĐ 214 + 3 chủ thể/nguyên tắc trọng điểm: Bên mời thầu, Nhà đầu tư, Bảo đảm cạnh tranh).
- **Thực tiễn nghiệp vụ & Cẩm nang chuyên sâu:**
  - **1.570 tình huống thực tế (Q&A)** trích xuất và chuẩn hóa từ Cổng TTĐT Chính phủ (Bộ Kế hoạch & Đầu tư, Bộ Tài chính giải đáp).
  - **15 Chuyên đề Tổng hợp thực tiễn (Syntheses)** đúc kết tiền lệ xử lý, tình huống bất khả kháng, phân tích rủi ro và giải pháp nghiệp vụ.
- **Mạng lưới quan hệ:**
  - Concept-based relationship graph với mảng số nguyên `related_articles` phục vụ tra cứu chính xác.
  - Liên kết 3 tầng: Luật ↔ Nghị định / Thông tư ↔ Tình huống thực tiễn (Q&A) & Cẩm nang (Syntheses).

## Cấu trúc Thư mục

```
law-wiki-bidding-v2/
├── wiki/
│   ├── INDEX.md              # Mục lục chính toàn bộ wiki (liệt kê đủ 100 điều luật)
│   ├── INDEX-QA.md           # Mục lục 1.570 tình huống thực tiễn theo Điều luật
│   ├── LOG.md                # Lịch sử thay đổi và nhật ký ingest
│   ├── SCHEMA.md             # Quy chuẩn cấu trúc wiki và hướng dẫn tra cứu
│   ├── articles/             # 100 điều luật (Điều 1 - 98 + Điều 29a, Điều 29b)
│   ├── chapters/             # 10 chương của Luật Đấu thầu
│   ├── concepts/             # 38 khái niệm và chủ thể pháp lý
│   ├── documents/            # Văn bản hướng dẫn (NĐ 214, NĐ 349, NĐ 24, TT 79, TT 80, TT 134)
│   ├── laws/                 # Văn bản luật gốc hợp nhất
│   ├── qa/                   # 1.570 tình huống thực tế
│   └── syntheses/            # 15 chuyên đề tổng hợp thực tiễn chuyên sâu
├── skills/                   # Kỹ năng Muse tra cứu pháp luật đấu thầu
├── raw/                      # Dữ liệu nguồn và văn bản gốc bất biến
└── scripts/                  # Bộ công cụ patch dữ liệu và lint kiểm tra chất lượng
```

## Hướng dẫn Sử dụng & Tra cứu

### 1. Với Hermes Agent / Muse

Hermes Agent tự động kích hoạt kỹ năng `tra-cuu-luat-dau-thau` để hỗ trợ tra cứu:
```bash
hermes
> "Chủ đầu tư có được tự quyết định chỉ định thầu rút gọn theo quy định mới nhất không?"
```
*Lưu ý tra cứu Q&A:* Để tối ưu hóa context, các tình huống Q&A được phân loại qua thuộc tính `related_articles: [X]`. Agent tra cứu câu hỏi liên quan đến Điều X bằng cách tìm kiếm trong `wiki/qa/` hoặc đọc cẩm nang `wiki/syntheses/`.

### 2. Với Obsidian

Mở repository này làm vault trong Obsidian → bật **Graph View** để trực quan hóa mạng lưới quan hệ giữa 100 Điều luật, 38 Khái niệm pháp lý và 15 Chuyên đề tổng hợp.

### 3. Kiểm tra Tính toàn vẹn (Linter)

Chạy công cụ kiểm thử chất lượng trước mỗi lần cập nhật:
```bash
python scripts/lint.py
```

## Lịch sử Phiên bản

- **v2.3.0** (2026-09-14): Ingest Thông tư 134/2026/TT-BTC thay thế toàn diện Thông tư 80/2025/TT-BTC
  - Thêm wiki/documents/tt-134-2026.md (toàn văn 7 điều và phụ lục 8 mẫu hồ sơ yêu cầu chỉ định thầu, 3 mẫu báo cáo đánh giá, 3 mẫu thẩm định, 6 mẫu kiểm tra, 2 mẫu giám sát).
  - Đổi trạng thái wiki/documents/tt-80-2025.md sang status: superseded, gắn cảnh báo thay thế từ 09/09/2026.
  - Cập nhật các điểm sửa đổi đối với Thông tư 79/2025/TT-BTC (Mẫu bảo lãnh dự thầu mới 04A, 04B và nâng hạn mức mua sắm lên 100 triệu đồng).
  - Cập nhật liên kết hướng dẫn tại 15 chuyên đề Syntheses, Luật Đấu thầu, INDEX.md, SCHEMA.md và kỹ năng Muse 	ra-cuu-luat-dau-thau.

- **v2.2.0** (2026-09-14): Chuẩn hóa toàn diện, sửa link/anchor hỏng & nâng cấp Schema
  - Xử lý triệt để 100% link hỏng và anchor hỏng theo đồ thị wikilink.
  - Bổ sung `wiki/documents/nd-24-2024.md` (*status: superseded*) giải quyết triệt để 86 tham chiếu cũ.
  - Bổ sung 3 concepts chủ thể cốt lõi: Bên mời thầu, Nhà đầu tư, Bảo đảm cạnh tranh.
  - Mở rộng `wiki/INDEX.md` liệt kê đầy đủ 100 Điều luật; cập nhật quy định tra cứu Q&A qua `related_articles`.
  - Cập nhật triệt để nội dung hạn mức NĐ 349 (1 tỷ, 3 tỷ, 5 tỷ) trong thân bài Điều 23 và loại bỏ trùng lặp `related_articles`.
  - Viết lại `wiki/SCHEMA.md`, thay thế CLAUDE.md bằng kỹ năng Muse `tra-cuu-luat-dau-thau` và bổ sung `scripts/lint.py`.

- **v2.1.0** (2026-09-14): Ingest Nghị định 349/2026/NĐ-CP sửa đổi Nghị định 214
  - Thêm `wiki/documents/nd-349-2026.md` (toàn văn 28 điều sửa đổi NĐ 214 & NĐ 32).
  - Cập nhật các điểm sửa đổi then chốt vào `wiki/documents/nd-214-2025/` (Chương I, Chương V).
  - Cập nhật cẩm nang Syntheses theo các hạn mức chỉ định thầu mới.

- **v2.0.0** (2026-09-09): Triển khai Tầng Thực Tiễn & Cẩm Nang Chuyên Sâu (Q&A & Syntheses)
  - Ingest & liên kết 1.570 bài Q&A thực tế từ Cổng TTĐT Chính phủ vào `wiki/qa/`.
  - Xây dựng 15 chuyên đề tổng hợp thực tiễn chuyên sâu tại `wiki/syntheses/`.
  - Tạo mục lục phân loại chuyên đề `wiki/INDEX-QA.md` và `wiki/syntheses/INDEX.md`.

- **v1.4.0** (2026-05-14): Ingest Thông tư 80/2025/TT-BTC
- **v1.3.0** (2026-05-14): Ingest Thông tư 79/2025/TT-BTC
- **v1.2.0** (2026-05-12): Ingest Nghị định 214/2025/NĐ-CP
- **v1.0.0** (2026-05-04): Khởi tạo khung tri thức Luật Đấu thầu hợp nhất

## License

MIT
