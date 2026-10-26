---
name: tra-cuu-luat-dau-thau
description: Tra cứu quy định pháp luật Đấu thầu Việt Nam (Luật 22/2023, NĐ 214/2025, NĐ 349/2026, TT 79, TT 80, 1.570 Q&A nghiệp vụ và 15 chuyên đề thực tiễn)
---

# Kỹ năng Tra cứu Pháp luật Đấu thầu (law-wiki-bidding-v2)

Kỹ năng này hướng dẫn Muse / AI Agent truy cập, định vị và giải đáp chính xác các thắc mắc về đấu thầu dựa trên kho tri thức chuẩn `law-wiki-bidding-v2`.

## 1. Bản đồ Kho tri thức (Knowledge Base Layout)

- **Thư mục làm việc:** `wiki/` (Vault Obsidian tại thư mục gốc repository).
- **Văn bản pháp luật gốc:**
  - `wiki/laws/luat-dau-thau-2023.md`: Luật Đấu thầu số 22/2023/QH15 (hợp nhất Luật 57/2024 và Luật 90/2025).
  - `wiki/articles/`: 100 điều luật chi tiết (Điều 1 đến Điều 98, bao gồm Điều 29a, Điều 29b chèn thêm).
  - `wiki/documents/nd-214-2025/`: Nghị định 214/2025/NĐ-CP (hướng dẫn thi hành Luật Đấu thầu, chia theo chương).
  - `wiki/documents/nd-349-2026.md`: Nghị định 349/2026/NĐ-CP (sửa đổi NĐ 214, điều chỉnh nâng hạn mức chỉ định thầu lên 1 tỷ, 3 tỷ, 5 tỷ).
  - `wiki/documents/nd-24-2024.md`: Nghị định 24/2024/NĐ-CP (*Status: superseded* - lưu vết lịch sử).
  - `wiki/documents/tt-79-2025/` & `wiki/documents/tt-80-2025.md`: Thông tư hướng dẫn của Bộ Tài chính.
- **Khái niệm & Nguyên tắc:**
  - `wiki/concepts/`: 38 khái niệm và chủ thể đấu thầu (Chủ đầu tư, Bên mời thầu, Nhà đầu tư, Bảo đảm cạnh tranh, Chỉ định thầu, v.v.).
- **Tình huống thực tế & Chuyên đề sâu:**
  - `wiki/syntheses/`: 15 chuyên đề cẩm nang tổng hợp thực tiễn chuyên sâu.
  - `wiki/qa/`: 1.570 câu hỏi và giải đáp chính thức từ Cổng TTĐT Chính phủ.
  - `wiki/INDEX.md` & `wiki/INDEX-QA.md`: Mục lục tra cứu phân tầng.

## 2. Quy tắc Điều hướng & Tra cứu Tối ưu

### Tra cứu Điều luật & Khái niệm
- Khi cần tìm quy định cụ thể của Luật: Tìm tệp tương ứng trong `wiki/articles/dieu-X-slug.md`.
- Các khoản, điểm được gắn thẻ anchor trực tiếp trong file (`{#khoan-1}`, `{#khoan-1-diem-a}`). Không tìm kiếm file riêng cho từng khoản.
- Khi cần hiểu rõ bản chất hoặc định nghĩa pháp lý: Đọc trang khái niệm tương ứng trong `wiki/concepts/`.

### Tra cứu Q&A Thực tiễn (BẮT BUỘC)
- **Tuyệt đối không kỳ vọng điều luật chứa link trực tiếp tới 1.570 Q&A:**
  Để tối ưu ngữ cảnh, các câu hỏi Q&A không được gắn liên kết hai chiều vào thân 100 điều luật.
- **Phương pháp 1 - Grep theo `related_articles` (Nhanh & chuẩn xác nhất):**
  Mỗi file Q&A có frontmatter `related_articles: [X]`. Khi muốn tìm các tình huống liên quan đến Điều X, hãy grep:
  ```bash
  grep -rn "related_articles:.*\<X\>" wiki/qa/
  ```
- **Phương pháp 2 - Tra cứu qua Mục lục:**
  Xem `wiki/INDEX-QA.md#dieu-X` để lấy danh sách các Q&A tiêu biểu của Điều X.
- **Phương pháp 3 - Tra cứu qua Chuyên đề Syntheses:**
  Đọc 15 chuyên đề tại `wiki/syntheses/` để nắm trọn vẹn cả căn cứ pháp lý, rủi ro thường gặp và các tình huống giải đáp nổi bật.

## 3. Quy tắc Hiệu lực & Lưu ý Pháp lý Quan trọng

- **Nghị định 349/2026/NĐ-CP:** Nâng hạn mức chỉ định thầu lên:
  - 1 tỷ đồng cho gói thầu dịch vụ tư vấn, phi tư vấn, hàng hóa.
  - 3 tỷ đồng cho gói thầu mua sắm thường xuyên đặc thù / khoa học công nghệ.
  - 5 tỷ đồng cho gói thầu xây lắp, hỗn hợp.
  (Không còn áp dụng hạn mức 500 triệu đồng cũ).
- **Nghị định 24/2024/NĐ-CP đã hết hiệu lực:** Được thay thế toàn diện bởi NĐ 214/2025/NĐ-CP và NĐ 349/2026/NĐ-CP.
- **Cơ quan quản lý:** Bộ Kế hoạch và Đầu tư đã sáp nhập vào Bộ Tài chính. Cơ quan quản lý hoạt động đấu thầu hiện nay là Bộ Tài chính.
