from flask import Flask, render_template, request
import mysql.connector # Tradutor para implementar o BD

# Aqui estamos criando o aplicativo de fato. A variável app é o coração do site.
app = Flask(__name__) 

# Configuração da fechadura do banco de dados
def conectar_banco():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "rota_financeira_db"
    )
    return conexao

# Rota da página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para testar o banco de dados
@app.route('/testar-banco')
def testar_banco():
    try:
        # Tenta abrir a conexão e fechar logo em seguida
        conexao = conectar_banco()
        conexao.close()
        return "<h1>Conexão com banco de dados feita com sucesso</h1>"
    except Exception as e:
        return f"<h1>Erro ao tentar conectar banco: {e}</h1>"

# Rota para receber os dados do usuario
@app.route('/adicionar-transacao', methods=['POST'])
def adicionar_transacao():
    # Primeiro capturar os dados usando os "names" que o front-end colocou lá no HTML
    descricao = request.form.get('descricao')
    valor = request.form.get('valor')  
    tipo = request.form.get('tipo')

    # Imprimir no terminal do VS code para auditar as transações
    print("-----------------------------------------------")
    print(f" DADOS RECEBIDOS DO FRONT-END:")
    print(f"Descrição: {descricao}")
    print(f"Valor: R$ {valor}")
    print(f"Tipo: {tipo}")
    print("-----------------------------------------------")

    return f"<h1>Dados de '{descricao}' recebidos com sucesso pelo Motor Python! </h1>"

# Trava de segurança - DEVE SER SEMPRE A ÚLTIMA COISA DO ARQUIVO!
if __name__ == '__main__':
    app.run(debug=True)