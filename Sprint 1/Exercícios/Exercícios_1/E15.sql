/*E15
Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.*/

SELECT cdven

FROM tbvendas 
WHERE deletado = 1
ORDER BY cdven;