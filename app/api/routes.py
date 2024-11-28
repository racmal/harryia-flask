from flask import Blueprint, request, jsonify
from app.models.model import get_ia_response

# Criação do Blueprint para a API
api = Blueprint('api', __name__)

# Rota que recebe perguntas via POST
@api.route('/ask', methods=['POST'])
def ask():
    # Recebe os dados da requisição JSON
    data = request.get_json()
    question = data.get('question')  # Extrai a pergunta do JSON
    context = data.get('context', None)  # Tenta extrair o contexto do JSON (se existir)

    # Se a pergunta não for fornecida, retorna um erro
    if not question:
        return jsonify({'error': 'Question is required'}), 400

    # Chama a função que interage com a IA para obter a resposta
    # Passa o contexto fornecido (se houver) ou o contexto padrão
    answer = get_ia_response(question, context)

    # Retorna a resposta da IA em formato JSON
    return jsonify({'answer': answer})
