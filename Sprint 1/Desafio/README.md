# Etapas


# 1. ... [Etapa I - Normalização](etapa-1/Modelagem_Relacional.sql)


Nessa etapa pode-se perceber com esse código:

    ```SQL
    SELECT * FROM tb_locacao;
    ```
A tabela "tb_locacao" possuía muitos atributos que se repetiam constantemente em uma consulta.
![](/Sprint%201/Evidências/tb_locacao(consulta).png)

### Identificação e criação de entidades separadas

Peguei as principais entidades no conjunto de dados original (tb_locacao) e as distribuí em tabelas relacionadas:

### Clientes (tb_cliente): 

    
    CREATE TABLE tb_cliente(
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(50),
    cidadeCliente VARCHAR(50),
    estadoCliente VARCHAR(50),
    paisCliente VARCHAR(50));
    
Contém informações exclusivas sobre os clientes, como nome, cidade, estado e país. Evita repetição de dados sobre clientes que aparecem em várias locações.


### Combustíveis (tb_combustivel): 

    
    CREATE TABLE tb_combustivel (
    idCombustivel PRIMARY KEY,
    tipoCombustivel VARCHAR(20),
    FOREIGN KEY (idCombustivel) REFERENCES tb_carros(idCombustivel)  );
    


Isolou os tipos de combustível, ligando-os aos carros. Isso evita a duplicação de informações para cada locação que usa o mesmo combustível.


### Carros (tb_carros): 

    
    CREATE TABLE tb_carros(
    idCarro PRIMARY KEY,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(50),
    modeloCarro VARCHAR(50),
    anoCarro INT,
    idCombustivel INT,
    FOREIGN KEY (idCombustivel) REFERENCES combustivel (idCombustivel)
    );
    

Representa os veículos com suas características, como marca, modelo, ano e classificação. Foi colocado uma chave estrangeira para a tabela de combustíveis.

    
### Vendedores (tb_vendedor): 

    
    CREATE TABLE tb_vendedor 
    (idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(50),
    sexoVendedor BOOLEAN,
    estadoVendedor VARCHAR(50) );
    

Possui dados sobre os vendedores, como nome, sexo e estado de origem. Evita repetição de dados em cada locação.


### Locações (locacao): 

    
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
    

Centraliza as operações de locação, contendo chaves estrangeiras para tb_cliente, tb_carros e tb_vendedor, além de dados transacionais, como datas, horários, quantidade de diárias e valores.


### Quilometragem (tb_kilometragem): 

    
    CREATE TABLE tb_kilometragem (
    idKm INTEGER PRIMARY KEY AUTOINCREMENT,
    idCarro INT,
    Kmcarro INT,
    FOREIGN KEY (idCarro) REFERENCES tb_carros(idCarro) 
    );
    
Criada para armazenar informações de quilometragem dos carros, que originalmente estavam na tabela de locação, mas são específicas de cada veículo.


As formas normais foram aplicadas para:
- Eliminar redundâncias.
- Manter a integridade referencial.
- Garantir eficiência em consultas e facilidade de manutenção.

### Inserções

Durante a normalização do banco de dados, foram utilizados comandos "INSERT INTO" e  "SELECT DISTINCT" para migrar os dados da tabela original (tb_locacao) para as novas tabelas criadas após a normalização. Abaixo, as inserções feitas:

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


### Modelo lógico após a normalização
![](/Sprint%201/Desafio/etapa-1/Modelo_Lógico_Relacional.png)

O modelo lógico relacional mostrado representa a estrutura do banco de dados após a etapa de normalização, que organiza os dados em tabelas distintas para reduzir redundâncias, garantir a integridade dos dados e melhorar a eficiência das consultas.

### Testando o banco normalizado 

    --Locações por vendedor

    SELECT ven.nomeVendedor AS Vendedor,
        COUNT(loc.idLocacao) AS totalLocacoes
    FROM locacao AS loc
    JOIN tb_vendedor AS ven ON loc.idVendedor = ven.idVendedor
    GROUP BY ven.nomeVendedor
    ORDER BY totalLocacoes DESC;

### Execução do código
![](/Sprint%201/Evidências/teste_relacional.png)

# 2. ... [Etapa II - Modelagem Dimensional](etapa-2/Modelagem_Dimensional.sql)

As dimensões foram estruturadas para otimizar a organização dos dados e facilitar análises detalhadas. Cada tabela de dimensão foi feita para evitar redundância e melhorar a eficiência do armazenamento, e simultâneamente a integridade dos dados.

### Dimensão cliente: 

    CREATE TABLE dimensao_cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(50),
    cidadeCliente VARCHAR(50),
    estadoCliente VARCHAR(50),
    paisCliente VARCHAR(50)
    );
Guarda dados dos clientes, permitindo análises geográficas e demográficas sem repetição de informações.

### Dimensão vendedor:
    CREATE TABLE dimensao_vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(50),
    sexoVendedor BOOLEAN,
    estadoVendedor VARCHAR(50)
    );
Possui dados dos vendedores, possibilitando análises de desempenho por região e características.

### Dimensão combustível
    CREATE TABLE dimensao_combustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(50)
    );
Guarda os tipos de combustível, permitindo segmentação das locações por categoria de combustível.

### Dimensão carros
    CREATE TABLE dimensao_carros
    (  idCarro INT PRIMARY KEY,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(50),
    modeloCarro VARCHAR(50),
    anoCarro INT,
    idCombustivel INT,
    FOREIGN KEY (idCombustivel) REFERENCES dimensao_combustivel(idCombustivel)
    );
Armazena especificações dos carros, como marca, modelo e tipo de combustível, evitando redundância e facilitando a análise do perfil dos veículos.

### Dimensão kilometragem 
    CREATE TABLE dimensao_kilometragem (
    idKm INT PRIMARY KEY,
    idCarro INT,
    Kmcarro INT,
    FOREIGN KEY (idCarro) REFERENCES dimensao_carros(idCarro)
    );
Armazena a quilometragem dos carros, possibilitando análises sobre desgaste e condições dos veículos.

### Fato locação
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
A tabela "fato_locacao" armazena os dados transacionais das locações, conectando clientes, carros e vendedores. Ela possui informações como o valor e quantidade diária da locação, data e hora de locação e entrega, permitindo análises sobre desempenho, receitas e comportamento dos clientes.

### Inserções

Após a criação das tabelas, a migração dos dados da tabela original (exemplo tb_cliente, tb_carro, etc.) para as tabelas dimensional foi realizada com os seguintes comandos "INSERT INTO" e "SELECT DISTINCT", que garantem a eliminação de duplicatas durante a inserção dos dados:

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

### Formatação
A data foi atualizada para o formato correto porque estava desformatado, o que poderia causar problemas em análises e consultas. 

    UPDATE fato_locacao
    SET dataLocacao = STRFTIME('%Y-%m-%d %H:%M:%S', 
        SUBSTR(dataLocacao, 1, 4) || '-' || 
        SUBSTR(dataLocacao, 5, 2) || '-' || 
        SUBSTR(dataLocacao, 7, 2) || ' 00:00:00')
    WHERE LENGTH(dataLocacao) = 8;

A conversão garante consistência e facilita o manuseio adequado dos dados de data e hora. 

#### Antes

![](/Sprint%201/Evidências/antes_formatacao_data.png)

#### Depois

![](/Sprint%201/Evidências/formatacao_data.png)

### Testando o banco dimensional

    --Quantidade de locações por tipo de carro

    SELECT dim.classiCarro AS tipoCarro,
        COUNT(fato.idLocacao) AS totalLocacoes
        
    FROM fato_locacao AS fato
    JOIN dimensao_carros AS dim ON fato.idCarro = dim.idCarro
    GROUP BY dim.classiCarro
    ORDER BY totalLocacoes DESC;

### Execução
![](/Sprint%201/Evidências/teste_dimensional.png)

### Modelo lógico dimensional Snowflake
![](/Sprint%201/Desafio/etapa-2/Modelo_Lógico_Dimensional.png)

Optei pela modelagem dimensional Snowflake para ter análises mais eficientes. Criei tabelas de dimensão como dimensao_cliente e dimensao_carros, que têm informações detalhadas de cada entidade. No centro, está a tabela de fatos "fato_locacao", que reúne métricas principais, como valores de locação, vinculando-as às dimensões. Com essa reestruturação, consegui eliminar redundâncias e garantir integridade.
