-- Passo 1: Criar o Banco de dados(O nosso cofre principal)
Create DATABASE IF NOT EXISTS rota_financeira_db;

-- Passo 2: Avisar ao MySql que vamos trabalhar dentro desse cofre
Use rota_financeira_db;

-- Passo 3: Criar a nodssa primeira tabela(A gaveta do usuário)
CREATE TABLE IF NOT EXISTS usuario (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,
senha VARCHAR(255) NOT NULL,
data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

