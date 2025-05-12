from flask import Flask
from flask import request, jsonify
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('public', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('public', filename)

@app.route('/ask', methods=['POST'])
def mensagem():
    data = request.get_json()
    mensagem = data.get('pergunta', '')
    resposta = f"Você disse: {mensagem}"
    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)