"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D dùng scipy/statsmodels hoặc statistics.NormalDist)
Không cần khoá API. Đã hoàn thiện các mục TODO CP1…CP4 và E1. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
from statistics import NormalDist

import pandas as pd

try:
    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize
except ImportError:
    NormalIndPower = None
    proportion_effectsize = None

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26                    # đồng cho 1.000 token đầu vào
GIA_RA = 130                    # đồng cho 1.000 token đầu ra
GIA_TOOL = 15                   # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000               # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000                # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000
QUY_MO_THANG = 45_000


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1.0 / p
    return (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs_sub = reqs.copy()
    runs_sub = runs[runs['request_id'].isin(reqs_sub['request_id'])].copy()
    if max_lan_chay is not None:
        runs_sub = runs_sub[runs_sub['attempt'] <= max_lan_chay]
        vuot = reqs_sub['so_lan_chay'] > max_lan_chay
        reqs_sub.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs_sub.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs_sub['tokens_in'] / 1000.0 * gia_vao + runs_sub['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs_sub['tool_calls'] * gia_tool
    xem_lai = reqs_sub['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs_sub['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = float(tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai)
    thanh_cong = int((reqs_sub['ket_qua'] == 'thanh_cong').sum())
    chay_lai = float((tien_token + tien_tool)[runs_sub['attempt'] > 1].sum())
    hoa_don_moi_yc = float((tien_token.sum() + tien_tool.sum()) / len(reqs_sub))
    return dict(
        token=float(tien_token.sum()),
        tool=float(tien_tool.sum()),
        chay_lai=chay_lai,
        xem_lai=float(xem_lai),
        lam_lai=float(lam_lai),
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=hoa_don_moi_yc,
    )


# ---------- Nhiệm vụ D1 · Cỡ mẫu và power theo cụm ----------
def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm khi so sánh hai tỉ lệ độc lập (two-sided)."""
    dist = NormalDist()
    za = dist.inv_cdf(1.0 - alpha / 2.0)
    zb = dist.inv_cdf(power)
    p_bar = (p1 + p2) / 2.0
    tu = za * math.sqrt(2.0 * p_bar * (1.0 - p_bar)) + zb * math.sqrt(p1 * (1.0 - p1) + p2 * (1.0 - p2))
    return math.ceil((tu / (p2 - p1)) ** 2)


def power_hai_ti_le(p1, p2, n_per_arm, alpha=0.05):
    """Power đạt được với cỡ mẫu n_per_arm mỗi nhóm khi phát hiện mức chênh p2 - p1."""
    dist = NormalDist()
    za = dist.inv_cdf(1.0 - alpha / 2.0)
    p_bar = (p1 + p2) / 2.0
    se_null = math.sqrt(2.0 * p_bar * (1.0 - p_bar))
    se_alt = math.sqrt(p1 * (1.0 - p1) + p2 * (1.0 - p2))
    zb = (abs(p2 - p1) * math.sqrt(n_per_arm) - za * se_null) / se_alt
    return dist.cdf(zb)


def co_mau_hieu_dung(so_cum, moi_cum, icc=0.02):
    """Tính (design_effect, n_eff) khi chia ngẫu nhiên theo cụm."""
    de = 1.0 + (moi_cum - 1.0) * icc
    return de, (so_cum * moi_cum) / de


def in_phan_a(runs, reqs):
    """In kết quả A2, A3 và A4."""
    ket_qua = mo_hinh(runs, reqs)
    print('\n=== A2 · Mô hình chi phí từ trace (phần nhân viên là simulated) ===')
    for ten, gia_tri in ket_qua.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:14s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:14s} {gia_tri:>14,.0f}')

    n_reqs = len(reqs)
    khong_tc = n_reqs - ket_qua['thanh_cong']
    he_thong_moi_yc = (ket_qua['tong'] + khong_tc * BASELINE) / n_reqs
    print(f"Gấp hoá đơn/yc : {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần [simulated]")
    print(f"Tỉ trọng làm lại: {ket_qua['lam_lai'] / ket_qua['tong'] * 100:.1f}% · xem lại: {ket_qua['xem_lai'] / ket_qua['tong'] * 100:.1f}% [simulated]")
    print(f"Cả hệ thống/yc : {he_thong_moi_yc:,.0f} đ ({he_thong_moi_yc / BASELINE:.2f}x của {BASELINE:,} đ) [simulated]")

    print('\n=== A3 · Tách theo loại yêu cầu [chi phí có phần simulated] ===')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub_reqs = reqs[reqs['loai'] == loai]
        sub_runs = runs[runs['request_id'].isin(sub_reqs['request_id'])]
        r = mo_hinh(runs, sub_sub := sub_reqs)
        rate = r['thanh_cong'] / len(sub_sub) * 100
        runs_per_req = len(sub_runs) / len(sub_sub)
        print(f"{loai:10s} | n={len(sub_sub):3d} | thành công={rate:5.1f}% | chạy/yc={runs_per_req:4.2f} | cps={r['cps']:8,.0f} đ ({r['cps']/BASELINE:4.2f}x) [sim]")

    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = (merged['status'] == 'ok').astype(int)
    pivot_ok = merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    print('\nTỉ lệ ok (%) theo lần thử (attempt):')
    print(pivot_ok.round(1).to_string())

    print('\n=== A4 · Chi phí cố định 40 triệu/tháng (phạm vi noi_dia + hang_nang) [simulated] ===')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    tc_thang = QUY_MO_THANG * kq_pv['thanh_cong'] / len(reqs)
    for nhan, khoi_luong, tc in [
        ('Đầy đủ 45.000 yc/tháng', QUY_MO_THANG, tc_thang),
        ('Một nửa (22.500 yc/tháng)', QUY_MO_THANG // 2, tc_thang / 2),
    ]:
        co_dinh = CHI_PHI_CO_DINH_THANG / tc
        tong_cps = kq_pv['cps'] + co_dinh
        print(f"{nhan:27s} | tc/tháng={tc:7,.0f} | cố định={co_dinh:5,.0f} đ | tổng cps={tong_cps:6,.0f} đ ({tong_cps/BASELINE:.2f}x) [sim]")


def in_phan_b(runs, reqs):
    """In kết quả B1, B2, B3 và B4."""
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = [
        ('Giá token gấp đôi', dict(gia_vao=52, gia_ra=260)),
        ('Giá token giảm một nửa', dict(gia_vao=13, gia_ra=65)),
        ('Tỉ lệ xem lại gấp đôi', dict(he_so_xem_lai=2.0)),
        ('Tỉ lệ xem lại giảm một nửa', dict(he_so_xem_lai=0.5)),
        ('Số ca làm lại gấp đôi', dict(he_so_lam_lai=2.0)),
        ('Số ca làm lại giảm một nửa', dict(he_so_lam_lai=0.5)),
        ('Lương nhân viên tăng 25%', dict(luong_phut=2500)),
        ('Chỉ cho chạy tối đa 2 lần', dict(max_lan_chay=2)),
        ('Chỉ cho chạy 1 lần', dict(max_lan_chay=1)),
    ]
    print('\n=== B1 · Bảng độ nhạy [simulated] ===')
    for ten, kw in kich_ban:
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f"{ten:28s} | {cps:6,.0f} đ | {(cps / goc - 1.0) * 100:+6.1f}%")

    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print('\n=== B2 · Đổi một cặp & xếp hạng [simulated] ===')
    print(f"Token x2 + Xem lại x2        | {cps_cap:6,.0f} đ | {(cps_cap / goc - 1.0) * 100:+6.1f}%")
    print('Xếp hạng mạnh nhất: 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%)')

    print('\n=== B3 · Chi phí cả hệ thống theo giới hạn chạy lại [simulated] ===')
    for gioihan in [1, 2, 3]:
        r = mo_hinh(runs, reqs, max_lan_chay=gioihan)
        khong_tc = len(reqs) - r['thanh_cong']
        ca_he_thong = r['tong'] + khong_tc * BASELINE
        print(f"Tối đa {gioihan} lần | trợ lý={r['tong']:9,.0f} đ | thất bại={khong_tc:3d} | cả hệ thống={ca_he_thong:9,.0f} đ | cps={r['cps']:5,.0f} đ [sim]")

    print('\n=== B4 · Xem lại 100% trong phạm vi noi_dia + hang_nang [simulated] ===')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    pv_runs = runs[runs['request_id'].isin(pham_vi['request_id'])]
    so_xem_100 = pv_runs[pv_runs['status'] == 'ok']['request_id'].nunique()
    so_lam_lai_pv = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    so_tc_pv = int((pham_vi['ket_qua'] == 'thanh_cong').sum())
    hoa_don_pv = float((pv_runs['tokens_in'] / 1000.0 * GIA_VAO + pv_runs['tokens_out'] / 1000.0 * GIA_RA + pv_runs['tool_calls'] * GIA_TOOL).sum())
    tb_phut_lam_lai = float(reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean())

    for nhan, phut_lam_lai in [('Giả định đề (9 phút/ca)', 9.0), (f'Trung bình dữ liệu ({tb_phut_lam_lai:.2f} phút/ca)', tb_phut_lam_lai)]:
        tong_b4 = hoa_don_pv + so_xem_100 * 5.0 * LUONG_PHUT + so_lam_lai_pv * phut_lam_lai * LUONG_PHUT
        cps_b4 = tong_b4 / so_tc_pv
        hoa_von_xem = (BASELINE * so_tc_pv - hoa_don_pv - so_lam_lai_pv * phut_lam_lai * LUONG_PHUT) / (so_xem_100 * LUONG_PHUT)
        print(f"{nhan:34s} | tổng={tong_b4:10,.0f} đ | cps={cps_b4:6,.0f} đ ({cps_b4/BASELINE:.2f}x) | hoà vốn xem lại <= {hoa_von_xem:.2f} phút [sim]")


def in_phan_d_va_e(reqs):
    """In kết quả cỡ mẫu D1, chỉ số an toàn hiện tại và 3 chỉ số E1."""
    print('\n=== D1 · Cỡ mẫu pilot (baseline=0,70, alpha=0,05, power=0,80, ICC=0,02) ===')
    n_5pt = co_mau_hai_ti_le(0.70, 0.75)
    de_75, _ = co_mau_hieu_dung(1, 75, 0.02)
    n_nv75 = math.ceil(n_5pt * de_75)
    so_nv_moi_nhom = math.ceil(n_nv75 / 75)
    max_nv20 = 20 / 0.02
    max_depot6 = 6 / 0.02
    n_6pt = co_mau_hai_ti_le(0.70, 0.76)
    m_min = math.ceil(n_6pt * (1.0 - 0.02) / (20.0 - n_6pt * 0.02))
    de_m, n_eff_m = co_mau_hieu_dung(20, m_min, 0.02)
    pwr_5pt_at_859 = power_hai_ti_le(0.70, 0.75, n_6pt)

    print(f"a) Chia theo yêu cầu (MDE +5 điểm)     : {n_5pt:,} yêu cầu/nhóm")
    print(f"b) Theo nhân viên (m=75)               : DE={de_75:.2f}, n={n_nv75:,}/nhóm -> {so_nv_moi_nhom} người/nhóm (tổng {so_nv_moi_nhom*2} > 40: không đủ)")
    print(f"c) 20 nhân viên/nhóm (trần c/ICC)      : tối đa {max_nv20:,.0f} < {n_5pt:,} (không đạt MDE 5 điểm)")
    print(f"d) 6 depot/nhóm (trần c/ICC)           : tối đa {max_depot6:,.0f} (không đạt)")
    print(f"e) MDE +6 điểm ({n_6pt}/nhóm), 20 nv/nhóm : cần m >= {m_min} yc/người (DE={de_m:.2f}, n_eff={n_eff_m:,.0f}); power ở mức 5 điểm={pwr_5pt_at_859:.2f}")

    if NormalIndPower is not None and proportion_effectsize is not None:
        es5 = proportion_effectsize(0.70, 0.75)
        n_sm = math.ceil(NormalIndPower().solve_power(effect_size=abs(es5), power=0.80, alpha=0.05))
        print(f"   (Đối chiếu statsmodels MDE 5đ: {n_sm:,} yêu cầu/nhóm)")

    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    print(f"Tỉ lệ mở lại 7 ngày hiện tại           : toàn mẫu={(reqs['mo_lai_trong_7_ngay']==1).mean()*100:.2f}% ({(reqs['mo_lai_trong_7_ngay']==1).sum()}/{len(reqs)}), phạm vi pilot={(pham_vi['mo_lai_trong_7_ngay']==1).mean()*100:.2f}% ({(pham_vi['mo_lai_trong_7_ngay']==1).sum()}/{len(pham_vi)})")

    print('\n=== E1 · Ba chỉ số tính thử trên 1.200 yêu cầu ===')
    chinh_mask = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua_mask = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    an_toan_mask = reqs['mo_lai_trong_7_ngay'] == 1
    print(f"Chính (đóng 24h, không mở lại 7 ngày)  : {chinh_mask.mean()*100:.2f}% ({int(chinh_mask.sum())}/{len(reqs)})")
    print(f"Dùng (tỉ lệ bỏ qua gợi ý: sửa + bỏ)    : {bo_qua_mask.mean()*100:.2f}% ({int(bo_qua_mask.sum())}/{len(xem)})")
    print(f"An toàn (lỗi lọt đến khách / mở lại 7n): {an_toan_mask.mean()*100:.2f}% ({int(an_toan_mask.sum())}/{len(reqs)})")


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_phan_a(runs, reqs)
    in_phan_b(runs, reqs)
    in_phan_d_va_e(reqs)
