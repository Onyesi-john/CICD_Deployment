import os
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Define folders
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return redirect(request.url)

    file = request.files["file"]
    if file.filename == "":
        return redirect(request.url)

    if file:
        # Save uploaded image
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        return render_template("result.html", image_path=file_path)

@app.route("/webcam")
def webcam():
    return render_template("webcam.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
