/*E09
Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, 
e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.*/

WITH produto_mais_vendido AS(SELECT COUNT(*) as qtd,
      cdpro,
      nmpro
	   
FROM tbvendas 
WHERE dtven BETWEEN '2014-02-03' AND '2018-02-02' AND
status = 'Concluído'
GROUP BY cdpro,nmpro )

SELECT cdpro,
       nmpro
       
FROM produto_mais_vendido
WHERE qtd = (SELECT MAX(qtd) FROM produto_mais_vendido)
