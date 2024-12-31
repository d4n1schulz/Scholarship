/*E05
Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. 
Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.*/


SELECT DISTINCT au.nome 

FROM autor  AS au
LEFT JOIN livro AS li
ON  au.codautor =  li.autor 
LEFT JOIN editora  AS ed
ON li.editora = ed.codeditora
LEFT JOIN endereco AS en
ON ed.endereco = en.codendereco 
WHERE en.estado NOT IN ('RIO GRANDE DO SUL','SANTA CATARINA','PARANÁ')
ORDER BY au.nome ASC;










