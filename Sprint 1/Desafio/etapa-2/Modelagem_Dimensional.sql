CREATE TABLE dimensao_cliente (
 idCliente INT PRIMARY KEY,
 nomeCliente VARCHAR(50),
 cidadeCliente VARCHAR(50),
 estadoCliente VARCHAR(50),
 paisCliente VARCHAR(50)
);

CREATE TABLE dimensao_vendedor (
 idVendedor INT PRIMARY KEY,
 nomeVendedor VARCHAR(50),
 sexoVendedor BOOLEAN,
 estadoVendedor VARCHAR(50)
);

CREATE TABLE dimensao_combustivel (
 idCombustivel INT PRIMARY KEY,
 tipoCombustivel VARCHAR(50)
);

CREATE TABLE dimensao_carros
(  idCarro INT PRIMARY KEY,
   classiCarro VARCHAR(50),
   marcaCarro VARCHAR(50),
   modeloCarro VARCHAR(50),
   anoCarro INT,
   idCombustivel INT,
   FOREIGN KEY (idCombustivel) REFERENCES dimensao_combustivel(idCombustivel)
);

CREATE TABLE dimensao_kilometragem (
 idKm INT PRIMARY KEY,
 idCarro INT,
 Kmcarro INT,
 FOREIGN KEY (idCarro) REFERENCES dimensao_carros(idCarro)
);

CREATE TABLE fato_locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    dataLocacao DATE,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL,
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES dimensao_cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES dimensao_carros(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES dimensao_vendedor(idVendedor) );

INSERT INTO dimensao_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_cliente;

INSERT INTO dimensao_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_vendedor;

INSERT INTO dimensao_combustivel (idCombustivel, tipoCombustivel)
SELECT idCombustivel, tipoCombustivel
FROM tb_combustivel;

INSERT INTO dimensao_carros (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM tb_carros;

INSERT INTO dimensao_kilometragem (idKm, idCarro, Kmcarro)
SELECT idKm, idCarro, Kmcarro
FROM tb_kilometragem;

INSERT INTO fato_locacao (idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
SELECT idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM locacao;

select * from fato_locacao fl 
select * from dimensao_kilometragem dk 
select * from dimensao_carros dc 
select * from dimensao_vendedor dv 
select * from dimensao_combustivel dc 
select * from dimensao_cliente dc 


--foi atualizado os valores para o formato correto
UPDATE fato_locacao
SET dataLocacao = STRFTIME('%Y-%m-%d %H:%M:%S', 
    SUBSTR(dataLocacao, 1, 4) || '-' || 
    SUBSTR(dataLocacao, 5, 2) || '-' || 
    SUBSTR(dataLocacao, 7, 2) || ' 00:00:00')
WHERE LENGTH(dataLocacao) = 8;


--Quantidade de locações por tipo de carro

SELECT dim.classiCarro AS tipoCarro,
       COUNT(fato.idLocacao) AS totalLocacoes
       
FROM fato_locacao AS fato
JOIN dimensao_carros AS dim ON fato.idCarro = dim.idCarro
GROUP BY dim.classiCarro
ORDER BY totalLocacoes DESC;




