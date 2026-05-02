from flask import Flask, render_template, request 
import mysql.connector # Tradutor para implementar o BD
from datetime import date 

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
# Rota para receber os dados do usuario
@app.route('/adicionar-transacao', methods=['POST'])
def adicionar_transacao():
    # Primeiro capturar os dados usando os "names" que o front-end colocou lá no HTML
    descricao = request.form.get('descricao')
    valor = request.form.get('valor')  
    tipo = request.form.get('tipo')

    data_atual = date.today() #Pega a data atual do computador

    try:
        # Segundo: conectar o banco e preparar o cursor (COM PARÊNTESES!)
        conexao = conectar_banco()
        cursor = conexao.cursor()
        
        # 3: preparar o comando SQL seguro (COM A COLUNA DESCRICAO!)
        sql = "INSERT INTO transacoes (usuario_id, descricao, valor, tipo, data_transacao) VALUES (%s, %s, %s, %s, %s)"
        
        # Injetar os valores. Usamos ID 1 porque é o ID dos "Adms testes"
        valores = (1, descricao, valor, tipo, data_atual)
        
        # Executar e salvar (Commit é essencial, senão ele não grava)
        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f"SALVO NO BANCO: {descricao} - R$ {valor}")
        return f"<h1>Transação de '{descricao}' salva no banco de dados com sucesso</h1>"
    
    except Exception as e:
        return f"<h1>Erro ao tentar salvar no banco: {e}</h1>"
    
    
# Trava de segurança - DEVE SER SEMPRE A ÚLTIMA COISA DO ARQUIVO!
if __name__ == '__main__':
    app.run(debug=True)