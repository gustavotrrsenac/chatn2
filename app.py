from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = 'MINHA CHAVE SECRETA'

@app.get('/')
def paginaInicial():
    if 'nomeUsuarioLogado' in session:
        return render_template('pagina_usuario_logado.html', nomeUsuario=session['nomeUsuarioLogado'])
    else:
        return redirect("/login")

@app.get('/login')
def exibirPaginaLogin():
    return render_template('login.html', msgErro='')


@app.post('/login')
def realizarLogin():
    usuarios = [
        {'email': 'teste@teste.com', 'password': '123456', 'nome': 'Teste'},
        {'email': 'camila@teste.com', 'password': 'abcdef', 'nome': 'Camila'},
        {'email': 'joao@teste.com', 'password': 'qwerty', 'nome': 'João'}
    ]

    email = request.form.get('email')
    password = request.form.get('password')

    nomeUsuarioEncontrado = None

    for u in usuarios:
        if u['email'] == email and u['password'] == password:
            nomeUsuarioEncontrado = u['nome']
            break

    if nomeUsuarioEncontrado is not None:
        session['nomeUsuarioLogado'] = nomeUsuarioEncontrado
        return render_template('pagina_usuario_logado.html', nomeUsuario=nomeUsuarioEncontrado)
    else:
        return render_template('login.html', msgErro='Usuário ou senha inválidos. Tente novamente.')

@app.get('/logout')
def realizarLogout():
    session.pop('nomeUsuarioLogado', None)
    return "Logout realizado com sucesso!"

def validarAutenticacaoUsuario():
    return ('nomeUsuarioLogado' in session)

@app.get('/pagina_usuario_logado')
def paginanomeUsuarioLogado():
    if validarAutenticacaoUsuario() == True:
        return render_template('pagina_usuario_logado.html', nomeUsuario=session['nomeUsuarioLogado'])
    else:
        return redirect("/login")
    
@app.errorhandler(404)
def page_not_found(e):
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)