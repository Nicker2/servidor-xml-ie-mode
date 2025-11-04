import os
from flask import Flask, render_template, send_from_directory
from datetime import datetime

app = Flask(__name__)

XML_FOLDER = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    filenames = [f for f in os.listdir(XML_FOLDER) if f.endswith('.xml')]
    
    file_details = []
    for f in filenames:
        full_path = os.path.join(XML_FOLDER, f)
        raw_time = os.path.getctime(full_path)
        formatted_time = datetime.fromtimestamp(raw_time).strftime('%d/%m/%Y %H:%M:%S')
        
        file_details.append({
            'name': f,
            'raw_time': raw_time,
            'mod_time': formatted_time
        })

    sorted_file_details = sorted(
        file_details,
        key=lambda item: item['raw_time'],
        reverse=True
    )
    
    return render_template('index.html', files_list=sorted_file_details)

# --- FUNÇÃO CORRIGIDA ABAIXO ---

@app.route('/<filename>')
def serve_xml(filename):
    # Permite que o servidor entregue arquivos .xml E .xsl
    if filename.endswith('.xml') or filename.endswith('.xsl'):
        return send_from_directory(XML_FOLDER, filename)
    
    # Se não for .xml ou .xsl, bloqueia
    return "Arquivo não encontrado ou tipo não permitido.", 404

# --- FIM DA CORREÇÃO ---

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == '__main__':
    app.run(port=8000, debug=True)