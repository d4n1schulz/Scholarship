/*E07
Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.*/

SELECT au.nome

FROM autor AS au
LEFT JOIN livro AS li
ON au.codautor = li.autor
WHERE li.autor IS NULL
ORDER BY au.nome ASC; 