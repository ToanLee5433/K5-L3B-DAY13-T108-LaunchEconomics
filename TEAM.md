# Team

## Thông tin nhóm

- Tên nhóm: `T108`
- Lớp: `L3B`
- Repo nhóm: `K5-L3B-DAY13-T108-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/ToanLee5433/K5-L3B-DAY13-T108-LaunchEconomics` · nhánh `main` (commit chốt mới nhất trên GitHub trước deadline)

## Thành viên

Nhóm gồm **2 thành viên**, làm việc song song theo tỷ lệ 70/30 và đảm nhiệm đầy đủ bốn vai của lab:

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Lê Quý Toàn | `2A202603941` | `lequytoanptit0303@gmail.com` | `ToanLee5433` | Người viết code + Người gắn nhãn 2 kiêm giữ hồ sơ |
|   2 | Đàm Hồng Thái | `2A202603927` | `thai.dh1012@gmail.com` | `itsbra1vo` | Người gắn nhãn 1 + Người kiểm số / QA duyệt chéo |

Bốn vai của lab (gộp tương ứng cho 2 thành viên):

- **Người viết code:** viết và chạy `src/lab13.py` (Lê Quý Toàn).
- **Người kiểm số:** đối chiếu số liệu `bang_chi_phi.md`, rà checklist và chạy kiểm chứng `src/lab13.py` trên máy thứ 2 + chấm nhóm bạn ở `report/team/phieu_cham.md` (Đàm Hồng Thái).
- **Người gắn nhãn 1:** đọc 20 ca lỗi, tự gắn nhãn độc lập ở CP3, lập bảng khắc phục 5 ca `report/team/bang_loi.md` và soạn E1 8 event có `trace_id` (Đàm Hồng Thái).
- **Người gắn nhãn 2 kiêm giữ hồ sơ:** tự gắn nhãn độc lập 20 ca CP3, so đồng thuận 95%, thiết kế `pilot_plan.yaml` và ghép hồ sơ `report/team/ho_so_launch_v0.md` (Lê Quý Toàn).

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## LeQuyToan-2A202603941

### Phần việc phụ trách

- Trưởng nhóm (~70% khối lượng): hoàn thiện toàn bộ mã nguồn tính toán [src/lab13.py](src/lab13.py) (nhiệm vụ A1, A2, A3, A4, B1–B4, D1, E1).
- Hoàn thiện báo cáo tài chính & độ nhạy [report/team/bang_chi_phi.md](report/team/bang_chi_phi.md), thiết kế thử nghiệm [report/team/pilot_plan.yaml](report/team/pilot_plan.yaml), phần chỉ số tính thử & rủi ro kinh tế trong [report/team/chi_so.md](report/team/chi_so.md), hồ sơ 1 trang [report/team/ho_so_launch_v0.md](report/team/ho_so_launch_v0.md) và báo cáo nhóm [report/team/group_report.md](report/team/group_report.md).
- Tự gắn nhãn độc lập 20 ca lỗi CP3, đối chiếu đồng thuận cùng Đàm Hồng Thái (`19/20 = 95%`), ghép bảng E1 + CP3 và trình bày bảo vệ trong phiên duyệt chéo Gate 2a.

### Đóng góp cụ thể

- Viết đầy đủ các hàm kinh tế chạy lại (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), mô hình chi phí từ trace (`mo_hinh`), hàm tính cỡ mẫu & power (`co_mau_hai_ti_le`, `power_hai_ti_le`, `co_mau_hieu_dung`) đạt đủ 3 phép thử A1 (`1,20`, `1,25`, `1,25`).
- Tính chi phí thật mỗi việc thành công (`4.472 đ`, `simulated`, gấp `16,3×` hoá đơn `274,7 đ/yc`), bóc tách 4 loại yêu cầu để thu hẹp phạm vi pilot về `noi_dia + hang_nang`, phân tích 9 kịch bản độ nhạy B1, chi phí cả hệ thống B3 (tối ưu ở giới hạn 2 lần = `6.901.220 đ`, `simulated`) và kịch bản xem lại 100% B4 (`11.743 đ`–`12.415 đ`, `simulated`).
- Tính cỡ mẫu pilot D1 và chốt phương án chia theo nhân viên (`20` vs `20`), chấp nhận đánh đổi MDE `+6 điểm` (`n = 859`, `m ≥ 299`, power còn `0,64` nếu hiệu ứng thật `+5 điểm`), viết đủ 3 luật dừng 4 vế và hoàn thiện đề xuất **Go có điều kiện**.
- Hoàn thành lượt gắn nhãn độc lập thứ hai 20 ca lỗi, cùng Đàm Hồng Thái thống nhất Ca 13 về *Giới hạn hệ thống* và gộp nhánh hoàn chỉnh lên `main`.

### Bằng chứng

- Code & tài liệu chính: `src/lab13.py` (`Ba phép thử đáp án biết trước: ĐẠT`), `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml` (pass `yaml.safe_load`, không còn dấu `?`), `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/2A202603941_LeQuyToan.md`.

## DamHongThai-2A202603927

### Phần việc phụ trách

- Thành viên 2 (~30% khối lượng): gắn nhãn độc lập 20 ca lỗi Google PAIR (Nhiệm vụ C), viết quy tắc ca ranh giới và lập bảng khắc phục 5 ca trong [report/team/bang_loi.md](report/team/bang_loi.md).
- Soạn 2 chỉ số tự đề xuất (chấp nhận gợi ý, hoàn tiền trùng), danh sách `8` event gắn `trace_id` và bảng kiểm tra chéo cho [report/team/chi_so.md](report/team/chi_so.md).
- Kiểm số, chạy kiểm thử `src/lab13.py` trên máy thứ 2, rà soát checklist và phụ trách chấm hồ sơ nhóm khác ở [report/team/phieu_cham.md](report/team/phieu_cham.md) trong phiên duyệt chéo Gate 2a.

### Đóng góp cụ thể

- Đẩy các commit `c1aa62f`, `a4e35d3`, `5fb8bfb`, `62f8432` trên nhánh `2A202603927_DamHongThai` hoàn thiện bộ nhãn độc lập đầu tiên 20 ca (`19/20 = 95%` đồng thuận khi ghép với Lê Quý Toàn), quy tắc phân biệt và bảng khắc phục 5 ca (Ca 1, 7, 10, 11, 5) có đủ event, ngưỡng cảnh báo định lượng, tần suất và 1 vai trò phụ trách/ca.
- Thiết kế trọn vẹn `8` event có `trace_id` (`request_received`, `agent_run_completed`, `recommendation_presented`, `staff_review_decision`, `refund_posted`, `customer_notified`, `request_closed`, `request_reopened`), 2 chỉ số bổ sung và kiểm tra chéo cho 5/5 chỉ số ở E1.
- Tham gia phiên duyệt chéo Gate 2a (các commit `4912eb7`, `802d2c3`, `5b46d5d`) và hoàn thiện phiếu chấm nhóm `HuuDuyenBL` tại `report/team/phieu_cham.md`.

### Bằng chứng

- Nhánh `2A202603927_DamHongThai` (commit `62f8432`, đã merge vào `main`): `report/team/bang_loi.md`, `report/team/chi_so.md` (phần E1), `report/team/2A202603927_DamHongThai.md`.
- Phiếu chấm duyệt chéo Gate 2a (`HuuDuyenBL`): `report/team/phieu_cham.md`.
