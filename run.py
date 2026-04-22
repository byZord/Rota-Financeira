
from flask import Flask, render_template
import mysql.connector #Tradutor para implementar o BD

# Aqui estamos criando o aplicativo de fato. A variável app é o coração do site. O __name__ é uma configuração interna do python para ele saber onde achar as pastas do projeto
app = Flask(__name__) 

#configuração da fechadura do banco de dados
def conectar_banco():
    conexao = mysql.connector.connect(
    host = "local_host",
    user = "root",
    password = "root",
    database = "rota_financeira_db"
    )
    
    return conexao

# Isso aqui pe a rota. É como se fosse o GPS da internet. O / significa a "pagina inicial" Você diz: "Quando alguém entrar na página inicial execute a função abaixo"
@app.route('/')
def index():
    
    return render_template('index.html')

# Isso aqui é uma trava de segurança do Python. Ela garante que o servidor só vai ligar se você executar esse arquivo diretamente
if __name__ == '__main__':
    # Essa função faz com que toda vez que o código for salvo o servidor reinicie sozinho e aplique as mudanças, além de mostrar os erros detalhados na tela caso algo dê errado
    app.run(debug=True) 

#rota para testar o banco de dados
@app.route('/Testar-banco')
def testar_banco():
    try:
        #Tenta abrir a conexão e fechar logo em seguida
        conexao = conectar_banco
        conexao.close()
        return "<h1>Conexão com banco de dados feita com sucesso🚀</h1>"
    
    #Uma mensagem caso a conexão falhe (ele indica o motivo)
    except Exception as e:
        return f"<h1>Erro ao tentar conectar banco: {e}</h1>"
    
if __name__ == '__main__':
    app.run(debug=True)

