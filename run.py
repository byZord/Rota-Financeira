
from flask import Flask, render_template

# Aqui estamos criando o aplicativo de fato. A variável app é o coração do site. O __name__ é uma configuração interna do python para ele saber onde achar as pastas do projeto
app = Flask(__name__) 

# Isso aqui pe a rota. É como se fosse o GPS da internet. O / significa a "pagina inicial" Você diz: "Quando alguém entrar na página inicial execute a função abaixo"
@app.route('/')
def index():
    
    return render_template('index.html')

# Isso aqui é uma trava de segurança do Python. Ela garante que o servidor só vai ligar se você executar esse arquivo diretamente
if __name__ == '__main__':
    # Essa função faz com que toda vez que o código for salvo o servidor reinicie sozinho e aplique as mudanças, além de mostrar os erros detalhados na tela caso algo dê errado
    app.run(debug=True) 