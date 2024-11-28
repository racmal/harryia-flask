 import sqlite3

# Função para criar e conectar ao banco de dados
def create_connection():
    conn = sqlite3.connect('data.db')  # Banco de dados local
    return conn

# Função para criar a tabela se ela não existir
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )
    """)
    conn.commit()
    conn.close()

# Função para adicionar uma pergunta e resposta
def add_question_answer(question, answer):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO questions (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()

# Função para recuperar todas as perguntas e respostas
def get_all_questions():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    rows = cursor.fetchall()
    conn.close()
    return rows

