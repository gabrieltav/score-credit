import os
from flask import Flask
from utils.constants import UPLOAD_FOLDER, PERMITTED_SIZE
from views.new_clients_view import new_clients
from views.upload_view import upload, unzip

app = Flask(__name__)
app.config["DEBUG"] = True;
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = PERMITTED_SIZE
app.config["DEBUG"] = os.environ.get("DEBUG", "").lower() == "true"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/upload-model', methods=['POST'])
def uploadModel():
    return upload(app.config['UPLOAD_FOLDER'])

@app.route('/unzip-model', methods=['POST'])
def unzipModel():
    return unzip()

@app.route('/predict', methods=['POST'])
def predict():
    return new_clients(app.config['UPLOAD_FOLDER'])

if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"])