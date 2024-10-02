from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


@app.route('/')
def home():
    return "Bem-vindo à página principal!"


@app.route('/cliente', methods=['GET', 'POST'])
def cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']

    flash("Cadastro realizado com sucesso!")
    return render_template('cliente.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        idade = request.form['idade']
        endereco = request.form['endereco']
        numero = request.form['numero']

        try:

            datetime.strptime(data_nascimento, '%Y-%m-%d')
        except ValueError:
            flash("A data de nascimento deve estar no formato YYYY-MM-DD.")
            return redirect(url_for('cadastro'))

        if not idade.isdigit():
            flash("A idade deve ser um número inteiro.")
            return redirect(url_for('cadastro'))

        if not numero.isdigit():
            flash("O número deve ser um valor inteiro.")
            return redirect(url_for('cadastro'))

        flash("Cadastro realizado com sucesso!")
        return redirect(url_for('cadastro'))

    return render_template('cadastro.html')


if __name__ == '__main__':
    app.run(debug=True)
