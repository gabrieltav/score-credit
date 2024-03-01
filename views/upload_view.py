import os
from werkzeug.utils import secure_filename
from flask import jsonify, flash, request
from utils.constants import ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS;

def upload(upload_folder):
    if request.method == 'POST':
        
        if 'file' not in request.files:
            flash('There is no file part')
            return jsonify({'message': 'No files sent.'}), 400
        file = request.files['file']
        
        if file.filename == '':
            flash('No files selected')
            return jsonify({'message': 'No files selected.'}), 400
        
        if file.filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
            return jsonify({'message': 'File type not allowed. Only CSV files are accepted.'}), 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_folder, filename))
            return filename, 200
    return jsonify({'message': 'Invalid method.'}), 405