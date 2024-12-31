/*E13
Apresente a query para listar os 10 produtos menos vendidos pelos canais de
E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no 
resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.*/

SELECT cdpro,
       nmcanalvendas,
       nmpro,
      SUM (qtd) AS quantidade_vendas

FROM tbvendas
WHERE status = 'Concluído' 
GROUP BY cdpro,nmcanalvendas
ORDER BY quantidade_vendas
LIMIT 10

