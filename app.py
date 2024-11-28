from flask import Flask, render_template
from app.api.routes import api

app = Flask(__name__)

# Registrando o Blueprint da API
app.register_blueprint(api, url_prefix='/api')

# Rota para a página inicial (formulário de perguntas)
@app.route('/')
def home():
    return render_template('index.html')  # Renderiza a página de perguntas

if __name__ == '__main__':
    app.run(debug=True)
