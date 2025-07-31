import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import zipfile
import os

# Debug information (only show in development)
if st.checkbox("🔧 Show Debug Info", value=False):
    st.write("**Current working directory:**", os.getcwd())
    st.write("**Files in current directory:**", os.listdir("."))
    if os.path.exists("models"):
        st.write("**Files in models directory:**", os.listdir("models"))
    if os.path.exists("../models"):
        st.write("**Files in ../models directory:**", os.listdir("../models"))

# Page config
st.set_page_config(page_title="Low Light Enhancer", layout="centered", page_icon="📷")

# Title
st.title("📷 Low Light Image Enhancer")
st.markdown("Upload low-light images (individually or as a `.zip`) to enhance them using the Zero-DCE model.")

# Load model
@st.cache_resource
def load_model():
    # Try different possible paths for the model
    possible_paths = [
        "../models/LOW_LIGHT_MODEL.h5",  # Local development (from src/)
        "models/LOW_LIGHT_MODEL.h5",     # Streamlit Cloud (from repo root)
        "./models/LOW_LIGHT_MODEL.h5",   # Alternative path
        "LOW_LIGHT_MODEL.h5"             # Same directory fallback
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            try:
                return tf.keras.models.load_model(path, compile=False)
            except Exception as e:
                st.warning(f"Failed to load model from {path}: {e}")
                continue
    
    return None

model = load_model()
if model is None:
    st.error("""
    ❌ **Model file not found!** 
    
    Please ensure 'LOW_LIGHT_MODEL.h5' is available in one of these locations:
    - `models/LOW_LIGHT_MODEL.h5` (recommended)
    - `../models/LOW_LIGHT_MODEL.h5` 
    - `LOW_LIGHT_MODEL.h5`
    
    **For Streamlit Cloud deployment:** Make sure the model file is committed to your GitHub repository in the `models/` folder.
    """)
    st.stop()

# Preprocess image
def preprocess_image(img: Image.Image) -> np.ndarray:
    img = img.convert("RGB").resize((512, 512))
    arr = np.asarray(img).astype(np.float32) / 255.0
    return np.expand_dims(arr, axis=0)

# Postprocess and return enhanced image
def enhance_image(model, image: Image.Image, intensity: float = 3.0) -> Image.Image:
    input_tensor = preprocess_image(image)
    curve = model.predict(input_tensor)
    curve = curve * intensity  # Boost enhancement strength

    x = tf.convert_to_tensor(input_tensor)
    for i in range(8):
        a = curve[..., i*3:(i+1)*3]
        x = x + a * (tf.square(x) - x)

    enhanced = x[0].numpy()
    enhanced = np.clip(enhanced * 255.0, 0, 255).astype(np.uint8)
    return Image.fromarray(enhanced)

# Enhancement intensity slider
intensity = st.slider("🔆 Enhancement Intensity", min_value=1.0, max_value=10.0, value=3.0, step=0.5)

# Upload
uploaded_file = st.file_uploader("📤 Upload image or .zip", type=['jpg', 'jpeg', 'png', 'zip'])

# Process uploaded image
if uploaded_file is not None:
    file_list = []

    if uploaded_file.name.endswith(".zip"):
        with zipfile.ZipFile(uploaded_file, "r") as zip_ref:
            zip_ref.extractall("temp_images")
            file_list = [os.path.join("temp_images", f) for f in zip_ref.namelist() if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    else:
        file_list = [uploaded_file]

    for file in file_list:
        if isinstance(file, str):
            img = Image.open(file)
        else:
            img = Image.open(file)

        st.image(img, caption="📷 Original", use_container_width=True)
        with st.spinner("✨ Enhancing..."):
            enhanced_img = enhance_image(model, img, intensity=intensity)
        st.image(enhanced_img, caption="⚡ Enhanced", use_container_width=True)

    if uploaded_file.name.endswith(".zip"):
        import shutil
        shutil.rmtree("temp_images")
