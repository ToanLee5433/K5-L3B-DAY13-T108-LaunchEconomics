# Báo cáo cá nhân — Đàm Hồng Thái

## 1. Thông tin thành viên

- Họ tên: Đàm Hồng Thái
- MSSV: `2A202603927`
- Email: `thai.dh1012@gmail.com`
- Vai trong nhóm: **Người gắn nhãn 1 + Người kiểm số / QA duyệt chéo**; phụ trách bảng lỗi CP3, soạn đề xuất event và chỉ số E1, và chấm duyệt chéo Gate 2a. Lê Quý Toàn đảm nhiệm **Người viết code + Người gắn nhãn 2 kiêm giữ hồ sơ**.

## 2. Phần việc phụ trách

Phân loại độc lập 20 ca lỗi theo năm loại Google PAIR, viết quy tắc xử lý ca gần ranh giới, đề xuất biện pháp phát hiện/khắc phục cho 5 ca đại diện trong `report/team/bang_loi.md`; soạn phần E1 không cần code (2 chỉ số tự đề xuất, 8 event có `trace_id` và kiểm tra chéo) để nhóm ghép vào `report/team/chi_so.md`; lập phiếu chấm duyệt chéo Gate 2a cho nhóm `HuuDuyenBL` trong `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

- Hoàn thiện bộ nhãn độc lập thứ nhất cho 20 ca lỗi, viết quy tắc phân biệt và bảng khắc phục 5 ca (Ca 1, 7, 10, 11, 5), mỗi ca đại diện một loại lỗi với event, ngưỡng cảnh báo định lượng, tần suất và 1 vai trò chịu trách nhiệm.
- Bổ sung ngưỡng theo dõi định lượng theo tuần cho Ca 10 (`> 1%` số yêu cầu trễ bị từ chối vì bất khả kháng trong tuần).
- Đối chiếu đồng thuận với bộ nhãn độc lập thứ hai của Lê Quý Toàn: đạt **`19/20 = 95%`** (vượt ngưỡng `80%`), chỉ lệch duy nhất Ca 13 (tôi gắn *Hệ thống*, Toàn gắn *Giới hạn hệ thống*) và thống nhất chốt *Giới hạn hệ thống* theo nguyên nhân gốc kèm quy tắc phân biệt trong `report/team/bang_loi.md`.
- Soạn 2 chỉ số tự đề xuất (*Tỷ lệ chấp nhận gợi ý* và *Tỷ lệ hoàn tiền trùng đã ghi sổ*), `8` event có `trace_id` và bảng kiểm tra chéo 5/5 chỉ số-event, đã gộp vào `report/team/chi_so.md`.
- Thực hiện chấm sơ bộ nhóm `HuuDuyenBL` trong phiên duyệt chéo (`4912eb7`, `802d2c3`, `5b46d5d`), sau đó cùng Lê Quý Toàn rà soát bản hồ sơ đầy đủ trên repo của `HuuDuyenBL` (`01de255`) để chuẩn hoá điểm `30/30` (**Go có điều kiện**) kèm câu hỏi kỹ thuật vào `report/team/phieu_cham.md`.

## 4. Bằng chứng

- Các commit `c1aa62f`, `a4e35d3`, `5fb8bfb`, `62f8432` trên nhánh `2A202603927_DamHongThai` (đã merge vào `main`) và `4912eb7`, `802d2c3`, `5b46d5d` trên nhánh `main`.
- `report/team/bang_loi.md`: hai bộ nhãn độc lập (`19/20 = 95%`), quy tắc phân biệt (bao gồm Ca 13) và bảng khắc phục 5 ca.
- `report/team/chi_so.md`: 2 chỉ số bổ sung, `8` event có `trace_id` và bảng kiểm tra chéo.
- `report/team/phieu_cham.md`: phiếu chấm Gate 2a đối với hồ sơ nhóm `HuuDuyenBL`.

## 5. Công cụ AI đã dùng

ChatGPT/Codex hỗ trợ trích nội dung 20 ca từ đề DOCX, lập bản nháp phân loại và biên tập bảng/đề xuất event. Tôi đã tự đối chiếu từng nhãn với mô tả ca và định nghĩa năm loại trong đề trước khi gửi đối chiếu với Lê Quý Toàn, sau đó bổ sung ngưỡng định lượng cho Ca 10, kiểm tra quy tắc Ca 13 và rà soát lại phần chấm chéo `phieu_cham.md` trên hồ sơ đầy đủ của `HuuDuyenBL`.

## 6. Tự đánh giá

Đã hoàn thành đầy đủ phần phân loại lỗi (`95%` đồng thuận với Lê Quý Toàn), phương án khắc phục có event, ngưỡng, tần suất cùng vai trò chịu trách nhiệm, bộ `8` event E1 và phiếu chấm Gate 2a cho nhóm `HuuDuyenBL`. Toàn bộ hồ sơ nhóm `T108` đã đồng bộ trên nhánh `main`, sẵn sàng nộp link repo trên LMS trước hạn 23:59.
