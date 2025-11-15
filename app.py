from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.get('/')
def home():
    teste = request
    a = 10
    b = 20
    c = a + b
    return f"A soma é {c}"

@app.get('/login')
def login():
    return render_template('login.html')


@app.post('/login')
def realizarLogin():
    email = request.form.get('email')
    password = request.form.get('password')
    if(email == 'teste@teste.com' and password == '123456'):
        return "Login realizado com sucesso!"
    else:
        return "Falha no login."


if __name__ == '__main__':
    app.run(debug=True)