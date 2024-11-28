function askQuestion() {
    const question = document.getElementById('question').value;

    if (!question) {
        alert('Por favor, insira uma pergunta!');
        return;
    }

    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: question })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('answer').innerText = 'Resposta: ' + data.answer;
    })
    .catch(error => {
        document.getElementById('answer').innerText = 'Erro ao processar a pergunta.';
    });
}
