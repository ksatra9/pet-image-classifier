# 🐶🐱 Pet Image Classifier using CNN

##  Overview
This project is a deep learning-based image classification system that classifies images as **Cat or Dog** using a Convolutional Neural Network (CNN).  
It includes an interactive web application built with Streamlit for real-time predictions.

---

##  Features
- Upload an image and get instant prediction  
- Displays prediction confidence  
- Clean and interactive UI using Streamlit  
- Uses trained CNN model  

---

##  Tech Stack
- Python  
- TensorFlow / Keras  
- NumPy  
- Streamlit  
- Pillow (PIL)  

---

##  Model Details
- Input size: 256 × 256 × 3  
- Model: CNN (Convolutional Neural Network)  
- Binary classification: Cat vs Dog  

---

##  Project Structure

pet-image-classifier/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── sample_images/

---

##  How to Run

### 1. Clone the repository
git clone https://github.com/ksatra9/pet-image-classifier.git

cd pet-image-classifier

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the app
streamlit run app.py


---

##  Model File
The trained model is stored externally due to GitHub size limits.

It will be automatically downloaded when running the app.

---

##  Demo
image.png

image-1.png

image-2.png
---

##  Future Improvements
- Add more classes (multi-class classification)  
- Improve accuracy using transfer learning  
- Deploy fully online with public access  

---

##  Author
Kavya Satra