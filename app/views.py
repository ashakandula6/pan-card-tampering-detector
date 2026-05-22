# Important imports
from app import app
from flask import request, render_template, jsonify
import os
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image
import base64
from io import BytesIO

# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'
app.config['EXISTNG_FILE'] = 'app/static/original'
app.config['GENERATED_FILE'] = 'app/static/generated'

# ====================== NEW JSON API ENDPOINT ======================
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if not data or "image" not in data:
            return jsonify({"error": "No image provided. Send base64 image."}), 400

        # Decode base64 image
        img_data = base64.b64decode(data["image"])
        uploaded_image = Image.open(BytesIO(img_data)).resize((250, 160))
        
        # Save temporarily for processing
        temp_path = os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'temp_predict.jpg')
        uploaded_image.save(temp_path)

        # Load original image
        original_path = os.path.join(app.config['EXISTNG_FILE'], 'image.jpg')
        original_image = Image.open(original_path).resize((250, 160))
        original_image.save(original_path)  # Ensure same size

        # Read images for comparison
        original_cv = cv2.imread(original_path)
        uploaded_cv = cv2.imread(temp_path)

        original_gray = cv2.cvtColor(original_cv, cv2.COLOR_BGR2GRAY)
        uploaded_gray = cv2.cvtColor(uploaded_cv, cv2.COLOR_BGR2GRAY)

        # Structural Similarity
        (score, diff) = structural_similarity(original_gray, uploaded_gray, full=True)
        diff = (diff * 255).astype("uint8")

        # Threshold and contours (for visualization if needed)
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # Optional: Draw contours
        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(original_cv, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(uploaded_cv, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Save generated images (optional for API)
        cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_original.jpg'), original_cv)
        cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_uploaded.jpg'), uploaded_cv)
        cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_diff.jpg'), diff)
        cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_thresh.jpg'), thresh)

        is_tampered = score < 0.95  # You can adjust this threshold

        return jsonify({
            "tampered": is_tampered,
            "similarity_score": round(score * 100, 2),
            "confidence": round(score, 4),
            "message": "Document is tampered" if is_tampered else "Document is genuine"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ====================== EXISTING WEB UI ROUTE ======================
@app.route("/", methods=["GET", "POST"])
def index():
    # GET request - Show home page
    if request.method == "GET":
        return render_template("index.html")

    # POST request - Web form upload
    if request.method == "POST":
        file_upload = request.files['file_upload']
        filename = file_upload.filename

        # Resize and save uploaded image
        uploaded_image = Image.open(file_upload).resize((250, 160))
        uploaded_image.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))

        # Resize original image to match
        original_image = Image.open(os.path.join(app.config['EXISTNG_FILE'], 'image.jpg')).resize((250, 160))
        original_image.save(os.path.join(app.config['EXISTNG_FILE'], 'image.jpg'))

        # Read images
        original_image = cv2.imread(os.path.join(app.config['EXISTNG_FILE'], 'image.jpg'))
        uploaded_image = cv2.imread(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))

        original_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        uploaded_gray = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)

        (score, diff) = structural_similarity(original_gray, uploaded_gray, full=True)
        diff = (diff * 255).astype("uint8")

        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(uploaded_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_original.jpg'), original_image)
        cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_uploaded.jpg'), uploaded_image)
        cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_diff.jpg'), diff)
        cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_thresh.jpg'), thresh)

        return render_template('index.html', pred=str(round(score * 100, 2)) + '%' + ' correct')


# Main function (for local testing)
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)