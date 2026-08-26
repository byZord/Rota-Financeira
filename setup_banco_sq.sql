USE rota_financeira_db;
-- ========================================================
-- CONSULTAS DE HOMOLOGAÇÃO (META #8)
-- ========================================================

-- TESTE 1: Agrupar e somar apenas as RECEITAS por mês
SELECT 
    MONTH(data_transacao) AS numero_mes,
    SUM(valor) AS total_mensal
FROM transacoes
WHERE tipo = 'receita'
GROUP BY MONTH(data_transacao)
ORDER BY numero_mes;

-- TESTE 2: Agrupar e somar apenas as DESPESAS por mês
SELECT 
    MONTH(data_transacao) AS numero_mes,
    SUM(valor) AS total_mensal
FROM transacoes
WHERE tipo = 'despesa'
GROUP BY MONTH(data_transacao)
ORDER BY numero_mes;

-- TESTE 3: Homologação das Metas Cadastradas
SELECT 
    id,
    nome_meta, 
    valor_alvo, 
    valor_atual, 
    data_limite 
FROM metas;