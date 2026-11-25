# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **`82,83%`** (`994/1.200`) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **`27,12%`** (`48/177`) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **`4,25%`** (`51/1.200`; trong phạm vi `noi_dia + hang_nang` là `3,97%` = `39/982`) |
| Dùng | Nhóm tự đề xuất: [Chờ ghép từ bạn cùng nhóm ở Đồng bộ 1] | [Chờ ghép từ bạn cùng nhóm] | Không cần tính |
| An toàn | Nhóm tự đề xuất: [Chờ ghép từ bạn cùng nhóm ở Đồng bộ 1] | [Chờ ghép từ bạn cùng nhóm] | Không cần tính |

**Lưu ý diễn giải:** Chỉ số chính trong đợt chạy thử là **`82,83%`**. Tuyệt đối **không** viết "trợ lý đã nâng chỉ số từ 0,70 lên 82,83%" vì đợt chạy thử vừa qua không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent. *(Phần bảng Event và kiểm tra chéo do thành viên 2 soạn song song và gửi ghép tại Đồng bộ 1).*

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| [Chờ ghép từ bạn cùng nhóm] | ... | ..., trace_id | ... |
| [Chờ ghép từ bạn cùng nhóm] | ... | ..., trace_id | ... |
| [Chờ ghép từ bạn cùng nhóm] | ... | ..., trace_id | ... |
| [Chờ ghép từ bạn cùng nhóm] | ... | ..., trace_id | ... |
| [Chờ ghép từ bạn cùng nhóm] | ... | ..., trace_id | ... |
| [Chờ ghép từ bạn cùng nhóm] | ... | ..., trace_id | ... |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- [Chờ ghép bảng đối chiếu event từ bạn cùng nhóm ở Đồng bộ 1]

## E2 · Rủi ro kinh tế

Số lấy trực tiếp từ bảng độ nhạy và kịch bản B4 (`report/team/bang_chi_phi.md`), giữ nhãn `simulated`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi ngoài pilot | Chi phí mỗi việc thành công tăng **`+51,8%`**, lên **`6.787 đ`** (`simulated`), mức tác động lớn nhất trong 9 kịch bản độ nhạy | Tỉ lệ ca `lam_lai` theo tuần trong phạm vi `noi_dia + hang_nang` vượt `7%` (mức chạy thử hiện là `4,9%` = `48/982`) | Thu hẹp phạm vi về riêng `noi_dia`, đặt trần chạy lại tối đa `2` lần (`6.901.220 đ`, `simulated`) và rà soát `20` trace lỗi gần nhất | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% kéo dài hoặc thời gian xem lại quá dài | CPS lên **`11.743 đ = 0,98×`** (với 9 phút làm lại) hoặc **`12.415 đ = 1,03×`** (nếu làm lại trung bình `15,30` phút như dữ liệu, `simulated` — đắt hơn tự làm) | Tỉ lệ yêu cầu bị `duoc_xem_lai == 1` vẫn `> 50%` vào cuối bước `0.25`, hoặc thời gian xem lại thật vượt mức hoà vốn `4,8–5,1` phút | Triển khai lộ trình giảm tỷ lệ xem lại theo bậc khi tỉ lệ sửa/bỏ `< 15%` và tối ưu giao diện tóm tắt lý do hoàn cho nhân viên | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thực tế thấp hơn dự kiến (chạy dưới 50% công suất) | Chi phí cố định `40 triệu đ/tháng` đội phần cố định/việc từ `1.185 đ` lên **`2.370 đ/việc`**, đưa CPS cộng cố định lên **`5.784 đ = 0,48×`** (`simulated`) | Số việc thành công hàng tuần `< 50%` kế hoạch (`< 4.200` việc/tuần ở quy mô đầy đủ hoặc dưới ngưỡng bước rollout) | Dừng mở rộng phạm vi/rollout và rà soát lại cấu trúc chi phí cố định giám sát hàng tháng | PM trợ lý hoàn phí |
