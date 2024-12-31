/*E03
 Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
 O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
 Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.*/

SELECT COUNT(li.cod) AS quantidade,
	   ed.nome,
	   en.estado,
	   en.cidade

FROM livro AS li
LEFT JOIN editora AS ed
ON li.editora = ed.codeditora 
LEFT JOIN endereco AS en
ON ed.endereco = en.codendereco
GROUP BY li.editora
ORDER BY quantidade DESC
LIMIT 5;


