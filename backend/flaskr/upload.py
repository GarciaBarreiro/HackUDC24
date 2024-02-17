from flask import Blueprint, request, redirect, url_for, flash, current_app, session
from werkzeug.utils import secure_filename
from flaskr.auth import login_required
import os

bp = Blueprint('upload', __name__, url_prefix='/upload')

@bp.route('/', methods=['POST'])
@login_required
def upload_file():
    #Check if the post request has the file part
    if 'file' not in request.files:
        flash('No file')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No file selected')
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['uploads'], secure_filename(filename)))
        process_file(os.path.join(current_app.config['uploads'], secure_filename(filename)))
        return redirect(url_for('index'))

import pandas as pd 
from .db import get_db

def process_file(filepath):
    # Read the CSV file
    df = pd.read_csv(filepath)
    # Here you can perform any necessary preprocessing on df
    # For example, renaming columns or converting data types
    user_id = session.get('user_id')

    # Insert data into the database
    db = get_db()
    for _, row in df.iterrows():
        date_split = row['Fecha'].split('/')
        db.execute('INSERT INTO consumption (cups, year, month, date, hour, cons, obt_met, user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                   (row['CUPS'], date_split[0], date_split[1], date_split[2], row['Hora'], row['Consumo_KWh'], row['Metodo_obtencion'], user_id))
    db.commit()
