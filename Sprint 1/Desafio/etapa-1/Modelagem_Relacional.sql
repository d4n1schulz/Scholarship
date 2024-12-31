CREATE TABLE tb_cliente(
idCliente INT PRIMARY KEY,
nomeCliente VARCHAR(50),
cidadeCliente VARCHAR(50),
estadoCliente VARCHAR(50),
paisCliente VARCHAR(50)
);


CREATE TABLE tb_combustivel (
idCombustivel PRIMARY KEY,
tipoCombustivel VARCHAR(20),
FOREIGN KEY (idCombustivel) REFERENCES tb_carros(idCombustivel)  );

CREATE TABLE tb_carros(
idCarro PRIMARY KEY,
classiCarro VARCHAR(50),
marcaCarro VARCHAR(50),
modeloCarro VARCHAR(50),
anoCarro INT,
idCombustivel INT,
FOREIGN KEY (idCombustivel) REFERENCES combustivel (idCombustivel)
);


CREATE TABLE tb_vendedor 
(idVendedor INT PRIMARY KEY,
nomeVendedor VARCHAR(50),
sexoVendedor BOOLEAN,
estadoVendedor VARCHAR(50) );


CREATE TABLE locacao (
idLocacao INT PRIMARY KEY NOT NULL,
idCliente INT NOT NULL,
idCarro INT NOT NULL,
idVendedor INT NOT NULL,
dataLocacao DATE NOT NULL,
horaLocacao TIME NOT NULL,
qtdDiaria INT NOT NULL,
vlrDiaria DECIMAL NOT NULL,
dataEntrega DATE NOT NULL,
horaEntrega TIME NOT NULL,
FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
FOREIGN KEY (idCarro) REFERENCES tb_carros(idCarro),
FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor)
);

CREATE TABLE tb_kilometragem (
    idKm INTEGER PRIMARY KEY AUTOINCREMENT,
    idCarro INT,
    Kmcarro INT,
    FOREIGN KEY (idCarro) REFERENCES tb_carros(idCarro) 
);

INSERT INTO tb_cliente (idcliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idcliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao ;

INSERT INTO tb_combustivel (idCombustivel,tipoCombustivel)
SELECT DISTINCT idCombustivel,tipoCombustivel
FROM tb_locacao ;

INSERT INTO tb_carros (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT DISTINCT idCarro,classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel
FROM tb_locacao;

INSERT INTO tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

INSERT INTO locacao (idLocacao, idCliente,idCarro,idVendedor,dataLocacao, horaLocacao, qtdDiaria ,vlrDiaria,dataEntrega,horaEntrega)
SELECT DISTINCT idLocacao, idCliente,idCarro,idVendedor,dataLocacao, horaLocacao, qtdDiaria ,vlrDiaria,dataEntrega,horaEntrega
FROM tb_locacao;

INSERT INTO tb_kilometragem (idCarro,Kmcarro)
SELECT DISTINCT idCarro, KmCarro
FROM tb_locacao ;






--Locações por Vendedor

SELECT ven.nomeVendedor AS Vendedor,
       COUNT(loc.idLocacao) AS totalLocacoes
FROM locacao AS loc
JOIN tb_vendedor AS ven ON loc.idVendedor = ven.idVendedor
GROUP BY ven.nomeVendedor
ORDER BY totalLocacoes DESC;







