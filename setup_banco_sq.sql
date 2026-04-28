-- Passo 1: Criar o Banco de dados(O nosso cofre principal)
Create DATABASE IF NOT EXISTS rota_financeira_db;

-- Passo 2: Avisar ao MySql que vamos trabalhar dentro desse cofre
Use rota_financeira_db;

-- Passo 3: Criar a nossa primeira tabela(A gaveta do usuário)
CREATE TABLE IF NOT EXISTS usuario (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,
senha VARCHAR(255) NOT NULL,
data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM usuario;

-- Passo 4: Criar a tabela de Transações (A gaveta de receitas e despesas)
CREATE TABLE IF NOT EXISTS transacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    tipo ENUM('receita', 'despesa') NOT NULL,
    data_transacao DATE NOT NULL,
    
    -- A Mágica do Relacionamento (Chave Estrangeira)
    FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE
);

SELECT * FROM transacoes;

