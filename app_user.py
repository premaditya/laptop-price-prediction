import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib

st.set_page_config(
    page_title="Laptop Price Prediction",
    page_icon="💻",
    layout="wide"
)

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        135deg,
        #0B1120 0%,
        #111827 50%,
        #1E293B 100%
    );
}

h1 {
    display: table;
    margin: 0 auto 10px auto;

    font-size: 2.6rem !important;
    font-weight: 900;

    color: #FFFFFF;

    padding: 12px 28px;

    background: linear-gradient(135deg,#1C1F26,#252A34);
    border: 1px solid #2E3440;
    border-radius: 18px;

    box-shadow: 0 4px 15px rgba(0,0,0,0.25);
}   

h2 {
    color: #4F8BF9;
    font-size: 1.35rem !important;
    font-weight: 600;
}

h3 {
    color: #4F8BF9;
}
div[data-testid="stHorizontalBlock"] {
    background: #1C1F26;
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.25);
}

.stButton > button {
    background: transparent;
    color: #4F8BF9;
    border: 2px solid #4F8BF9;
    border-radius: 999px;
    height: 50px;
    min-width: 180px;
    font-size: 16px;
    font-weight: 600;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: #4F8BF9;
    color: white;
    box-shadow: 0 0 15px rgba(79,139,249,0.4);
}

div.stButton {
    display: flex;
    justify-content: center;
}
            
.predict-container {
    display: flex;
    justify-content: center;
    margin: 25px 0;
}

div[data-testid="stMetric"] {
    background: linear-gradient(135deg,#1C1F26,#252A34);
    border: 1px solid #2E3440;
    border-radius: 18px;
    padding: 25px;
    text-align: center;
}

[data-testid="stMetricLabel"] {
    color: #A0AEC0;
    font-size: 16px;
}

[data-testid="stMetricValue"] {
    color: #4F8BF9;
    font-size: 48px;
    font-weight: 700;
}

div[data-testid="stDataFrame"] {
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)


model = joblib.load("model.pkl")

st.markdown("""
<div style="text-align:center; margin-bottom:10px;">
    <span style="
        display:inline-block;
        font-size:2.8rem;
        font-weight:900;
        padding:12px 28px;
        border-radius:18px;
        border:1px solid #2E3440;
        background:linear-gradient(135deg,#1C1F26,#252A34);
        box-shadow:0 4px 15px rgba(0,0,0,0.25);
    ">
        <span style="
            background:linear-gradient(90deg,#FFFFFF,#4F8BF9);
            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;
        ">
            Laptop Price Prediction
        </span>
    </span>
</div>
""", unsafe_allow_html=True)
st.markdown(
    """
    <p style='text-align:center;
              color:#9CA3AF;
              font-size:16px;
              margin-top:-10px;
              margin-bottom:20px;'>
        Machine Learning Powered Price Estimation
    </p>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# -------- Laptop Information --------
st.header("💻 Laptop Information")
col1, col2 = st.columns(2)

with col1:

    Company = st.selectbox(
        "Company",["Select Company"] +
        [
            "Acer", "Apple", "Asus", "Chuwi", "Dell",
            "Fujitsu", "Google", "HP", "Huawei", "LG",
            "Lenovo", "Mediacom", "Microsoft", "MSI",
            "Razer", "Samsung", "Toshiba", "Vero", "Xiaomi"
        ]
    )

    TypeName = st.selectbox(
        "Type",["Select Type"] +
        [
            "Notebook", "Gaming", "Ultrabook",
            "2 in 1 Convertible", "Workstation", "Netbook"
        ]
    )

    Os = st.selectbox(
        "Operating System",["Select Operating System"]+
        [
            "Windows", "No OS", "Linux",
            "Chrome OS", "Mac", "Other"
        ]
    )

with col2:

    Cpu_brand = st.selectbox(
        "CPU Brand",["Select CPU"]+
        [
            "Intel Core i7",
            "Intel Core i5",
            "Intel Core i3",
            "Other Intel Processor",
            "AMD Processor",
            "Other Processor"
        ]
    )

    Gpu_brand = st.selectbox(
        "GPU Brand",["Select GPU"]+
        [
            "Intel",
            "Nvidia",
            "AMD",
            "ARM"
        ]
    )

    Ram = st.number_input(
        "RAM (GB)",
        min_value=2,
        max_value=64,
        value=8,
        step=2
    )
# -------- Display Specifications --------
st.header("🖥️ Display Specifications")

d1, d2, d3 = st.columns(3)

with d1:
    Inches = st.number_input(
        "Screen Size (Inches)",
        min_value=10.0,
        max_value=19.0,
        value=15.6,
        step=0.1
    )

with d2:
    Width = st.number_input(
        "Resolution Width (px)",
        min_value=1300,
        max_value=3840,
        value=1920,
        step=10
    )

with d3:
    Height = st.number_input(
        "Resolution Height (px)",
        min_value=760,
        max_value=2160,
        value=1080,
        step=10
    )

d4, d5, d6 = st.columns(3)

with d4:
    Weight = st.number_input(
        "Weight (kg)",
        min_value=0.69,
        max_value=5.0,
        value=2.0,
        step=0.01
    )

with d5:
    Touchscreen = st.radio(
        "Touchscreen",
        ["Yes", "No"],
        horizontal=True
    )

with d6:
    Ips = st.radio(
        "IPS Display",
        ["Yes", "No"],
        horizontal=True
    )

Touchscreen = 1 if Touchscreen == "Yes" else 0
Ips = 1 if Ips == "Yes" else 0
# -------- Storage Specifications --------
st.header("💾 Storage Specifications")

s1, s2, s3, s4 = st.columns(4)

with s1:
    Ssd = st.number_input(
        "SSD (GB)",
        min_value=0,
        max_value=2000,
        value=256,
        step=10
    )

with s2:
    Hdd = st.number_input(
        "HDD (GB)",
        min_value=0,
        max_value=4000,
        value=0,
        step=10
    )

with s3:
    Flash_Storage = st.number_input(
        "Flash Storage (GB)",
        min_value=0,
        max_value=512,
        value=0,
        step=10
    )

with s4:
    Hybrid = st.number_input(
        "Hybrid Storage (GB)",
        min_value=0,
        max_value=2000,
        value=0,
        step=10
    )

# -------- Calculated Feature --------
Ppi = np.sqrt(Width**2 + Height**2) / Inches

#-------Creating a input DataFrame---------
input_data = pd.DataFrame({
    "Company": [Company],
    "TypeName": [TypeName],
    "Inches" : [Inches],
    "Ram" : [Ram],
    "Weight": [Weight],
    "Touchscreen": [Touchscreen],
    "IPS": [Ips],
    "Width": [Width],
    "Height": [Height],
    "PPI": [Ppi],
    "Cpu_Brand": [Cpu_brand],
    "SSD": [Ssd],
    "HDD": [Hdd],
    "Flash_Storage": [Flash_Storage],
    "Hybrid": [Hybrid],
    "Gpu_Brand": [Gpu_brand],
    "OS": [Os]
})

st.markdown("""
<div class="predict-container">
""", unsafe_allow_html=True)

predict = st.button("Predict Price")

st.markdown("""
</div>
""", unsafe_allow_html=True)

#-------Prediction----------
if predict:

    if Company == "Select Company":
        st.error("Please select a company")

    elif TypeName == "Select Type":
        st.error("Please select a laptop type")

    elif Cpu_brand == "Select CPU":
        st.error("Please select a CPU brand")

    elif Gpu_brand == "Select GPU":
        st.error("Please select a GPU brand")

    elif Os == "Select Operating System":
        st.error("Please select an operating system")

    else:
        prediction = model.predict(input_data)

        st.subheader("📋 Specifications")
        st.dataframe(input_data)

        st.subheader("💰 Predicted Price")

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.metric(
                label="Estimated Laptop Price",
                value=f"€ {prediction[0]:,.2f}"
            )

        st.markdown("---")

st.caption("Built using Streamlit and K-Nearest Neighbors Regression")