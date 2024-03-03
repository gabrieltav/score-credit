import os
import zipfile
import subprocess
from werkzeug.utils import secure_filename
from flask import jsonify, flash, request
from utils.constants import ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS;

def upload(folder):
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
            file.save(os.path.join(folder, filename))
            return filename, 200
    return jsonify({'message': 'Invalid method.'}), 405

def restart_application():
    # Modifique o caminho para o arquivo .wsgi conforme necessário
    wsgi_file = './tmp/uploads/predict.pkl'
    
    # Use o comando touch no arquivo .wsgi para forçar o Apache a recarregar a aplicação
    subprocess.run(["touch", wsgi_file])

    return jsonify({'message': 'Application restarted successfully!'}), 200

def unzip():
    # Caminho para o arquivo zip
    path = './tmp/uploads/predict.zip'

    # Verificando se o arquivo zip existe
    if not os.path.exists(path):
        return jsonify({'error': 'Arquivo zip não encontrado.'}), 404

    # Diretório onde deseja extrair os arquivos
    destination_directory = './tmp/uploads'

    # Garantindo que o diretório de destino exista
    os.makedirs(destination_directory, exist_ok=True)

    try:
        # Descompactando o arquivo zip
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(destination_directory)
    except zipfile.BadZipFile:
        return jsonify({'error': 'O arquivo zip está corrompido.'}), 400

    # Excluindo o arquivo zip após a descompactação
    try:
        os.remove(path)
    except OSError:
        return jsonify({'error': 'Não foi possível excluir o arquivo zip.'}), 500

    return jsonify({'message': 'Files unzipped successfully!'}), 200
