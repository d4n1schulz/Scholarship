/*E12
Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto 
em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
Observação: Apenas vendas com status concluído.*/

WITH  total_bruto AS (SELECT SUM(ven.qtd*ven.vrunt) AS valor_total_vendas,
ven.cdvdd

FROM tbvendas AS ven
LEFT JOIN tbvendedor AS vdd
ON ven.cdvdd = vdd.cdvdd 
WHERE ven.status = 'Concluído'
GROUP BY ven.cdvdd)

SELECT dp.cddep,
	   dp.nmdep,
	   dp.dtnasc,
	   br.valor_total_vendas

FROM total_bruto AS br
LEFT JOIN tbdependente AS dp
ON br.cdvdd = dp.cdvdd 
WHERE valor_total_vendas = (SELECT MIN(valor_total_vendas) FROM total_bruto);

