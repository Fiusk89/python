from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/play', methods=['POST'])
def play():
    guess = int(request.form['guess'])  # Obtém o palpite do formulário
    # Chama a função do jogo e obtém a resposta
    resultado = iniciar_jogo(guess)
    return render_template('resultado.html', resultado=resultado)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)