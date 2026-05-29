import pickle
import numpy as np
import streamlit as st

# 1. NẠP MÔ HÌNH AI
with open("mo_hinh_gia_nha.pkl", "rb") as f:
    model = pickle.load(f)

# 2. CẤU HÌNH TRANG WEB
st.set_page_config(page_title="AI Định Giá Nhà", page_icon="🏠")

# --- ĐOẠN CODE TRANG TRÍ VÀ FIX LỖI MÀU Ô NHẬP LIỆU ---
st.markdown("""
    <style>
    /* Đổi nền của toàn bộ ứng dụng thành màu xanh dương nhạt */
    .stApp {
        background-color: #E3F2FD;
    }
    
    /* KHUNG TIÊU ĐỀ XANH DƯƠNG (Giữ nguyên phom chuẩn của bạn ở ảnh c95fc0) */
    .header-box {
        background-color: #BBDEFB;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #90CAF9;
        text-align: center;
        margin-bottom: 25px;
    }
    .header-box h1 {
        margin: 0; 
        color: #0D47A1;
    }
    .header-box p {
        margin: 5px 0 0 0; 
        color: #1565C0; 
        font-style: italic;
    }

    /* FIX LỖI: Ép các ô nhập liệu luôn luôn có nền trắng, chữ đen rõ ràng, không bị hóa đen */
    .stNumberInput div[data-baseweb="input"] {
        background-color: white !important;
        border-radius: 10px;
        border: 1px solid #90CAF9 !important;
    }
    .stNumberInput input {
        color: black !important;
        -webkit-text-fill-color: black !important; /* Đảm bảo hiện chữ đen trên một số trình duyệt */
    }
    
    /* Ép chữ nhãn (Label) phía trên các ô nhập số phải là màu tối để nhìn rõ trên nền xanh nhạt */
    .stNumberInput label p {
        color: #0D47A1 !important;
        font-weight: bold;
    }
    
    /* ĐỔI MÀU NÚT BẤM THÀNH MÀU ĐỎ TRẦM */
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

# 3. HIỂN THỊ TIÊU ĐỀ TRONG KHUNG
st.markdown("""
    <div class="header-box">
        <h1>🏠 Hệ Thống Định Giá Nhà Tự Động</h1>
        <p>Nhập thông số bên dưới để AI dự đoán giá nhà ngay lập tức.</p>
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
        
    st.success(f"###
