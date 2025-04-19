import streamlit as st
import numpy as np
from PIL import Image
import random

# Class labels for traffic signs
CLASS_NAMES = [
    "Speed Limit 20", "Speed Limit 30", "Speed Limit 50", "Speed Limit 60", "Speed Limit 70",
    "Speed Limit 80", "End of Speed Limit 80", "Speed Limit 100", "Speed Limit 120",
    "No Passing", "No Passing for Vehicles over 3.5 tons", "Right-of-way at Intersection",
    "Priority Road", "Yield", "Stop", "No Vehicles", "Vehicles Over 3.5 Tons Prohibited",
    "No Entry", "General Caution", "Dangerous Curve Left", "Dangerous Curve Right",
    "Double Curve", "Bumpy Road", "Slippery Road", "Road Narrows on the Right",
    "Road Work", "Traffic Signals", "Pedestrians", "Children Crossing", "Bicycles Crossing",
    "Beware of Ice/Snow", "Wild Animals Crossing", "End of All Restrictions", "Turn Right Ahead",
    "Turn Left Ahead", "Ahead Only", "Go Straight or Right", "Go Straight or Left",
    "Keep Right", "Keep Left", "Roundabout Mandatory", "End of No Passing",
    "End of No Passing by Vehicles Over 3.5 Tons"
]

# Simulated prediction (random)
def simulate_prediction():
    index = random.randint(0, len(CLASS_NAMES) - 1)
    confidence = round(random.uniform(0.7, 1.0), 2)
    return CLASS_NAMES[index], confidence

# Preprocessing stub
def process_image(img: Image.Image) -> np.ndarray:
    img = img.resize((32, 32))
    array = np.asarray(img) / 255.0
    return np.expand_dims(array, axis=0)

st.set_page_config("Traffic Sign Recognition", page_icon="🚗")
st.title("🚗 Traffic Sign Classifier (Demo)")
st.caption("Developed by Chandra")

image_file = st.file_uploader("Upload a traffic sign image", type=["jpg", "jpeg", "png"])

if image_file:
    uploaded_image = Image.open(image_file)
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    processed = process_image(uploaded_image)
    prediction_label, confidence = simulate_prediction()

    st.markdown("### 🧠 Simulated Prediction Result")
    st.success(f"**Traffic Sign:** {prediction_label}")
    st.info(f"**Confidence (simulated):** {confidence * 100:.2f}%")
