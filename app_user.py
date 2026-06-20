import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib


model = joblib.load("model.pkl")

st.title("Laptop Price Prediction")

# -------- Laptop Information --------
st.header("💻 Laptop Information")

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

# -------- Hardware Specifications --------
st.header("⚙️ Hardware Specifications")

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

Weight = st.number_input(
    "Weight (kg)",
    min_value=0.69,
    max_value=5.0,
    value=2.0,
    step=0.01
)

# -------- Display Specifications --------
st.header("🖥️ Display Specifications")

Inches = st.number_input(
    "Screen Size (Inches)",
    min_value=10.0,
    max_value=19.0,
    value=15.6,
    step=0.1
)

Width = st.number_input(
    "Resolution Width (px)",
    min_value=1300,
    max_value=3840,
    value=1920,
    step=10
)

Height = st.number_input(
    "Resolution Height (px)",
    min_value=760,
    max_value=2160,
    value=1080,
    step=10
)

Touchscreen = st.radio("Touchscreen", ["Yes", "No"])
Touchscreen = 1 if Touchscreen == "Yes" else 0

Ips = st.radio("IPS Display", ["Yes", "No"])
Ips = 1 if Ips == "Yes" else 0

# -------- Storage Specifications --------
st.header("💾 Storage Specifications")

Ssd = st.number_input(
    "SSD (GB)",
    min_value=0,
    max_value=2000,
    value=256,
    step=10
)

Hdd = st.number_input(
    "HDD (GB)",
    min_value=0,
    max_value=4000,
    value=0,
    step=10
)

Flash_Storage = st.number_input(
    "Flash Storage (GB)",
    min_value=0,
    max_value=512,
    value=0,
    step=10
)

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

#-------Prediction----------
if st.button("Predict Price"):

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
        st.success(f"€{prediction[0]:,.2f}")
st.markdown("---")
st.caption("Built using Streamlit and K-Nearest Neighbors Regression")
