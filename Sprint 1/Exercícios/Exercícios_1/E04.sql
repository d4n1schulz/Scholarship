/*E04
Apresente a query para listar a quantidade de livros publicada por cada autor. 
Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).*/

SELECT au.nome,
	   au.codautor,
	   au.nascimento,
	   COUNT(li.autor) AS quantidade
	
FROM autor AS au
LEFT JOIN livro AS li
ON au.codautor =  li.autor 
GROUP BY au.codautor
ORDER BY au.nome ASC; 





