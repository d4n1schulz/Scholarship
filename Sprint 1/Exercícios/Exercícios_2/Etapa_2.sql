/*3.2. Etapa 2
Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na biblioteca para um arquivo
CSV. Utilizar o caractere | (pipe) como separador. Lembre-se que o conteúdo do seu arquivo deverá respeitar a
sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo:
CodEditora NometEditora QuantidadeLivros
Observação: O arquivo exportado, conforme as especificações acima, deve ser disponibilizado no GitHub.*/

SELECT li.editora AS CodEditora,
       ed.nome AS NomeEditora, 
       COUNT(*) AS QuantidadeLivros

FROM livro AS li
LEFT JOIN editora AS ed
ON li.editora = ed.codeditora 
GROUP BY li.editora
ORDER BY QuantidadeLivros DESC 
LIMIT 5;

