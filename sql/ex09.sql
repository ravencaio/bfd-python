SELECT
    ano,
    COUNT(*) as qtd_turmas
FROM Turma
GROUP BY ano
HAVING qtd_turmas > 2