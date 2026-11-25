# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: `T108`
- Lớp: `L3B`
- Thành viên: xem [TEAM.md](../../TEAM.md) (nhóm 2 thành viên **Lê Quý Toàn** & **Đàm Hồng Thái** phân công song song 70/30, gộp đủ 4 vai của lab).

## 2. Mục tiêu và cách tiếp cận

Nhóm dựng **hồ sơ launch v0** cho trợ lý hoàn phí **LogiX-VN** tại cổng **Gate 2a** trên mẫu dữ liệu giả lập `1.200` yêu cầu (`1.624` lần chạy). Cách tiếp cận gồm hai luồng song song:

1. **Luồng kỹ thuật & mô hình tài chính (A, B, D, E2, Hồ sơ v0 — Lê Quý Toàn):** Lập trình chuẩn hoá mô hình chi phí từ trace trong `src/lab13.py`, phân tích phân khúc và độ nhạy, thiết kế thử nghiệm ngẫu nhiên theo cụm nhân viên (`pilot_plan.yaml`), định lượng rủi ro kinh tế và tổng hợp đề xuất **Go có điều kiện**.
2. **Luồng phân loại lỗi, telemetry & kiểm định (C, Event E1, QA, Gate 2a — Đàm Hồng Thái):** Gắn nhãn độc lập 20 ca lỗi theo khung Google PAIR, đề xuất `8` event gắn `trace_id` + 2 chỉ số bổ sung, chạy kiểm thử trên máy thứ 2 và đóng vai hội đồng chấm nhóm bạn.

## 3. Giải pháp

- **Nhiệm vụ A & B ([bang_chi_phi.md](bang_chi_phi.md), [src/lab13.py](../../src/lab13.py)):** Vượt qua 3 phép thử A1 (`1,20 · 1,25 · 1,25`), áp dụng quy tắc tử số tính mọi lần chạy và mẫu số chỉ tính `ket_qua == 'thanh_cong'`. Phân rã theo 4 loại yêu cầu, cộng chi phí cố định `40 triệu đ/tháng` và chạy 9 kịch bản độ nhạy + kịch bản cả hệ thống B3 + xem lại 100% B4.
- **Nhiệm vụ C ([bang_loi.md](bang_loi.md)):** Hai thành viên tự gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR trước khi đối chiếu, đạt đồng thuận **`19/20 = 95%`** (vượt ngưỡng `80%`), thống nhất xử lý Ca 13 về *Giới hạn hệ thống* kèm quy tắc phân biệt và hoàn thiện bảng khắc phục 5 ca (Ca 1, 7, 10, 11, 5) đủ event, ngưỡng cảnh báo, tần suất và 1 vai trò phụ trách/ca.
- **Nhiệm vụ D ([pilot_plan.yaml](pilot_plan.yaml)):** Tính đủ 5 bài toán cỡ mẫu D1, đối chiếu điều kiện tách tác động D2 và tỉ lệ mở lại 7 ngày hiện tại (`4,25%`), thiết kế pilot phân tầng theo 12 depot trên 40 nhân viên (`20` vs `20`) với 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`.
- **Nhiệm vụ E ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)):** Tính thử 3 chỉ số trên 1.200 yêu cầu, bổ sung 2 chỉ số (chấp nhận gợi ý, hoàn tiền trùng) + `8` event gắn `trace_id` đã kiểm tra chéo 5/5 chỉ số, trích xuất 3 rủi ro kinh tế từ bảng độ nhạy và tổng hợp thành 1 trang hồ sơ launch v0.

## 4. Kết quả

- **Chi phí mỗi việc thành công (A2):** **`4.472 đ`** (`simulated`), gấp **`16,3 lần`** hoá đơn token + tool (`274,7 đ/yêu cầu`); chi phí giờ nhân viên chiếm **`92,5%`** (làm lại `51,8%`, xem lại `40,7%`, `simulated`). Chi phí cả hệ thống tính cả `222` ca thất bại là **`5.865 đ/yc = 0,49×`** so với mức tự làm `12.000 đ` (`simulated`).
- **Thu hẹp phạm vi & cố định (A3, A4):** Chọn `noi_dia` (`2.696 đ = 0,22×`, `95,0%` thành công, `simulated`) và `hang_nang` (`8.221 đ = 0,69×`, `74,1%` thành công, `simulated`); loại `quoc_te` (`22.515 đ = 1,88×`, `27,3%` thành công, `simulated`) và `doi_tac` (`10.215 đ = 0,85×`, `54,4%`, `simulated`). Cộng cố định `40 triệu/tháng` ở `45.000` yc/tháng đạt **`4.599 đ = 0,38×`** (`5.784 đ = 0,48×` ở nửa khối lượng, `simulated`).
- **Độ nhạy & vận hành (B1–B4):** Ba yếu tố nhạy nhất là số ca làm lại (`+51,8%`), tỉ lệ xem lại (`+40,7%`) và lương nhân viên (`+23,1%`) (`simulated`). Giới hạn chạy tối đa **2 lần** cho chi phí cả hệ thống thấp nhất (**`6.901.220 đ`**, `simulated`). Xem lại 100% đẩy chi phí lên `11.743 đ = 0,98×` (9 phút làm lại) hoặc `12.415 đ = 1,03×` (`15,30` phút làm lại trong dữ liệu, `simulated`).
- **Phân loại lỗi (C) & thiết kế pilot (D) & chỉ số (E1):** Đồng thuận CP3 **`19/20 = 95%`** (20/20 thống nhất sau Ca 13). Chỉ số chính trong đợt chạy thử là **`82,83%`** (`994/1.200`), tỉ lệ bỏ qua gợi ý **`27,12%`** (`48/177`), tỉ lệ mở lại 7 ngày **`4,25%`** (`3,97%` trong phạm vi pilot); đã thiết kế đủ `8` event gắn `trace_id`. Pilot chọn chia theo nhân viên `20` vs `20`, chấp nhận `MDE = +6 điểm` (`n = 859/arm`, `m ≥ 299`, power giảm còn `0,64` ở mức `+5 điểm`).
- **Đề xuất cuối (`ho_so_launch_v0.md`):** **Go có điều kiện** cho **pilot** `noi_dia + hang_nang`.
- **Kết quả duyệt chéo từ hội đồng:** `[Cập nhật sau phiên duyệt chéo 17:00–17:45 và hoàn thiện phiếu chấm nhóm mình tại report/team/phieu_cham.md]`.

## 5. Khó khăn và cách xử lý

- **Nhân sự nhóm 2 người thay vì 4 người:** Tái cấu trúc phân công theo 2 luồng chạy song song 70/30, tách riêng quyền sở hữu nhánh/file rồi merge có kiểm soát để tránh xung đột lớn và vẫn giữ đúng quy tắc gắn nhãn độc lập CP3 (không sao chép trước khi so).
- **Thiếu thư viện `statsmodels` ở Python hệ thống:** Tích hợp hàm `co_mau_hai_ti_le` và `power_hai_ti_le` bằng `statistics.NormalDist` chuẩn xác trong `src/lab13.py` kèm nhánh kiểm tra `try/except ImportError` cho `statsmodels` để chạy ổn định trên mọi máy kiểm tra.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong [TEAM.md](../../TEAM.md).

## 7. Hạn chế và hướng cải thiện

- **Dữ liệu thời gian nhân viên đang ở dạng `simulated`:** Cần thu thập ngay `review_minutes` và `phut_lam_lai` thực tế qua event gắn `trace_id` ngay tuần đầu bước `0.10`.
- **Hạn chế cỡ mẫu cụm (40 nhân viên):** Power ở mức cải thiện `+5 điểm` giảm còn `0,64` khi nâng MDE lên `+6 điểm`; cần theo dõi chặt chẽ đủ `≥ 299` yêu cầu/nhân viên ở bước `0.50` trước ngày chốt quyết định.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`stats.power`) và tài liệu nội bộ `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`
