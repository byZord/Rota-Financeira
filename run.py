from flask import Flask, render_template, request, redirect, url_for
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
    try:
        # Abre a conexão e cria o cursor
        conexao = conectar_banco()

        #O dictionary = True faz o python organizar os dados com os nomes das colubas (ex: linha[Descricao])
        cursor = conexao.cursor(dictionary=True)

        # O comando SQL para ler a tabela (SELECT), ordenado da mais mais nova para a mais velha
        sql = "SELECT * FROM transacoes ORDER BY data_transacao DESC"
        cursor.execute(sql)

        # Pega todas as linhas que o banco achou e guarda na variavel
        minhas_transacoes = cursor.fetchall()

        # Fechando as portas
        cursor.close()
        conexao.close()
        
    except Exception as e:
        # Trava para o pc: se não achar o banco, avisa no terminal e cria uma lista vazia
        print(f"Aviso: Banco não conectado. Carregando site vazio. Error: {e}")
        minhas_transacoes = []

    # Carrega o HTML e INJETA a lista de dados lá dentro
    return render_template('index.html', lista_para_html=minhas_transacoes)

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
        
        # Redireciona para a pagina principal "index"
        return redirect(url_for('index'))
    
    except Exception as e:
        # SE DER ERRO, ELE CAI AQUI NA AMBULÂNCIA
        return f"<h1>Erro ao tentar salvar no banco: {e}</h1>"
    
    
# Trava de segurança - DEVE SER SEMPRE A ÚLTIMA COISA DO ARQUIVO!
if __name__ == '__main__':
    app.run(debug=True)