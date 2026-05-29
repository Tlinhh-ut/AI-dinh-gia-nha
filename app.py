import pickle
import numpy as np
import streamlit as st

# 1. NẠP MÔ HÌNH AI
with open("mo_hinh_gia_nha.pkl", "rb") as f:
    model = pickle.load(f)

# 2. CẤU HÌNH TRANG WEB
st.set_page_config(page_title="AI Định Giá Nhà", page_icon="🏠")

# --- ĐOẠN CODE ĐỔI MÀU NỀN VÀ SỬA LỖI CHỮ TÀNG HÌNH KHI ĐỂ DARK MODE ---
st.markdown("""
    <style>
    /* 1. Đổi nền của toàn bộ ứng dụng thành màu xanh dương nhạt (Chỉ áp dụng ở Light Mode để không phá giao diện Dark) */
    @media (prefers-color-scheme: light) {
        .stApp {
            background-color: #E3F2FD;
        }
    }
    
    /* 2. FIX LỖI MẤT CHỮ: Sử dụng màu nền ô nhập liệu thích ứng tự động theo giao diện hệ thống */
    .stNumberInput div[data-baseweb="input"] {
        border-radius: 10px;
    }
    
    /* 3. TẠO KHUNG CHO TIÊU ĐỀ (Tự động đổi màu chữ theo chế độ sáng/tối) */
    .header-box {
        background-color: #BBDEFB; /* Màu khung mặc định */
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #90CAF9;
        text-align: center;
        margin-bottom: 25px;
    }
    /* Nếu người dùng bật Dark Mode, chỉnh khung tiêu đề sẫm màu lại cho đỡ chói */
    @media (prefers-color-scheme: dark) {
        .header-box {
            background-color: #0D47A1;
            border-color: #1565C0;
        }
        .header-box h1, .header-box p {
            color: #FFFFFF !important;
        }
    }
    
    /* 4. ĐỔI MÀU NÚT BẤM THÀNH MÀU ĐỎ TRẦM (Màu Đỏ Đô/Crimson) */
    div.stButton > button:first-child {
        background-color: #A31D1D !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #6D0B0B !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. TIÊU ĐỀ (Được tinh chỉnh để đổi màu chữ động theo chế độ sáng/tối)
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
st.write("---") 
if st.button("💰 TÍNH GIÁ NHÀ NGAY", type="primary", use_container_width=True):
    with st.spinner('AI đang phân tích thị trường...'):
        thong_so = [[dien_tich, phong_ngu, phong_tam, khoang_cach]]
        gia_du_doan = max(0, model.predict(thong_so)[0])
        
    st.success(f"### 🏠 Giá nhà dự đoán: **{gia_du_doan:.2f}** (triệu đồng)")
    st.balloons()
