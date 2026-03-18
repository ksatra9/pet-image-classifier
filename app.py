import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import gdown
import os

# Download model if not exists
@st.cache_resource
def load_model():
    if not os.path.exists("model.h5"):
        url = "https://drive.google.com/uc?id=1eNbYsNbUCG_TiYMQ_T2zON-crFSO592z"
        gdown.download(url, "model.h5", quiet=False)
    return tf.keras.models.load_model("model.h5")

model = load_model()

# Preprocess image (MATCH TRAINING SIZE)
def preprocess_image(image):
    img = image.resize((256, 256))   # ✅ FIXED SIZE
    img = np.array(img) / 255.0      # normalize
    img = np.expand_dims(img, axis=0)
    return img

# UI
st.set_page_config(page_title="Pet Classifier", layout="centered")

st.title("🐶🐱 Pet Image Classifier")
st.write("Upload an image to classify it as Cat or Dog")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file is None:
    st.info("👆 Upload an image to get prediction")
else:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Preprocess
    img = preprocess_image(image)

    # Prediction
    prediction = model.predict(img)[0][0]

    # Output
    if prediction > 0.5:
        label = "Dog 🐶"
        confidence = prediction
    else:
        label = "Cat 🐱"
        confidence = 1 - prediction

    st.success(f"Prediction: {label}")
    st.write(f"Confidence: {confidence * 100:.2f}%")

    # Progress bar (looks good for demo)
    st.progress(float(confidence))