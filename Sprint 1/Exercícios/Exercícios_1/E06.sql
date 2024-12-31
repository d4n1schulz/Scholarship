/*E06
Apresente a query para listar o autor com maior número de livros publicados. 
O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.*/

SELECT au.codautor, 
 	   au.nome,
 	   COUNT(*) AS quantidade_publicacoes

FROM autor AS au
LEFT JOIN livro AS li
ON au.codautor = li.autor 
GROUP BY au.codautor 
ORDER BY quantidade_publicacoes DESC
LIMIT 1;


