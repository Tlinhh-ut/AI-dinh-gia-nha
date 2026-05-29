import pickle
import numpy as np
import streamlit as st

# 1. NẠP MÔ HÌNH AI
with open("mo_hinh_gia_nha.pkl", "rb") as f:
    model = pickle.load(f)

# 2. CẤU HÌNH TRANG WEB
st.set_page_config(page_title="AI Định Giá Nhà", page_icon="🏠")

# --- ĐOẠN CODE ĐỔI MÀU NỀN VÀ TRANG TRÍ CHUẨN KHÔNG LỖI VIỀN ---
st.markdown("""
    <style>
    /* Đổi nền của toàn bộ ứng dụng thành xanh dương nhạt */
    .stApp {
        background-color: #E3F2FD;
    }
    
    /* FIX LỖI Ô NHẬP LIỆU */
    .stNumberInput div[data-baseweb="input"] {
        background-color: white !important;
        border-radius: 10px;
        border: 1px solid #90CAF9 !important;
    }
    
    /* Ép chữ bên trong ô luôn là màu đen */
    .stNumberInput input {
        color: black !important;
        -webkit-text-fill-color: black !important;
    }
    
    /* FIX LỖI RỚT CHỮ NHÃN (LABEL): Ép chữ và icon nằm chung một dòng, chữ màu xanh đậm rõ ràng */
    .stNumberInput label {
        display: inline-block !important;
        max-width: 100% !important;
    }
    .stNumberInput label p {
        color: #0D47A1 !important;
        font-weight: bold !important;
        display: inline !important;
        white-space: nowrap !important; /* Không cho phép tự ý xuống dòng */
    }
    
    /* TẠO KHUNG CHO TIÊU ĐỀ (Giữ nguyên phom 25px, bo góc 20px của bạn) */
    .header-box {
        background-color: #BBDEFB; /* Màu xanh dương đậm hơn màu nền */
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #90CAF9;
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* ĐỔI MÀU NÚT BẤM THÀNH MÀU ĐỎ TRẦM (Màu Đỏ Đô/Crimson) */
    div.stButton > button:first-child {
        background-color: #A31D1D !important; /* Màu đỏ trầm */
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        transition: 0.3s;
    }
    /* Hiệu ứng khi di chuột vào nút bấm sẽ đậm lên một tí */
    div.stButton > button:first-child:hover {
        background-color: #6D0B0B !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. TIÊU ĐỀ (Giữ nguyên khung màu xanh dương đậm hơn)
st.markdown("""
    <div class="header-box">
        <h1 style='margin:0; color:#0D47A1;'>🏠 Hệ Thống Định Giá Nhà Tự Động</h1>
        <p style='margin:5px 0 0 0; color:#1565C0; font-style: italic;'>Nhập thông số bên dưới để AI dự đoán giá nhà ngay lập tức.</p>
    </div>
""", unsafe_allow_html=True)

# --- 4. CHIA THÀNH 2 CỘT NHẬP LIỆU ---
col1, col2 = st.columns(2)

with col1:
    dien_tich = st.number_input("📐 Diện tích (m²):", min_value=30, max_value=500, value=30, step=5)
    phong_ngu = st.number_input("🛏️ Số phòng ngủ:", min_value=1, max_value=10, value=1, step=1)

with col2:
    khoang_cach = st.number_input("📍 Khoảng cách trung tâm (km):", min_value=1.0, max_value=50.0, value=1.0, step=0.1)
    phong_tam = st.number_input("🚿 Số phòng tắm:", min_value=1, max_value=5, value=1, step=1)

# 5. NÚT BẤM VÀ HIỆU ỨNG
st.write("---") # Dòng kẻ ngang cho đẹp
if st.button("💰 TÍNH GIÁ NHÀ NGAY", type="primary", use_container_width=True):
    with st.spinner('AI đang phân tích thị trường...'):
        thong_so = [[dien_tich, phong_ngu, phong_tam, khoang_cach]]
        gia_du_doan = max(0, model.predict(thong_so)[0])
        
    st.success(f"### 🏠 Giá nhà dự đoán: **{gia_du_doan:.2f}** (triệu đồng)")
    st.balloons()
