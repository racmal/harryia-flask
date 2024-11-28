from transformers import pipeline

# Carregar o modelo de QA do Hugging Face
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Função para gerar respostas mais coerentes
def get_ia_response(question):
    # Contexto com informações sobre a IA (HarryIA)
    context = """
    Olá! Eu sou a HarryIA, uma IA criada para responder suas perguntas de forma divertida e interativa.
    Meu nome é HarryIA, e eu posso te ajudar com diversas informações, curiosidades e muito mais.
    Se você quiser saber mais sobre mim, é só perguntar! :)
    Eu também posso responder perguntas sobre tecnologia, ciência, história e outros assuntos!
    """

    # Caso a pergunta seja sobre o nome da IA
    if "nome" in question.lower() or "qual é o seu nome" in question.lower():
        return "Oi! Eu sou a HarryIA, uma assistente virtual bem inteligente e divertida! 😄"

    # Caso a pergunta seja sobre algo específico
    result = qa_pipeline({
        'context': context,
        'question': question
    })

    # Retorna a resposta da IA
    return result['answer'] if result['answer'] else "Desculpe, não entendi sua pergunta."
