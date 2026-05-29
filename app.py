import pickle
import numpy as np
import streamlit as st

# 1. NẠP MÔ HÌNH AI
with open("mo_hinh_gia_nha.pkl", "rb") as f:
    model = pickle.load(f)

# 2. CẤU HÌNH TRANG WEB
st.set_page_config(page_title="AI Định Giá Nhà", page_icon="🏠")

# --- ĐOẠN CODE ĐỔI MÀU NỀN SANG XANH DƯƠNG NHẠT ---
st.markdown("""
    <style>
    /* Đổi nền của toàn bộ ứng dụng */
    .stApp {
        background-color: #E3F2FD;
    }
    /* Làm cho các ô nhập liệu nổi bật hơn trên nền xanh */
    .stNumberInput {
        background-color: white;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. TIÊU ĐỀ
st.title("🏠 Hệ Thống Định Giá Nhà Tự Động")
st.write("Nhập thông số bên dưới để AI dự đoán giá nhà ngay lập tức.")

# --- 4. CHIA THÀNH 2 CỘT NHẬP LIỆU ---
col1, col2 = st.columns(2)

with col1:
    dien_tich = st.number_input("📐 Diện tích (m²):", min_value=30, max_value=500, value=100, step=5)
    phong_ngu = st.number_input("🛏️ Số phòng ngủ:", min_value=1, max_value=10, value=3, step=1)

with col2:
    khoang_cach = st.number_input("📍 Khoảng cách trung tâm (km):", min_value=1, max_value=50, value=5, step=1)
    phong_tam = st.number_input("🚿 Số phòng tắm:", min_value=1, max_value=5, value=2, step=1)

# 5. NÚT BẤM VÀ HIỆU ỨNG
st.write("---") # Dòng kẻ ngang cho đẹp
if st.button("💰 TÍNH GIÁ NHÀ NGAY", type="primary", use_container_width=True):
    with st.spinner('AI đang phân tích thị trường...'):
        thong_so = [[dien_tich, phong_ngu, phong_tam, khoang_cach]]
        gia_du_doan = max(0, model.predict(thong_so)[0])
        
    st.success(f"### 🏠 Giá nhà dự đoán: **{gia_du_doan:.2f}** (triệu đồng)")
    st.balloons()
