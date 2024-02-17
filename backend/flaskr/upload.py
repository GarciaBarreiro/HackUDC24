from flask import Blueprint, request, jsonify, current_app, session
from werkzeug.utils import secure_filename
from flaskr.auth import login_required
import os
import pandas as pd
from .db import get_db

bp = Blueprint('upload', __name__, url_prefix='/upload')

@bp.route('/', methods=['POST'])
def upload_file():
    f = request.files.get('file')
    data_filename = secure_filename(f.filename)
    f.save(os.path.join(current_app.config['UPLOAD_FOLDER'],
                            data_filename))
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.seek(0)
        file.save(save_path)
        try:
            process_file(save_path)
            return jsonify({'message': 'File successfully uploaded and processed.'}), 200
        except Exception as e:
            return jsonify({'error': 'Failed to process file', 'details': str(e)}), 500

def process_file(filepath):
    # Read the CSV file
    df = pd.read_csv(filepath, sep=';')
    # Assume necessary preprocessing on df here
    # user_id = session.get('user_id')
    user_id = 0

    # Insert data into the database
    db = get_db()
    try:
        for _, row in df.iterrows():
            # Assuming 'Fecha' and other columns exist and splitting date appropriately
            date_split = row['Fecha'].split('/')
            print(date_split)
            db.execute('INSERT INTO consumption (cups, year, month, date, hour, cons, obt_met, user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                       (row['CUPS'], date_split[2], date_split[1], date_split[0], row['Hora'], row['Consumo_KWh'], row['Metodo_obtencion'], user_id))
            print("here 5")
        db.commit()
    except Exception as e:
        print(e)
        raise e  # Rethrow the exception to handle it in the calling function