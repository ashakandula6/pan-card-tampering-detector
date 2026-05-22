````markdown
# 🛡️ PAN Card Tampering Detection Web App

A production-ready Flask web application that detects tampering in uploaded PAN Card images using Structural Similarity Index (SSIM) and OpenCV.

![Project Architecture](architecture.png)

## 🚀 Features

- Upload any PAN card image (PNG, JPG, JPEG)
- Detects if the PAN card is **original** or **tampered**
- Clean REST API endpoint (`/predict`) for integration
- Dockerized for consistent deployment
- Automated CI/CD pipeline with GitHub Actions
- Deployed on AWS EC2

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
├── .github/workflows/      # CI/CD Pipeline
├── Dockerfile
├── requirements.txt
├── app.py
└── README.md
```

---

## ⚙️ How to Run Locally

### Using Docker (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/ashakandula6/pan-card-tampering-detector.git

# 2. Move into project folder
cd pan-card-tampering-detector

# 3. Build Docker image
docker build -t pan-card-api .

# 4. Run Docker container
docker run -p 5000:5000 pan-card-api
```

Open in browser:

```bash
http://localhost:5000
```

---

## 🔌 API Endpoint

### POST `/predict`

### Request

```json
{
  "image": "base64_encoded_image_string"
}
```

### Response

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

- **Render (Current)**: https://pan-card-tampering-detector-1.onrender.com/
- **AWS EC2 (Production Deployment)**: `http://your-ec2-ip:5000` *(Coming soon)*

---

## 🧠 Tech Stack

- **Backend**: Flask (Python)
- **Computer Vision**: OpenCV + scikit-image (SSIM)
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Cloud**: AWS (EC2 + ECR)
- **Frontend**: HTML/CSS (Materialize CSS)

---

## 🚀 Deployment

- **CI/CD Pipeline**: Fully automated (GitHub → ECR → EC2)
- **Status**: ✅ Dockerized + CI/CD Ready

---

## 🔮 Future Enhancements

- Integrate Deep Learning (CNN) model
- Add user authentication
- HTTPS using API Gateway
- Better UI/UX and mobile responsiveness

---

## 🙋‍♀️ Author

**Asha Kandula**  

GitHub: https://github.com/ashakandula6

---