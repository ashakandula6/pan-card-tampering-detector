# 🛡️ PAN Card Tampering Detection Web App

A production-ready Flask web application that detects tampering in uploaded PAN Card images using Structural Similarity Index (SSIM) and OpenCV.

---

## 🚀 Features

- Upload PAN card images (PNG, JPG, JPEG)
- Detect whether the document is **original** or **tampered**
- REST API endpoint (`/predict`) for integration
- Dockerized application for easy deployment
- Automated CI/CD pipeline using GitHub Actions
- AWS EC2 deployment ready

---

## 📁 Project Structure

```bash
pan-card-tampering-detector/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── views.py
│   └── templates/
├── app/static/             # uploads, original, generated images
├── .github/workflows/      # GitHub Actions CI/CD
├── Dockerfile
├── requirements.txt
├── app.py
└── README.md
```

---

## ⚙️ How to Run Locally

### 🐳 Using Docker (Recommended)

```bash
# Clone repository
git clone https://github.com/ashakandula6/pan-card-tampering-detector.git

# Move into project folder
cd pan-card-tampering-detector

# Build Docker image
docker build -t pan-card-api .

# Run Docker container
docker run -p 5000:5000 pan-card-api
```

Open in browser:

```bash
http://localhost:5000
```

---

## 🔌 API Endpoint

### POST `/predict`

### Request Body

```json
{
  "image": "base64_encoded_image_string"
}
```

### Sample Response

```json
{
  "tampered": false,
  "similarity_score": 97.85,
  "confidence": 0.9785,
  "message": "Document is genuine"
}
```

---

## 🌐 Live Deployments

### Render Deployment
https://pan-card-tampering-detector-1.onrender.com/

### AWS EC2 Deployment
`http://your-ec2-ip:5000` *(Coming Soon)*

---

## 🧠 Tech Stack

| Technology | Usage |
|---|---|
| Flask | Backend Framework |
| OpenCV | Image Processing |
| scikit-image | SSIM Comparison |
| Docker | Containerization |
| GitHub Actions | CI/CD |
| AWS EC2 + ECR | Cloud Deployment |
| HTML/CSS | Frontend UI |

---

## 🚀 Deployment

- CI/CD Pipeline: GitHub → ECR → EC2
- Dockerized and production-ready
- Automated deployment workflow

---

## 🔮 Future Enhancements

- Deep Learning based tampering detection
- User authentication system
- HTTPS support using API Gateway
- Improved mobile responsiveness
- Detection analytics dashboard

---

## 🙋‍♀️ Author

### Asha Kandula

GitHub: https://github.com/ashakandula6

---
<img width="774" height="544" alt="WhatsApp Image 2026-05-20 at 20 14 12" src="https://github.com/user-attachments/assets/c2f98166-88a0-45cd-b660-1c28c1dbfafc" />
