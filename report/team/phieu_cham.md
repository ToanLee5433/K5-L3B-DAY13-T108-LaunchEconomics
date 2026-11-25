# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): **T108** (Lớp L3B)
- Nhóm được chấm (đội trình): **HuuDuyenBL** (Lớp L3B · repo commit `01de255`)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10** | Chọn **Go có điều kiện** cho pilot `noi_dia + hang_nang` (bắt đầu `2026-12-07`, chốt `2027-01-11`). Khớp số thuận lợi (cả hệ thống `5.865 đ/yêu cầu = 0,49×`, phạm vi cộng cố định `40 triệu/tháng` đạt `4.599 đ = 0,38×`, `simulated`) **và** nêu đủ `3` số bất lợi (xem lại 100% lên `11.743–12.415 đ = 0,98×–1,03×`, power còn `0,64` ở mức `+5 điểm`, phút nhân viên ở dạng `simulated`) kèm `4` điều kiện có vai trò phụ trách và ngày kiểm tra cụ thể (khóa lùi ngày chạy nếu chưa xong điều kiện `1–2` trước `2026-12-07`). |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10** | Gắn nhãn `[simulated]`/`[sim]` đầy đủ ở các bảng `bang_chi_phi.md`, `chi_so.md`, trạng thái `Giả lập` ở mục `1, 2, 3, 7` của `ho_so_launch_v0.md` và liệt kê `simulated_inputs` trong `pilot_plan.yaml`. Phạm vi thu hẹp có cơ sở định lượng rõ: giữ `noi_dia` (`2.696 đ = 0,22×`, `95,0%` thành công) và `hang_nang` (`8.221 đ = 0,69×`, `74,1%`), loại `quoc_te` (`22.515 đ = 1,88×`, `27,3%`) và `doi_tac` (`10.215 đ = 0,85×`). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **10** | Chia theo cụm nhân viên `20 + 20` (đối chứng đồng thời, ngẫu nhiên phân tầng theo depot, có kiểm soát ảnh hưởng gián tiếp qua tài khoản và log `staff_id`), chấp nhận MDE `+6 điểm` (`n = 859/nhóm`, `m ≥ 299`, `DE = 6,96`, bước `0.50` chạy ~2 tuần cộng `7` ngày theo dõi tới `2027-01-11`). Có đủ `3` luật dừng đúng mẫu `NẾU – TRONG – THÌ – KHÔNG THÌ` kèm ngưỡng, thời hạn, `1` vai trò phụ trách/luật và rollback `30` phút. |
| **Tổng** | | | | **30 / 30** | Hồ sơ đầy đủ, đồng nhất số liệu qua các file (`bang_chi_phi.md`, `bang_loi.md` đồng thuận `17/20 = 85%`, `chi_so.md` có `10` event `trace_id`, `pilot_plan.yaml`, `ho_so_launch_v0.md`). |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ `HuuDuyenBL` chứng minh tính khả thi kinh tế rõ ràng trong phạm vi `noi_dia + hang_nang` (`0,38×` đã gồm `40 triệu đ/tháng` ở `45.000` yc/tháng, `simulated`), nhận diện trung thực `3` rủi ro bất lợi và gán đủ `4` điều kiện tiền kiểm cùng `3` luật dừng. Tuy nhiên hội đồng khuyến nghị đội làm rõ `2` điểm kỹ thuật trong luật dừng của `pilot_plan.yaml` trước ngày bắt đầu `2026-12-07` (xem câu hỏi bên dưới).

**Một câu hỏi cho đội trình:** Trong `pilot_plan.yaml`, (1) ở bước rollout `0.10` chỉ có `4` nhân viên (xác suất báo động giả khi chênh `≥ 2 điểm` là `56/1.000`), đội có tách ngưỡng tương đối `≥ 2 điểm` chỉ bật từ bước `0.25` (`10` nhân viên) không; và (2) ngưỡng chi phí `8.000 đ/việc` trong luật dừng số `2` chỉ tính chi phí biến đổi (`~3.414 đ`) hay có cộng cố định `40 triệu đ/tháng` (sẽ vọt lên `~15.300 đ` ở bước `4` người và `~8.200 đ` ở `10` người)?

**Câu trả lời của đội trình (ghi lại tại buổi):** Chưa ghi nhận phản hồi trực tiếp thêm từ đội `HuuDuyenBL` sau khi hội đồng `T108` rà soát bản hồ sơ đầy đủ trên repo (commit `01de255`) sau phiên tại lớp. Hội đồng giữ quyết định **Go có điều kiện** với khuyến nghị đội `HuuDuyenBL` làm rõ hai điểm trên trong `pilot_plan.yaml` trước ngày bắt đầu `2026-12-07`.
