SELECT
    SUM(nota1)/COUNT(*) as média,
    id_turma
FROM Aluno
GROUP BY id_turma
