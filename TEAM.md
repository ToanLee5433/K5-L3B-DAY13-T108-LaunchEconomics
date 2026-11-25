# Team

## Thông tin nhóm

- Tên nhóm: `T108`
- Lớp: `L3B`
- Repo nhóm: `K5-L3B-DAY13-T108-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/ToanLee5433/K5-L3B-DAY13-T108-LaunchEconomics` · nhánh `main` · commit `[cập nhật khi push chốt cuối buổi]`

## Thành viên

Nhóm gồm **2 thành viên**, làm việc song song theo tỷ lệ 70/30 và đảm nhiệm đầy đủ bốn vai của lab:

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Lê Quý Toàn | `2A202603941` | `lequytoanptit0303@gmail.com` | `ToanLee5433` | Người viết code + Người gắn nhãn 1 kiêm giữ hồ sơ |
|   2 | [Điền Họ tên thành viên 2] | [MSSV] | [Email] | [GitHub] | Người gắn nhãn 2 + Người kiểm số / QA duyệt chéo |

Bốn vai của lab (gộp tương ứng cho 2 thành viên):

- **Người viết code:** viết và chạy `src/lab13.py` (Thành viên 1).
- **Người kiểm số:** đối chiếu số liệu từ `bang_chi_phi.md`, rà checklist và chạy kiểm chứng `src/lab13.py` trên máy thứ 2 (Thành viên 2).
- **Người gắn nhãn 1 kiêm giữ hồ sơ:** tự gắn nhãn độc lập 20 ca CP3 và ghép kết quả vào `report/team/ho_so_launch_v0.md` (Thành viên 1).
- **Người gắn nhãn 2:** đọc 20 ca lỗi, tự gắn nhãn độc lập ở CP3, so đồng thuận và hoàn thiện `report/team/bang_loi.md` + soạn nháp Event E1 + ghi `report/team/phieu_cham.md` (Thành viên 2).

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
- Tham gia gắn nhãn độc lập 20 ca lỗi CP3 và trình bày 1 phút trong phiên duyệt chéo Gate 2a.

### Đóng góp cụ thể

- Viết đầy đủ các hàm kinh tế chạy lại (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), mô hình chi phí từ trace (`mo_hinh`), hàm tính cỡ mẫu & power (`co_mau_hai_ti_le`, `power_hai_ti_le`, `co_mau_hieu_dung`) đạt đủ 3 phép thử A1 (`1,20`, `1,25`, `1,25`).
- Tính chi phí thật mỗi việc thành công (`4.472 đ`, `simulated`, gấp `16,3×` hoá đơn `274,7 đ/yc`), bóc tách 4 loại yêu cầu để thu hẹp phạm vi pilot về `noi_dia + hang_nang`, phân tích 9 kịch bản độ nhạy B1, chi phí cả hệ thống B3 (tối ưu ở giới hạn 2 lần = `6.901.220 đ`, `simulated`) và kịch bản xem lại 100% B4 (`11.743 đ`–`12.415 đ`, `simulated`).
- Tính cỡ mẫu pilot D1 và chốt phương án chia theo nhân viên (`20` vs `20`), chấp nhận đánh đổi MDE `+6 điểm` (`n = 859`, `m ≥ 299`, power còn `0,64` ở mức `+5 điểm`), viết đủ 3 luật dừng 4 vế và hoàn thiện đề xuất **Go có điều kiện**.

### Bằng chứng

- File code chạy hoàn chỉnh: `src/lab13.py` (`Ba phép thử đáp án biết trước: ĐẠT`).
- Các file hồ sơ đã hoàn thiện: `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml` (pass `yaml.safe_load`, không còn dấu `?`), `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, và báo cáo cá nhân `report/team/2A202603941_LeQuyToan.md`.

## [HoVaTen-MSSV thành viên 2]

### Phần việc phụ trách

- Gắn nhãn độc lập 20 ca lỗi & hoàn thiện `report/team/bang_loi.md`; đề xuất 2 chỉ số + ≥ 6 event có `trace_id` cho `report/team/chi_so.md`; kiểm chứng `src/lab13.py` trên máy thứ 2 & soát checklist; điền phiếu chấm Gate 2a `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- [Cập nhật sau Đồng bộ 1 & Duyệt chéo]

### Bằng chứng

- [Cập nhật file `report/team/bang_loi.md`, `report/team/phieu_cham.md`, `report/team/<MSSV>_<HoTen>.md`]
