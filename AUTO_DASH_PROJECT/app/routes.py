import os
import pandas as pd
from flask import request, redirect, render_template, flash, url_for
from werkzeug.utils import secure_filename
import plotly.express as px
from app import app

# Create the upload folder if it doesn't exist
UPLOAD_FOLDER = 'app/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return redirect(url_for('upload_file'))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    graph_html_blocks = []  # Holds all the generated charts

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Read the Excel file
            df = pd.read_excel(file_path)

            # Detect columns
            numeric_cols = df.select_dtypes(include='number').columns.tolist()
            categorical_cols = df.select_dtypes(exclude='number').columns.tolist()

            # Histogram for each numeric column
            for col in numeric_cols:
                fig = px.histogram(df, x=col, title=f'Distribution of {col}')
                graph_html_blocks.append(fig.to_html(full_html=False))

            # Bar chart for each (categorical x numeric) combo
            for cat_col in categorical_cols:
                if df[cat_col].nunique() <= 20:  # Avoid cluttered charts
                    for num_col in numeric_cols:
                        avg_data = df.groupby(cat_col)[num_col].mean().reset_index()
                        fig = px.bar(avg_data, x=cat_col, y=num_col, title=f'Average {num_col} by {cat_col}')
                        graph_html_blocks.append(fig.to_html(full_html=False))

            # Scatter plots for numeric column pairs
            if len(numeric_cols) >= 2:
                for i in range(len(numeric_cols)):
                    for j in range(i + 1, len(numeric_cols)):
                        fig = px.scatter(df, x=numeric_cols[i], y=numeric_cols[j], title=f'{numeric_cols[j]} vs {numeric_cols[i]}')
                        graph_html_blocks.append(fig.to_html(full_html=False))

            # Pie chart for categorical columns with few unique values
            for cat_col in categorical_cols:
                if df[cat_col].nunique() <= 10:
                    fig = px.pie(df, names=cat_col, title=f'Distribution of {cat_col}')
                    graph_html_blocks.append(fig.to_html(full_html=False))

            # Render the dashboard
            return render_template(
                'dashboard.html',
                table=df.to_html(classes='data', header="true"),
                graph_html_blocks=graph_html_blocks
            )
 
    return render_template('upload.html')

# Info route
@app.route('/info', methods=['GET'])
def info_page():
    return render_template('info.html')

@app.route('/about', methods=['GET'])
def about():
    return redirect(url_for('info_page'))

@app.route('/contact', methods=['GET'])
def contact():
    return redirect(url_for('info_page'))

@app.route('/explore', methods=['GET'])
def explore():
    return redirect(url_for('info_page'))