/*E14
Apresente a query para listar o gasto médio por estado da federação. 
As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a 
coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.
Observação: Apenas vendas com status concluído.*/

SELECT estado,
       ROUND (AVG(qtd*vrunt),2) AS gastomedio

FROM tbvendas 
WHERE status = 'Concluído'
GROUP BY estado
ORDER BY gastomedio DESC;
