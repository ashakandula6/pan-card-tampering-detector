Here's a **README.md** for your PAN Card Tampering Detection Flask app:

# 🛡️ PAN Card Tampering Detection Web App

This is a Flask-based web application that detects tampering in uploaded PAN Card images using machine learning.

## 🚀 Features

- Upload any PAN card image (PNG, JPG, JPEG)
- Detects if the PAN card is **original** or **tampered**
- Simple and clean frontend UI
- Built with Python, Flask, and Materialize CSS

---

## 📁 Project Structure

```

PanCApp/
│
├── app/
│   ├── **init**.py
│   ├── views.py
│   └── model.pkl  # Your ML model
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   └── index.html
│
├── requirements.txt
├── .gitignore
└── app.py

````

---

## ⚙️ Installation & Setup

### 1. Clone the Repo
```bash
git clone https://github.com/ashakandula6/pan-card-tampering-detector.git
cd pan-card-tampering-detector
````

### 2. Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## 🧠 Tech Stack

* Python 
* Flask 
* HTML/CSS (Materialize CSS)
* Machine Learning (Scikit-Learn / TensorFlow)
* Git & GitHub

---

## 🌐 Deploy for Free

You can deploy this app on:

* [Render](https://render.com/) — simple Flask deployment
* [Railway](https://railway.app/)
* [Vercel (via Serverless)](https://vercel.com/)
* [Heroku (needs workarounds now)](https://www.heroku.com/)

---

## 🙋‍♀️ Author

**Asha Kandula**
🔗 GitHub: [@ashakandula6](https://github.com/ashakandula6)

---

![image](https://github.com/user-attachments/assets/cb5374cb-f0a1-42d3-8c4c-5868a75d0321)
Link for website: https://pan-card-tampering-detector-1.onrender.com/
