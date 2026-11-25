# Bảng lỗi và cách khắc phục · Nhiệm vụ C

Phân loại theo nguyên nhân gốc trong năm nhóm Google PAIR: **Do người dùng**, **Hệ thống**, **Ngữ cảnh**, **Giới hạn hệ thống**, **Ngầm**. Ca được gắn một nhãn chính; quy tắc bên dưới xử lý các trường hợp gần ranh giới.

## Nhãn độc lập của tôi

Tôi đã gắn nhãn đủ 20 ca độc lập trước khi đối chiếu. Chưa có bộ nhãn độc lập thứ hai của một thành viên trong nhóm, vì vậy cột người gắn nhãn 2 và phép tính đồng thuận được để **chờ đối chiếu**, không tự điền nhãn giả định.

| Ca | Nhãn người gắn nhãn 1 (tôi) | Nhãn người gắn nhãn 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Chờ đối chiếu | Chưa biết | Do người dùng (tạm) |
| 2 | Hệ thống | Chờ đối chiếu | Chưa biết | Hệ thống (tạm) |
| 3 | Ngữ cảnh | Chờ đối chiếu | Chưa biết | Ngữ cảnh (tạm) |
| 4 | Giới hạn hệ thống | Chờ đối chiếu | Chưa biết | Giới hạn hệ thống (tạm) |
| 5 | Ngầm | Chờ đối chiếu | Chưa biết | Ngầm (tạm) |
| 6 | Do người dùng | Chờ đối chiếu | Chưa biết | Do người dùng (tạm) |
| 7 | Hệ thống | Chờ đối chiếu | Chưa biết | Hệ thống (tạm) |
| 8 | Hệ thống | Chờ đối chiếu | Chưa biết | Hệ thống (tạm) |
| 9 | Do người dùng | Chờ đối chiếu | Chưa biết | Do người dùng (tạm) |
| 10 | Ngữ cảnh | Chờ đối chiếu | Chưa biết | Ngữ cảnh (tạm) |
| 11 | Giới hạn hệ thống | Chờ đối chiếu | Chưa biết | Giới hạn hệ thống (tạm) |
| 12 | Ngầm | Chờ đối chiếu | Chưa biết | Ngầm (tạm) |
| 13 | Hệ thống | Chờ đối chiếu | Chưa biết | Hệ thống (tạm) |
| 14 | Do người dùng | Chờ đối chiếu | Chưa biết | Do người dùng (tạm) |
| 15 | Hệ thống | Chờ đối chiếu | Chưa biết | Hệ thống (tạm) |
| 16 | Ngữ cảnh | Chờ đối chiếu | Chưa biết | Ngữ cảnh (tạm) |
| 17 | Ngầm | Chờ đối chiếu | Chưa biết | Ngầm (tạm) |
| 18 | Ngữ cảnh | Chờ đối chiếu | Chưa biết | Ngữ cảnh (tạm) |
| 19 | Giới hạn hệ thống | Chờ đối chiếu | Chưa biết | Giới hạn hệ thống (tạm) |
| 20 | Hệ thống | Chờ đối chiếu | Chưa biết | Hệ thống (tạm) |

**Tỉ lệ đồng thuận:** Chưa tính được / 20 = chưa xác định; cần bộ nhãn độc lập thứ hai. Sau khi có bộ nhãn đó, đếm số dòng trùng rồi chia 20; ngưỡng đạt là ít nhất 16/20 (80%).

## Quy tắc cho ca lệch và ca gần ranh giới

- **Ca 1, 6, 9, 14:** chọn *Do người dùng* khi dữ liệu nhập hoặc lựa chọn của khách là đầu vào sai làm kích hoạt luồng sai; nếu trợ lý nhận ra điểm không khớp mà vẫn xử lý sai thì chuyển sang *Hệ thống*.
- **Ca 2, 7, 8, 15, 20:** chọn *Hệ thống* khi trợ lý/tool vi phạm chính sách, tính toán sai, tuyên bố thành công sai hoặc thực hiện trùng; việc nhân viên bắt được trước khi gửi không đổi nguyên nhân gốc.
- **Ca 3, 10, 16, 18:** chọn *Ngữ cảnh* khi thao tác đúng thiết kế/chính sách nhưng kỳ vọng, thời điểm hoặc cách giải thích không khớp hoàn cảnh khách; nếu thao tác sai chính sách thì là *Hệ thống*.
- **Ca 4, 11, 19:** chọn *Giới hạn hệ thống* khi thiếu dữ liệu, ngoài phạm vi hoặc không xử lý được dạng đầu vào và hệ thống nói rõ rồi chuyển tiếp; nếu hệ thống che giấu giới hạn bằng câu trả lời sai thì gắn *Hệ thống*.
- **Ca 5, 12, 17:** chọn *Ngầm* khi lỗi/tác động đã xảy ra nhưng người dùng và hệ thống không nhận ra trong lúc xử lý, chỉ lộ qua kiểm tra hoặc theo dõi sau đó; nếu có cảnh báo mà bị bỏ qua thì xem là *Hệ thống*.
- **Ca 13:** gắn *Hệ thống* vì trợ lý đã phản hồi nhưng không báo ngoài phạm vi, khiến nội dung chung về phí vận chuyển có thể bị hiểu là trả lời cho yêu cầu bảo hiểm; chỉ gắn *Giới hạn hệ thống* nếu trợ lý nêu rõ không hỗ trợ và chuyển tiếp an toàn.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | `refund_command_rejected` của ngân hàng; cảnh báo khi số tài khoản không qua kiểm tra độ dài/checksum, theo từng lệnh | Kiểm tra định dạng trước khi tạo lệnh, hiển thị số đã che để khách xác nhận; nếu bị từ chối thì không gửi lại tự động và yêu cầu cập nhật thông tin | Chủ sản phẩm CSKH |
| 7 | Hệ thống | Đối soát `refund_api_result` với `customer_notification_sent`; báo động ngay nếu trạng thái API khác `success` mà đã gửi thông báo thành công | Chỉ báo thành công sau xác nhận ghi sổ; 503 chuyển trạng thái chờ/nhân viên và dùng khóa idempotency khi thử lại | Kỹ sư tích hợp thanh toán |
| 10 | Ngữ cảnh | Theo dõi `request_reopened` trong 7 ngày với lý do “bất khả kháng/cam kết giao”; nếu tỷ lệ mở lại vượt **1% số yêu cầu trễ bị từ chối vì bất khả kháng trong tuần**, phát cảnh báo và rà soát hàng tuần | Giải thích rõ cam kết 24 giờ và ngoại lệ bão trước khi từ chối; đưa đường dẫn khiếu nại/nhân viên vào phản hồi | Trưởng vận hành CSKH |
| 11 | Giới hạn hệ thống | Đếm `unsupported_input` theo loại tệp; cảnh báo nếu tỷ lệ thoại không được xử lý vượt 2% trong ngày | Nêu rõ chưa hỗ trợ âm thanh, cho khách gửi bản chép lời hoặc chuyển nhân viên kèm trạng thái đầu vào | Quản lý sản phẩm AI |
| 5 | Ngầm | Đối soát hàng ngày mẫu đơn có mã giảm giá giữa số hoàn và giá sau giảm; cảnh báo bất kỳ chênh lệch nào và báo cáo số tiền hoàn thừa | Tạm giữ luồng tự động có mã giảm giá cho đến khi công thức được sửa; hoàn phần chênh và thêm kiểm thử hồi quy | Chủ chính sách hoàn phí |

**Ghi chú hoàn tất:** Phần phân loại độc lập và quy tắc đã có; để hoàn tất yêu cầu đồng thuận của nhóm, người gắn nhãn thứ hai cần tự phân loại trước khi xem bảng này, rồi mới điền cột còn trống, số ca trùng và nhãn thống nhất cuối cùng.
