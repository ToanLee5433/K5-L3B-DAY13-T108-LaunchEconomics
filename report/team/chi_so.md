# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **`82,83%`** (`994/1.200`) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **`27,12%`** (`48/177`) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **`4,25%`** (`51/1.200`; trong phạm vi `noi_dia + hang_nang` là `3,97%` = `39/982`) |
| Dùng | Tỷ lệ chấp nhận gợi ý | Số gợi ý nhân viên chọn `giu` / tổng số gợi ý đã hiển thị và có quyết định | Không cần tính (cần thu thập event đầy đủ; đối chiếu trên `177` ca được xem lại là `129/177 = 72,88%`) |
| An toàn | Tỷ lệ hoàn tiền trùng đã ghi sổ | Số lệnh hoàn trùng đã ghi sổ / tổng số lệnh hoàn đã ghi sổ; nhận diện trùng theo cùng `order_id` và khoản hoàn | Không cần tính (cần thu thập event `refund_posted`) |

**Lưu ý diễn giải:** Chỉ số chính trong đợt chạy thử là **`82,83%`**. Tuyệt đối **không** viết "trợ lý đã nâng chỉ số từ 0,70 lên 82,83%" vì đợt chạy thử vừa qua không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent (nhóm thiết kế `8` event có đủ `trace_id`).

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_received` | API tiếp nhận | `request_id`, `trace_id`, `depot`, `staff_id`, `request_type`, `arm` | Khi nhận yêu cầu |
| `agent_run_completed` | Agent runtime | `request_id`, `trace_id`, `run_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls` | Kết thúc mỗi lần chạy, kể cả lỗi |
| `recommendation_presented` | Giao diện trợ lý | `request_id`, `trace_id`, `recommendation_id`, `suggested_action`, `suggested_amount` | Khi gợi ý hiện cho nhân viên |
| `staff_review_decision` | Giao diện nhân viên | `request_id`, `trace_id`, `recommendation_id`, `decision` (`giu`/`sua`/`bo`), `review_minutes`, `staff_id` | Khi nhân viên quyết định |
| `refund_posted` | Dịch vụ thanh toán | `request_id`, `trace_id`, `order_id`, `refund_id`, `amount`, `status` | Khi khoản hoàn được ghi sổ |
| `customer_notified` | Dịch vụ thông báo | `request_id`, `trace_id`, `channel`, `sent_at`, `message_type` | Khi gửi thông báo cho khách |
| `request_closed` | Hệ thống yêu cầu | `request_id`, `trace_id`, `closed_at`, `resolution` | Khi đóng yêu cầu |
| `request_reopened` | Hệ thống yêu cầu | `request_id`, `trace_id`, `reopened_at`, `reason` | Khi khách mở lại yêu cầu |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính “đóng trong 24 giờ và không mở lại trong 7 ngày”: tính từ `request_received`, `request_closed`, `request_reopened`; mẫu số là số yêu cầu nhận được (phân nhóm theo `arm`).
- Tỷ lệ bỏ qua gợi ý: tính từ `recommendation_presented` và `staff_review_decision`; tử số là quyết định `sua` hoặc `bo` (đồng thời đo `review_minutes` thực tế thay cho số `simulated`).
- Tỷ lệ lỗi lọt đến khách theo `mo_lai_trong_7_ngay`: tính từ `request_received` và `request_reopened`; lưu `reason` để xác định mở lại do lỗi.
- Tỷ lệ chấp nhận gợi ý: tính từ `recommendation_presented` và `staff_review_decision`; tử số là quyết định `giu`.
- Tỷ lệ hoàn tiền trùng đã ghi sổ: tính từ `refund_posted`; đối chiếu `order_id`, `amount` và `refund_id` để nhận diện khoản trùng.

## E2 · Rủi ro kinh tế

Số lấy trực tiếp từ bảng độ nhạy và kịch bản B4 (`report/team/bang_chi_phi.md`), giữ nhãn `simulated`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi ngoài pilot | Chi phí mỗi việc thành công tăng **`+51,8%`**, lên **`6.787 đ`** (`simulated`), mức tác động lớn nhất trong 9 kịch bản độ nhạy | Tỉ lệ ca `lam_lai` theo tuần trong phạm vi `noi_dia + hang_nang` vượt `7%` (mức chạy thử hiện là `4,9%` = `48/982`) | Thu hẹp phạm vi về riêng `noi_dia`, đặt trần chạy lại tối đa `2` lần (`6.901.220 đ`, `simulated`) và rà soát `20` trace lỗi gần nhất | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% kéo dài hoặc thời gian xem lại quá dài | CPS lên **`11.743 đ = 0,98×`** (với 9 phút làm lại) hoặc **`12.415 đ = 1,03×`** (nếu làm lại trung bình `15,30` phút như dữ liệu, `simulated` — đắt hơn tự làm) | Tỉ lệ yêu cầu bị `duoc_xem_lai == 1` vẫn `> 50%` vào cuối bước `0.25`, hoặc thời gian xem lại thật (`review_minutes`) vượt mức hoà vốn `4,8–5,1` phút | Triển khai lộ trình giảm tỷ lệ xem lại theo bậc khi tỉ lệ sửa/bỏ `< 15%` và tối ưu giao diện tóm tắt lý do hoàn cho nhân viên | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thực tế thấp hơn dự kiến (chạy dưới 50% công suất) | Chi phí cố định `40 triệu đ/tháng` đội phần cố định/việc từ `1.185 đ` lên **`2.370 đ/việc`**, đưa CPS cộng cố định lên **`5.784 đ = 0,48×`** (`simulated`) | Số việc thành công hàng tuần `< 50%` kế hoạch (`< 4.200` việc/tuần ở quy mô đầy đủ hoặc dưới ngưỡng bước rollout) | Dừng mở rộng phạm vi/rollout và rà soát lại cấu trúc chi phí cố định giám sát hàng tháng | PM trợ lý hoàn phí |
