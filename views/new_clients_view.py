import pandas as pd
import joblib
import os
from flask import jsonify
from views.upload_view import upload
from model.client import convert_client_to_dictionary

modelo = None

def load_model():
    global modelo
    try:
        modelo = joblib.load('./tmp/uploads/predict.pkl')
    except FileNotFoundError:
        print('File predict.pkl not found. Using default template.')

load_model()

def new_clients(folder):
    if modelo is None:
        return jsonify({'error': 'Model not found. Load the model before using this route'}), 500

    upload_result = upload(folder)
    filename, status_code = upload_result
    
    if status_code != 200:
        return upload_result
    
    new_clients = pd.read_csv(f"{folder}/{filename}")
    # print(new_clients.dtypes)

    forecasts = []

    results = []

    id_cliente = 1

    for client in new_clients.itertuples():

        data = convert_client_to_dictionary(client)

        forecast = modelo.predict([list(data.values())])

        forecasts.append(forecast[0])

        client_result = {
            "id": id_cliente,
            "score_credit": forecast[0]
        }

        results.append(client_result)

        id_cliente += 1
    
    # Excluindo o arquivo zip novos_clientes
    try:
        os.remove('./tmp/uploads/novos_clientes.csv')
    except OSError:
        return jsonify({'error': 'Não foi possível excluir o arquivo zip.'}), 500

    return jsonify({"new_clients": results})