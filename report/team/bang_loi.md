# Bảng lỗi và cách khắc phục · Nhiệm vụ C

Phân loại theo nguyên nhân gốc trong năm nhóm Google PAIR: **Do người dùng**, **Hệ thống**, **Ngữ cảnh**, **Giới hạn hệ thống**, **Ngầm**. Ca được gắn một nhãn chính; quy tắc bên dưới xử lý các trường hợp gần ranh giới.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: **Đàm Hồng Thái** · Người gắn nhãn 2: **Lê Quý Toàn** (cả hai tự gắn độc lập 20 ca theo mô tả đề bài trước khi đối chiếu).

| Ca | Nhãn người gắn nhãn 1 (Đàm Hồng Thái) | Nhãn người gắn nhãn 2 (Lê Quý Toàn) | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Hệ thống | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** `19 / 20 = 95%` (vượt ngưỡng đạt tối thiểu `16/20 = 80%`; phân bố sau thống nhất: Do người dùng `4` ca, Hệ thống `5` ca, Ngữ cảnh `4` ca, Giới hạn hệ thống `4` ca, Ngầm `3` ca).

## Quy tắc cho ca lệch và ca gần ranh giới

- **Ca 13 (ca lệch duy nhất — Thái gắn *Hệ thống*, Toàn gắn *Giới hạn hệ thống* → thống nhất *Giới hạn hệ thống*):** Nguyên nhân gốc là bảo hiểm hàng hoá của công ty đối tác nằm **ngoài phạm vi** trợ lý, kể cả khi trợ lý xử lý giới hạn đó kém (trả lời chung chung về phí vận chuyển). Thái gắn *Hệ thống* do câu trả lời chung chung dễ gây hiểu nhầm; hai thành viên thống nhất quy tắc: ca ngoài phạm vi thì gắn *Giới hạn hệ thống* theo nguyên nhân gốc, còn việc trả lời mập mờ được xử lý ở biện pháp khắc phục (buộc nêu rõ ngoài phạm vi và chuyển tiếp an toàn).
- **Ca 1, 6, 9, 14:** chọn *Do người dùng* khi dữ liệu nhập hoặc lựa chọn của khách là đầu vào sai làm kích hoạt luồng sai; việc trợ lý chưa gợi ý cách sửa là phần cải thiện ở bảng khắc phục.
- **Ca 2, 7, 8, 15, 20:** chọn *Hệ thống* khi trợ lý/tool vi phạm chính sách, tính toán sai, tuyên bố thành công sai hoặc thực hiện trùng; việc nhân viên bắt được trước khi gửi không đổi nguyên nhân gốc.
- **Ca 3, 10, 16, 18:** chọn *Ngữ cảnh* khi thao tác đúng thiết kế/chính sách nhưng kỳ vọng, thời điểm hoặc cách giải thích không khớp hoàn cảnh khách; nếu thao tác sai chính sách thì là *Hệ thống*.
- **Ca 4, 11, 19:** chọn *Giới hạn hệ thống* khi thiếu dữ liệu, ngoài phạm vi hoặc không xử lý được dạng đầu vào và hệ thống nói rõ rồi chuyển tiếp.
- **Ca 5, 12, 17:** chọn *Ngầm* khi lỗi sai (về tiền hoàn hoặc chi phí token gấp `3×`) đã xảy ra nhưng cả khách lẫn hệ thống đều không nhận ra lúc xử lý, chỉ lộ qua kiểm tra mẫu hoặc theo dõi sau đó.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | `refund_command_rejected` của ngân hàng; cảnh báo khi số tài khoản không qua kiểm tra độ dài/checksum, theo từng lệnh | Kiểm tra định dạng trước khi tạo lệnh, hiển thị số đã che để khách xác nhận; nếu bị từ chối thì không gửi lại tự động và yêu cầu cập nhật thông tin | Chủ sản phẩm CSKH |
| 7 | Hệ thống | Đối soát `refund_api_result` với `customer_notification_sent`; báo động ngay nếu trạng thái API khác `success` mà đã gửi thông báo thành công | Chỉ báo thành công sau xác nhận ghi sổ; 503 chuyển trạng thái chờ/nhân viên và dùng khóa idempotency khi thử lại | Kỹ sư tích hợp thanh toán |
| 10 | Ngữ cảnh | Theo dõi `request_reopened` trong 7 ngày với lý do “bất khả kháng/cam kết giao”; nếu tỷ lệ mở lại vượt **1% số yêu cầu trễ bị từ chối vì bất khả kháng trong tuần**, phát cảnh báo và rà soát hàng tuần | Giải thích rõ cam kết 24 giờ và ngoại lệ bão trước khi từ chối; đưa đường dẫn khiếu nại/nhân viên vào phản hồi | Trưởng vận hành CSKH |
| 11 | Giới hạn hệ thống | Đếm `unsupported_input` theo loại tệp; cảnh báo nếu tỷ lệ thoại không được xử lý vượt 2% trong ngày | Nêu rõ chưa hỗ trợ âm thanh, cho khách gửi bản chép lời hoặc chuyển nhân viên kèm trạng thái đầu vào | Quản lý sản phẩm AI |
| 5 | Ngầm | Đối soát hàng ngày mẫu đơn có mã giảm giá giữa số hoàn và giá sau giảm; cảnh báo bất kỳ chênh lệch nào và báo cáo số tiền hoàn thừa | Tạm giữ luồng tự động có mã giảm giá cho đến khi công thức được sửa; hoàn phần chênh và thêm kiểm thử hồi quy | Chủ chính sách hoàn phí |
