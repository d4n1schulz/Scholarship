/*E08
Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam 
com o status concluída.  
As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.*/




 WITH qtd_vendas AS (SELECT COUNT (*) AS qtd,
						           vdd.cdvdd
					 
					FROM tbvendas AS ven
					LEFT JOIN tbvendedor AS vdd
					ON ven.cdvdd = vdd.cdvdd 
					WHERE ven.status = 'Concluído'
					GROUP BY ven.cdvdd
					ORDER BY qtd DESC
					LIMIT 1) 

SELECT cdvdd,
	   nmvdd

FROM tbvendedor 
WHERE cdvdd = (SELECT cdvdd FROM qtd_vendas)


