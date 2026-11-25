# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: T108 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | `4.472 đ` (`simulated`, gấp `16,3×` hoá đơn `274,7 đ/yc`); phạm vi pilot `noi_dia + hang_nang` là `3.414 đ` chưa cố định, cộng cố định `40 triệu/tháng` thành `4.599 đ` ở `45.000` yc/tháng (`5.784 đ` ở nửa khối lượng, `simulated`) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (`+51,8%` khi ×2 → `6.787 đ`, chiếm `51,8%` tổng chi phí); 2. Tỉ lệ xem lại (`+40,7%` → `6.292 đ`, chiếm `40,7%`); 3. Lương nhân viên (`+23,1%` → `5.506 đ`) (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống `5.865 đ/yc = 0,49×` của `12.000 đ` (`simulated`); riêng `quoc_te` lỗ `1,88×` (`22.515 đ`) và `doi_tac` `0,85×` (`10.215 đ`) nên loại; `noi_dia` `0,22×` (`2.696 đ`) và `hang_nang` `0,69×` (`8.221 đ`) (`simulated`). Nếu xem lại 100%: `0,98×`–`1,03×` (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử: Chính `82,83%` (`994/1.200`), Dùng bỏ qua gợi ý `27,12%` (`48/177`), An toàn mở lại 7 ngày `4,25%` (`51/1.200`; phạm vi `3,97%`); bổ sung 2 chỉ số (chấp nhận gợi ý, hoàn trùng sổ cái) + `8` event có `trace_id` đã kiểm tra chéo | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 5 · Bảng lỗi và cách khắc phục | Gắn nhãn độc lập 20 ca theo 5 loại Google PAIR: đồng thuận `19/20 = 95%` (lệch duy nhất Ca 13, đã chốt *Giới hạn hệ thống*); bảng khắc phục 5 ca (Ca 1, 7, 10, 11, 5) đủ event, ngưỡng, tần suất và 1 vai trò phụ trách/ca | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 6 · Pilot plan | Chia theo nhân viên (`20` vs `20` ở 12 depot), chấp nhận MDE `+6 điểm` (`n = 859/arm`, `m ≥ 299`, `DE = 6,96`, power còn `0,64` nếu hiệu ứng thật `+5 điểm`), rollout `[0.10, 0.25, 0.50]` (bước `0.50` gom `≥ 8–10` ngày + `7` ngày bảo hành; lệch `≥ 2` điểm chỉ bật từ bước `10` người; ngưỡng `8.000 đ` chỉ tính chi phí biến đổi `3.414 đ`, chưa cộng `40 triệu` cố định, `simulated`), 3 luật dừng đủ 4 vế, kill-switch `30` phút | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2 → `6.787 đ` (`+51,8%`); xem lại 100% kéo dài → `11.743–12.415 đ` (`0,98×–1,03×`, hoà vốn `≤ 4,8–5,1` phút); khối lượng giảm 50% → cố định `+2.370 đ/việc`, CPS `5.784 đ` (`simulated`) | Giả lập | Trưởng nhóm CSKH |

**Đề xuất:** **Go có điều kiện** cho **pilot** trong phạm vi `noi_dia + hang_nang` (loại `quoc_te` và `doi_tac`), kèm bốn điều kiện bắt buộc sau:

- Sửa lỗi hoàn trùng (thêm khoá chống trùng `idempotency_key`) và bật đối soát API sổ cái tự động mỗi giờ trước ngày mở pilot — **Người phụ trách:** Kỹ sư trưởng agent · **Ngày kiểm tra:** `2026-12-01`.
- Ký xác nhận bằng văn bản đánh đổi thống kê `MDE = +6 điểm` (`n = 859/nhóm`, `m ≥ 299` yêu cầu/nhân viên; power giảm còn `0,64` nếu tác động thật chỉ `+5 điểm`) — **Người phụ trách:** Giám đốc vận hành LogiX-VN · **Ngày kiểm tra:** `2026-12-02`.
- Bật đủ `8` event gắn `trace_id` và thay toàn bộ số liệu phút `_simulated` bằng `review_minutes` đo thực tế ngay sau tuần đầu của bước `0.10` — **Người phụ trách:** Kỹ sư trưởng agent · **Ngày kiểm tra:** `2026-12-10`.
- Lập kế hoạch giảm tỉ lệ xem lại theo bậc ngay khi tỉ lệ sửa/bỏ gợi ý `< 15%` để tránh kịch bản xem lại 100% (`0,98×–1,03×` so với `12.000 đ`, `simulated`) — **Người phụ trách:** Trưởng nhóm CSKH · **Ngày kiểm tra:** `2026-12-17`.
