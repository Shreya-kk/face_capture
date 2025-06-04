from flask import Flask, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)  # ✅ Corrected

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/upload_frame', methods=['POST'])
def upload_frame():
    file = request.files['frame']
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)
    return 'Frame received and saved.'

if __name__ == '__main__':  # ✅ Corrected
    app.run(debug=True)
