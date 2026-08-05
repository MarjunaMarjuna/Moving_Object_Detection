# Moving_Object_Detection

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📖 Overview

This project demonstrates the fundamentals of **Computer Vision** using **Python** and **OpenCV**. It includes basic image processing operations such as image resizing, Gaussian smoothing, thresholding, video frame capture, and a real-time **Moving Object Detection** system using a webcam.

The moving object detection module identifies motion by comparing the current video frame with an initial background frame and highlights detected objects using bounding boxes.

---

## ✨ Features

* 📷 Capture live video from a webcam
* 🎯 Detect moving objects in real time
* 🖼️ Resize images using `imutils`
* 🌫️ Apply Gaussian Blur for noise reduction
* ⚫ Convert images to grayscale
* ⚪ Perform binary thresholding
* 📦 Detect contours of moving objects
* 🟩 Draw bounding boxes around detected motion
* ❌ Exit the application by pressing **Q**

---

## 🛠️ Technologies Used

* Python 3.x
* OpenCV (`cv2`)
* NumPy
* imutils

---

## 📂 Project Structure

Moving_Object_Detection
│
├── cameraTest.py              # Real-time moving object detection
│
├── frame/
│   └── frm.py                 # Webcam frame capture example
│
├── Resize/
│   ├── initialimage.jpg
│   ├── resizedImage2.jpg
│   └── resze.py               # Image resizing
│
├── Smoothen/
│   ├── initialimage.jpg
│   └── smooth.py              # Gaussian Blur example
│
└── threshold/
    ├── initialimage.jpg
    └── thres.py               # Image thresholding

---

## ⚙️ Installation

Clone the repository:

bash:
git clone https://github.com/MarjunaMarjuna/Moving_Object_Detection.git

Move into the project directory:

bash
cd Moving_Object_Detection

Install the required packages:


bash
pip install opencv-python imutils numpy

---

## ▶️ Running the Project

### Moving Object Detection

bash
python cameraTest.py

### Webcam Frame Capture

bash
python frame/frm.py

### Image Resize

bash
python Resize/resze.py

### Gaussian Blur

bash
python Smoothen/smooth.py


### Image Thresholding

bash
python threshold/thres.py


---

## 🔄 Moving Object Detection Workflow

Webcam
   │
   ▼
Capture Video Frames
   │
   ▼
Resize Frame
   │
   ▼
Convert to Grayscale
   │
   ▼
Gaussian Blur
   │
   ▼
Store Initial Background Frame
   │
   ▼
Calculate Frame Difference
   │
   ▼
Binary Threshold
   │
   ▼
Dilation
   │
   ▼
Contour Detection
   │
   ▼
Bounding Box
   │
   ▼
Display Detected Motion

---

## 🧠 How It Works

The application continuously captures frames from the webcam.

1. The first frame is stored as the reference background.
2. Each new frame is converted to grayscale.
3. Gaussian Blur is applied to reduce noise.
4. The current frame is compared with the background frame.
5. The absolute difference is thresholded to isolate moving regions.
6. Dilation fills small gaps in detected objects.
7. Contours are extracted from the threshold image.
8. Objects larger than a predefined area are considered moving objects.
9. A green bounding box is drawn around detected objects.

---

## 📌 Image Processing Modules

### 📏 Image Resize

Demonstrates resizing an image using the **imutils** library while maintaining the aspect ratio.

### 🌫️ Gaussian Smoothing

Applies Gaussian Blur with different kernel sizes to reduce image noise before further processing.

### ⚫ Thresholding

Converts grayscale images into binary images based on a threshold value.

### 📹 Webcam Frame Capture

Shows how to capture and display live frames using OpenCV.

---

## 🚀 Applications

* Smart Surveillance Systems
* Motion Detection
* Security Monitoring
* Home Automation
* Traffic Monitoring
* Human Activity Detection
* Industrial Monitoring
* Computer Vision Learning

---

## 📈 Future Improvements

* YOLO-based object detection
* Object tracking using DeepSORT
* Multiple object classification
* Save detected motion as video
* Motion alerts via email
* Streamlit or Flask web interface
* Performance optimization
* GPU acceleration

---

## 📚 Learning Outcomes

This project helped in understanding:

* OpenCV fundamentals
* Image preprocessing
* Gaussian filtering
* Thresholding techniques
* Contour detection
* Motion detection algorithms
* Real-time video processing
* Webcam integration
* Computer Vision workflows

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to your branch
5. Submit a Pull Request

---

## 👩‍💻 Author

**Marzuna M A**

Computer Science Engineering Student

AI • Machine Learning • Computer Vision Enthusiast

GitHub: https://github.com/MarjunaMarjuna

---

## 📄 License

This project is available under the **MIT License**.

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
