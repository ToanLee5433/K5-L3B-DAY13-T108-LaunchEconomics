# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Tỷ lệ chấp nhận gợi ý | Số gợi ý nhân viên chọn `giu` / tổng số gợi ý đã hiển thị và có quyết định | Cần thu thập event; chưa tính được từ CSV hiện có |
| An toàn | Tỷ lệ hoàn tiền trùng đã ghi sổ | Số lệnh hoàn trùng đã ghi sổ / tổng số lệnh hoàn đã ghi sổ; nhận diện trùng theo cùng `order_id` và khoản hoàn | Cần thu thập event; chưa tính được từ CSV hiện có |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_received` | API tiếp nhận | `request_id`, `trace_id`, `depot`, `staff_id`, `request_type` | Khi nhận yêu cầu |
| `agent_run_completed` | Agent runtime | `request_id`, `trace_id`, `run_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls` | Kết thúc mỗi lần chạy |
| `recommendation_presented` | Giao diện trợ lý | `request_id`, `trace_id`, `recommendation_id`, `suggested_action`, `suggested_amount` | Khi gợi ý hiện cho nhân viên |
| `staff_review_decision` | Giao diện nhân viên | `request_id`, `trace_id`, `recommendation_id`, `decision` (`giu`/`sua`/`bo`), `staff_id` | Khi nhân viên quyết định |
| `refund_posted` | Dịch vụ thanh toán | `request_id`, `trace_id`, `order_id`, `refund_id`, `amount`, `status` | Khi khoản hoàn được ghi sổ |
| `customer_notified` | Dịch vụ thông báo | `request_id`, `trace_id`, `channel`, `sent_at`, `message_type` | Khi gửi thông báo cho khách |
| `request_closed` | Hệ thống yêu cầu | `request_id`, `trace_id`, `closed_at`, `resolution` | Khi đóng yêu cầu |
| `request_reopened` | Hệ thống yêu cầu | `request_id`, `trace_id`, `reopened_at`, `reason` | Khi khách mở lại yêu cầu |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính “đóng trong 24 giờ và không mở lại trong 7 ngày”: cần `request_received`, `request_closed`, `request_reopened`; mẫu số là số yêu cầu nhận được.
- Tỷ lệ bỏ qua gợi ý: cần `recommendation_presented` và `staff_review_decision`; tử số là quyết định `sua` hoặc `bo`.
- Tỷ lệ lỗi lọt đến khách theo `mo_lai_trong_7_ngay`: cần `request_received` và `request_reopened`; lưu `reason` để xác định mở lại do lỗi.
- Tỷ lệ chấp nhận gợi ý: cần `recommendation_presented` và `staff_review_decision`; tử số là quyết định `giu`.
- Tỷ lệ hoàn tiền trùng đã ghi sổ: cần `refund_posted`; đối chiếu `order_id`, `amount` và `refund_id` để nhận diện khoản trùng.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
