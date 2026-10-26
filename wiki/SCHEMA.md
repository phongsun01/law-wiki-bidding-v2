# LLM Wiki Schema — Luật Đấu thầu Việt Nam

Tài liệu này xác định chuẩn dữ liệu, cấu trúc thư mục, quy tắc liên kết, quy tắc tra cứu và vòng đời bảo trì cho kho tri thức **law-wiki-bidding-v2**.

---

## 1. Phạm vi & Cơ sở pháp lý (Domain)

Kho tri thức hệ thống hóa toàn diện hệ thống pháp luật về đấu thầu tại Việt Nam, bao gồm:
- **Luật gốc:** [[luat-dau-thau-2023|Luật Đấu thầu số 22/2023/QH15]] (được sửa đổi, bổ sung bởi Luật số 57/2024/QH15 và Luật số 90/2025/QH15).
- **Nghị định hướng dẫn:**
  - [[documents/nd-214-2025|Nghị định 214/2025/NĐ-CP]] (Hiệu lực từ 01/10/2025, thay thế NĐ 24/2024/NĐ-CP).
  - [[documents/nd-349-2026|Nghị định 349/2026/NĐ-CP]] (Sửa đổi, bổ sung NĐ 214/2025/NĐ-CP, nâng hạn mức chỉ định thầu).
  - [[documents/nd-24-2024|Nghị định 24/2024/NĐ-CP]] (*Status: superseded* - lưu vết lịch sử phục vụ đối chiếu các tình huống cũ).
- **Thông tư hướng dẫn:**
  - [[documents/tt-79-2025|Thông tư 79/2025/TT-BTC]] (Quy định chi tiết về cung cấp, đăng tải thông tin và lựa chọn nhà thầu trên Hệ thống mạng đấu thầu quốc gia).
  - [[documents/tt-80-2025|Thông tư 80/2025/TT-BTC]] (Quy định mẫu hồ sơ yêu cầu, báo cáo đánh giá, báo cáo thẩm định, kiểm tra hoạt động đấu thầu).
- **Thực tiễn áp dụng:**
  - 1.570 câu hỏi và giải đáp nghiệp vụ chính thức từ Cổng Thông tin điện tử Chính phủ (`wiki/qa/`).
  - 15 chuyên đề tổng hợp thực tiễn sâu rộng (`wiki/syntheses/`).

---

## 2. Cấu trúc thư mục (Directory Structure)

Thư mục làm việc cốt lõi của Wiki là `wiki/`. Obsidian Vault đặt ở thư mục gốc của repository.

```
law-wiki-bidding-v2/
├── wiki/
│   ├── articles/      # 100 điều luật (Điều 1 - 98 + Điều 29a, 29b chèn thêm)
│   ├── chapters/      # 10 chương của Luật Đấu thầu 2023
│   ├── concepts/      # 38 khái niệm pháp lý cốt lõi (31 gốc + 4 NĐ214 + 3 chủ thể)
│   ├── documents/     # Nghị định và Thông tư hướng dẫn (hub + chapter files)
│   ├── laws/          # Văn bản luật hợp nhất
│   ├── qa/            # 1.570 tình huống giải đáp nghiệp vụ
│   ├── syntheses/     # 15 chuyên đề cẩm nang tổng hợp thực tiễn
│   ├── INDEX.md       # Mục lục tra cứu phân tầng toàn diện
│   ├── INDEX-QA.md    # Danh mục tổng hợp tra cứu 1.570 Q&A theo điều
│   ├── LOG.md         # Nhật ký thay đổi và lịch sử ingest
│   └── SCHEMA.md      # Quy chuẩn kỹ thuật này
├── raw/               # Văn bản nguồn và dữ liệu crawl bất biến
└── scripts/           # Công cụ tự động hóa và linter bảo đảm chất lượng
```

---

## 3. Quy chuẩn Frontmatter (Frontmatter Specifications)

Mọi tệp markdown trong wiki đều phải mở đầu bằng YAML frontmatter hợp lệ.

### 3.1 Articles (`wiki/articles/*.md`)
```yaml
---
law_id: luat-dau-thau-2023
article_number: 23
title: Chỉ định thầu
chapter: 2
chapter_title: Lựa chọn nhà thầu, nhà đầu tư
effective_date: 2024-01-01
last_amended: 2026-09-09
amendment_history: "Luật 22/2023/QH15, Luật 57/2024/QH15, NĐ 349/2026/NĐ-CP"
status: amended
summary: "Quy định các trường hợp áp dụng chỉ định thầu và hạn mức gói thầu..."
related_articles: [4, 20, 29, 38]
total_clauses: 3
tags:
  - "chi-dinh-thau"
  - "hinh-thuc-lua-chon"
  - "amended-nd349"
---
```
*Lưu ý:*
- `related_articles`: BẮT BUỘC là mảng số nguyên các điều liên quan (`[4, 20, 29, 38]`), KHÔNG dùng wikilinks trong trường này để hỗ trợ tìm kiếm và quan hệ ma trận. Không để trùng lặp số điều.
- `tags`: Dùng chữ thường, nối từ bằng dấu gạch ngang (`-`).

### 3.2 Concepts (`wiki/concepts/*.md`)
```yaml
---
title: "Bên mời thầu"
concept_id: "ben-moi-thau"
domain: "chu-the"
related_articles: [4, 79]
tags:
  - "khai-niem"
  - "chu-the"
  - "ben-moi-thau"
---
```

### 3.3 Documents (`wiki/documents/*.md`)
```yaml
---
title: "Nghị định 214/2025/NĐ-CP hướng dẫn Luật Đấu thầu về lựa chọn nhà thầu"
doc_type: "decree"            # decree | circular
document_id: "214/2025/ND-CP"
issuer: "Chính phủ"
date_issued: "2025-08-04"
effective_date: "2025-10-01"
status: "active"              # active | amended | superseded
supersedes: ["24/2024/ND-CP"]
tags:
  - "nghi-dinh"
  - "van-ban-huong-dan"
---
```

### 3.4 Q&A (`wiki/qa/*.md`)
```yaml
---
id: qa-0001
title: "Điều kiện áp dụng chỉ định thầu rút gọn đối với gói thầu cấp bách"
source: "Cổng Thông tin điện tử Chính phủ"
url: "https://baochinhphu.vn/..."
date: "2024-05-10"
related_articles: [23]
tags:
  - "chi-dinh-thau"
  - "cap-bach"
---
```

---

## 4. Quy tắc Liên kết (Wikilinks) & Anchor

1. **Định dạng Wikilink chuẩn:**
   - Liên kết trang: `[slug]` (ví dụ: `[[dieu-1-pham-vi]]`) hoặc `[[documents/nd-214-2025]]` hoặc `[[dieu-1-pham-vi|Điều 1]]`.
   - Liên kết có anchor: `[[dieu-4-giai-thich-tu-ngu#khoan-1]]` hoặc `[[dieu-4-giai-thich-tu-ngu#khoan-1|Khoản 1 Điều 4]]`.
2. **Không tạo tệp con cho khoản/điểm:**
   - Toàn bộ nội dung điều luật nằm trong 1 tệp duy nhất.
   - Các khoản/điểm được đánh dấu bằng anchor rõ ràng:
     - Khoản: `### Khoản 1. ... {#khoan-1}`
     - Điểm: `- **Điểm a.** ... {#khoan-1-diem-a}`
3. **Tuyệt đối không dùng ký tự đại diện (Wildcard):**
   - Không tạo link dạng `dieu-23-*`. Bắt buộc dùng đúng slug file: `[[dieu-23-chi-dinh-thau]]`.

---

## 5. Quy tắc Tra cứu Q&A Thực tiễn (Crucial for AI Agent / Muse)

- **Q&A không gắn wikilink hai chiều trong điều luật:**
  Do có tới 1.570 câu hỏi thực tiễn, việc chèn toàn bộ link Q&A vào thân 100 điều luật sẽ làm phình kích thước context quá mức cần thiết và phá vỡ cấu trúc tinh gọn.
- **Phương thức tra cứu Q&A chuẩn:**
  1. **Tra qua `related_articles`:** Mỗi Q&A đều chứa trường `related_articles: [X]`. Agent tra cứu câu hỏi liên quan đến Điều X bằng cách tìm kiếm:
     ```bash
     grep -rn "related_articles:.*\[.*\<X\>.*\]" wiki/qa/
     ```
  2. **Tra qua `wiki/INDEX-QA.md`:** `INDEX-QA.md` cung cấp mục lục điều hướng theo điều với anchor `{#dieu-X}`.
  3. **Tra cứu qua chuyên đề `wiki/syntheses/`:** 15 trang tổng hợp thực tiễn đã đúc kết và dẫn nguồn các Q&A tiêu biểu nhất cho từng nghiệp vụ.

---

## 6. Chính sách Cập nhật & Ngưỡng Kích thước Trang

1. **Khi văn bản pháp luật sửa đổi, bổ sung:**
   - Cập nhật trường `last_amended`, `status: amended` và lịch sử sửa đổi trong frontmatter.
   - Thêm hộp thoại cảnh báo `> [!IMPORTANT]` hoặc `> [!WARNING]` ngay đầu bài viết và chú thích rõ nội dung được sửa đổi.
   - **Bắt buộc rà soát và cập nhật nội dung giải thích trong thân bài**, không để mâu thuẫn giữa phần lưu ý đầu trang và thân văn bản (ví dụ: hạn mức chỉ định thầu phải sửa trực tiếp từ 500 triệu lên 1 tỷ, 3 tỷ, 5 tỷ theo NĐ 349).
   - Nếu văn bản hết hiệu lực: chuyển `status: superseded`, ghi rõ văn bản thay thế và giữ lại để làm đối sánh lịch sử, không xóa file làm gãy link.
2. **Ngưỡng kích thước trang (Page Size Policy):**
   - **Trang tổng hợp (Concepts, Syntheses):** Khuyến nghị ≤ 200 dòng để bảo đảm tính súc tích, tránh làm tràn ngữ cảnh của AI.
   - **Ngoại lệ bắt buộc (Exemptions):** Các văn bản quy phạm pháp luật gốc (`wiki/laws/` và `wiki/documents/`) như NĐ 214 Chương 1, Chương 2, NĐ 349... được **miễn trừ** quy định 200 dòng nhằm giữ nguyên tính toàn vẹn, nguyên văn và liền mạch của điều khoản luật. Không được chia cắt cơ học văn bản quy phạm pháp luật gốc làm sai lệch cấu trúc chương/mục.

---

## 7. Quy trình Kiểm thử Chất lượng (Quality Assurance)

Mọi thay đổi trong kho tri thức phải được kiểm tra thông qua công cụ:
```bash
python scripts/lint.py
```
Linter tự động xác thực:
- 100% wikilink và anchor hợp lệ (không link hỏng, không target ma).
- Tính nhất quán của frontmatter và trường `related_articles`.
- Kiểm tra các trang mồ côi ngoài danh mục cho phép.
- Đồng bộ hóa giữa `INDEX.md` và hệ thống tệp thực tế.
