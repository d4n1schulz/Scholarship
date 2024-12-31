/*3.1. Etapa 1
Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV. Utilizar o caractere ";" (ponto e
vírgula) como separador. Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus
respectivos nomes de cabeçalho que listamos abaixo:
CodLivro Titulo CodAutor NomeAutor Valor CodEditora NomeEditora
Observação: O arquivo exportado, conforme as especificações acima, deve ser disponibilizado no GitHub.*/

SELECT DISTINCT li.cod AS CodLivro,
       li.titulo AS Titulo,
       li.autor AS CodAutor,
       au.nome AS NomeAutor,
       li.valor AS Valor ,
       li.editora AS CodEditora,
       ed.nome AS NomeEditora
  
FROM livro AS li
LEFT JOIN autor AS au
ON li.autor = au.codautor 
LEFT JOIN editora AS ed
ON li.editora = ed.codeditora 
ORDER BY valor DESC
LIMIT 10;