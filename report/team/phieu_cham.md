# Phiếu chấm hội đồng Gate 2a

- Nhóm chấm (hội đồng): **T108**
- Nhóm được chấm: **HuuDuyenBL**

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **5** | Transcript chưa có đề xuất Go/No-go để đối chiếu trực tiếp. Phân tích có số thuận lợi là **5.865 đ/yêu cầu**, bằng **0,49×** nhân viên tự làm; đồng thời nêu bất lợi như `quoc_te` **22.515 đ/việc thành công (1,88×)** và kịch bản xem lại kéo dài **12.415 đ (1,03×)**. Tạm 5 điểm vì chưa thấy hồ sơ quyết định cho biết nhóm xử lý các số bất lợi ra sao. |
| Số giả lập và phạm vi | Không nhãn; phạm vi “mọi yêu cầu” | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10** | Transcript gắn `[simulated]` cho chi phí và tác động từ thời gian nhân viên; A3 phân tích đủ **4 loại** và A4 nêu phạm vi `noi_dia + hang_nang` (**982 yêu cầu**, CPS cơ sở **3.414 đ** trước chi phí cố định), có lý do số liệu để loại `quoc_te` (**22.515 đ**, **1,88×** mức tự làm). Điểm dựa trên transcript, chưa xác minh cách gắn nhãn trong các hồ sơ Markdown. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **5** | D1 tính được yêu cầu **1.251/nhóm** cho MDE +5 điểm, thừa nhận 40 nhân viên không đủ cho thiết kế đó; phương án MDE +6 điểm là **859/nhóm**, **299 yêu cầu/nhân viên**, nhưng power chỉ **0,64** nếu hiệu ứng thật là +5 điểm. Transcript không có bằng chứng về phân bổ ngẫu nhiên/đối chứng đồng thời hoặc luật dừng có ngưỡng, thời hạn và người quyết định. |
| **Tổng** | | | | **20 / 30** | **Điểm sơ bộ theo transcript; cần hồ sơ launch và pilot plan để chốt hai tiêu chí chưa xác minh.** |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Kết quả chạy cho thấy chi phí hệ thống trung bình **5.865 đ/yêu cầu** thấp hơn mức tự làm **12.000 đ**, nhưng lợi thế không áp dụng cho `quoc_te` (**22.515 đ**) và có thể mất khi xem lại 100% với thời gian làm lại trung bình (**12.415 đ**). Chỉ xem xét pilot nếu thu hẹp phạm vi theo A3 và hồ sơ pilot xác nhận thiết kế đối chứng cùng luật dừng đầy đủ.

**Một câu hỏi cho đội trình:** Trong `pilot_plan.yaml`, đơn vị phân nhóm và cách bảo đảm đối chứng chạy đồng thời, ngẫu nhiên là gì; luật dừng an toàn áp dụng ngưỡng nào, theo dõi bao lâu và vai trò nào có quyền dừng?

