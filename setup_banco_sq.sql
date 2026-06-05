-- ============================================
-- Passo 1: Criar o banco de dados (O nosso cofre principal)
-- ============================================

CREATE DATABASE IF NOT EXISTS rota_financeira_db;

-- ============================================
-- Passo 2: Avisar ao MySQL que vamos trabalhar dentro desse cofre
-- ============================================

USE rota_financeira_db;

-- ============================================
-- Passo 3: Criar a nossa primeira tabela (A gaveta de usuários)
-- ============================================

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,

    nome VARCHAR(100) NOT NULL,

    email VARCHAR(100) NOT NULL UNIQUE,

    senha VARCHAR(255) NOT NULL,

    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- Passo 4: Criar a tabela de Transações
-- (A gaveta de receitas e despesas)
-- ============================================

CREATE TABLE IF NOT EXISTS transacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,

    usuario_id INT NOT NULL,

    descricao VARCHAR(255) NOT NULL,

    valor DECIMAL(10,2) NOT NULL,

    tipo ENUM('receita', 'despesa') NOT NULL,

    data_transacao DATE NOT NULL,

    -- A Mágica do Relacionamento (Chave Estrangeira)
    FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)
        ON DELETE CASCADE
);

-- ============================================
-- Passo 5: Inserir um Usuário de Teste
-- Como o ID é automático, não precisamos informá-lo
-- ============================================

INSERT INTO usuarios (
    nome,
    email,
    senha
)
VALUES (
    'Administrador Teste',
    'admin@teste.com',
    'senha123'
);

-- ============================================
-- Passo 6: Inserir Transações de Teste para o usuário 1
-- Vamos colocar 3 transações diferentes
-- ============================================

INSERT INTO transacoes (
    usuario_id,
    descricao,
    valor,
    tipo,
    data_transacao
)
VALUES
(
    1,
    'Salário Mensal',
    3500.00,
    'receita',
    '2026-04-05'
),
(
    1,
    'Supermercado Extra',
    450.50,
    'despesa',
    '2026-04-10'
),
(
    1,
    'Conta de Luz',
    120.00,
    'despesa',
    '2026-04-15'
);

-- ============================================
-- Passo 7: Criar a tabela de Investimentos 
-- ============================================

CREATE TABLE IF NOT EXISTS investimentos ( 
    id INT AUTO_INCREMENT PRIMARY KEY, 
    usuario_id INT NOT NULL, 
    tipo_investimento VARCHAR(100) NOT NULL, -- Ex: Tesouro Direto, CDB, Ações, Poupança 
    valor_aplicado DECIMAL(10, 2) NOT NULL, 
    data_aplicacao DATE NOT NULL, 
     
    -- O Relacionamento: Garante que o investimento pertence ao usuário correto 
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE 
); 
 
-- ======================================================================== 
-- Passo 8: Inserir Investimentos de Teste para o usuário 1 (Administrador)
-- ========================================================================
 
INSERT INTO investimentos (usuario_id, tipo_investimento, valor_aplicado, data_aplicacao) 
VALUES  
(1, 'CDB Banco Inter 102% CDI', 1200.00, '2026-05-10'), 
(1, 'Tesouro Selic 2029', 850.00, '2026-05-15'); 

-- ================================================================= 
-- Passo 9: Conferir se a nova gaveta foi criada com os dados dentro
-- =================================================================
 
SELECT * FROM investimentos; 