# Resumo

**Fundamentals of Analytics on AWS – Part 2**: Aprendi sobre data lakes, data warehouses e arquiteturas de dados modernas na AWS, explorando seus benefícios, desafios e serviços associados. Compreendi como utilizar serviços da AWS, como o Lake Formation, para criar e gerenciar essas arquiteturas, além de identificar casos de uso comuns e padrões de referência. O curso também destacou a importância da movimentação de dados e os pilares das arquiteturas de dados modernas, proporcionando uma visão prática e atualizada do mercado de analytics.

**AWS Glue Getting Started**: Aprendi a utilizar o AWS Glue e o DataBrew para integrar, catalogar e transformar dados, além de realizar análises de qualidade e perfil de dados. Compreendi os benefícios e a estrutura de custos dessas ferramentas, e como aplicá-las em cenários reais para otimizar processos de dados. Também explorei tutoriais práticos para usar o Glue Studio e o DataBrew diretamente no AWS Management Console.

**AWS - Tutoriais Técnicos - Analytics**: Aprendi a transformar e catalogar dados utilizando o AWS Glue, consultar dados com o AWS Athena e visualizar dados com o Amazon QuickSight. Essas ferramentas da AWS ajudam a transformar dados brutos em insights valiosos, facilitando a análise e a tomada de decisões. O conteúdo abordou desde a preparação dos dados até a criação de visualizações eficientes.


# Exercícios

## Exercício 1

1. ...
[Arquivos](../Sprint%206/Exercícios/E01/)

2. ...
[Evidências](../Sprint%206/Exercícios/E01/Evidências/)


## Exercício 2

1. ...
[Arquivos](../Sprint%206/Exercícios/E02/)

2. ...
[Evidências](../Sprint%206/Exercícios/E02/Evidências/)


## Exercício 3

1. ...
[Arquivo](../Sprint%206/Exercícios/E03/)

2. ...
[Evidências](../Sprint%206/Exercícios/E03/Evidências/)

# Evidências

### Exercício 1:

Etapa 1:

Declare e inicialize uma lista contendo 250 números inteiros obtidos de forma aleatória. Após, aplique o método reverse sobre o conteúdo da lista e imprima o resultado.

Execução:

![etapa-1](../Sprint%206/Exercícios/E01/Evidências/etapa-1.png)


Etapa 2:
Declare e inicialize uma lista contendo o nome de 20 animais. Ordene-os em ordem crescente
e itere sobre os itens, imprimindo um a um (pode utilizar list comprehension). Na sequência, armazene o conteúdo da
lista em um arquivo de texto, um item em cada linha.

Execução:

![etapa-2(1)](../Sprint%206/Exercícios/E01/Evidências/etapa-2(1).png)

Arquivo gerado:

![etapa-2(2)](../Sprint%206/Exercícios/E01/Evidências/etapa-2(2).png)


Etapa 3:
Gerar um dataset de nomes de pessoas

Execução:

![etapa-3(1)](../Sprint%206/Exercícios/E01/Evidências/etapa-3(1).png)

Arquivo gerado:

![etapa-3(2)](../Sprint%206/Exercícios/E01/Evidências/etapa-3(2).png)

#### Observação: Retirei o arquivo "nomes_aleatorios.txt" do repositório pois é um arquivo muito grande para passar ao repositório do github.

### Exercício 2:

Etapa 1:
Listar algumas linhas após a leitura do CSV

![etapa-1](../Sprint%206/Exercícios/E02/Evidências/et1.png)

Etapa 2:
Renomear a coluna para "Nomes", imprimir o esquema e mostrar 10 linhas diferentes

![etapa-2](../Sprint%206/Exercícios/E02/Evidências/et2.png)

Etapa 3: 
Ao dataframe ``df_nomes``adicione nova coluna chamada ``Escolaridade`` e atribua para cada linha um dos três valores de forma aleatória: *Fundamental*, *Medio* ou *Superior*. Para esta etapa, evite usar funções de iteração, como por exemplo: for, while, entre outras. Dê preferência aos métodos oferecidos pelo próprio Spark.

![etapa-3](../Sprint%206/Exercícios/E02/Evidências/et3.png)

Etapa 4:
Ao data frame ``df_nomes``, adicione nova coluna chamada ``Pais`` e atribua para cada linha o nome de um dos 13 países
da América do Sul, de forma aleatória. Para esta etapa, evite usar funções de iteração, como por exemplo: for, while,
entre outras. Dê preferência aos métodos oferecidos pelo próprio Spark.

![etapa-4](../Sprint%206/Exercícios/E02/Evidências/et4.png)


Etapa 5:
Ao dataframe ``df_nomes``, adicione nova coluna chamada ``AnoNascimento`` e atribua para cada linha um valor de ano entre 1945 e 2010, de forma aleatória. Para esta etapa, evite usar funções de iteração, como por exemplo: for, while, entre outras. Dê preferência aos métodos oferecidos pelo próprio Spark.

![etapa-5](../Sprint%206/Exercícios/E02/Evidências/et5.png)

Etapa 6:
Usando o metodo select do dataframe ``df_nomes``, selecione as pessoas que nasceram neste século. Armazene resultado em outro dataframe chamado ``df_select`` e mostre 10 nomes deste.

![etapa-6](../Sprint%206/Exercícios/E02/Evidências/et6.png)

Etapa 7:
Usando ``Spark SQL`` repita o processo da etapa 6.

![etapa-7](../Sprint%206/Exercícios/E02/Evidências/et7.png)

Etapa 8:
Usando o método filter do dataframe ``df_nomes``, conte o número de pessoas que são da geração *Millennials* (nascidos entre 1980 e 1994) no Dataset.

![etapa-8](../Sprint%206/Exercícios/E02/Evidências/et8.png)

Etapa 9:
Repita o processo da etapa 8 usando ``Spark SQL``.

![etapa-9](../Sprint%206/Exercícios/E02/Evidências/et9.png)

Etapa 10:

Usando ``Spark SQL``, obtenha a quantidade de pessoas de cada país para cada uma das gerações abaixo. Armazene o resultado em um novo dataframe e depois mostre todas as linhas em ordem crescente de Pais, Geração e Quantidade:

Baby Boomers - nascidos entre 1944 e 1964;

Geração X - nascidos entre 1965 e 1979;4

Millennials (Geração Y) - nascidos entre 1980 e 1994;

Geração Z - nascidos entre 1995 e 2015.

![etapa-10](../Sprint%206/Exercícios/E02/Evidências/et10.png)


### Exercício 3:

Criei a IAM Role para os jobs do AWS Glue

![criando_role](../Sprint%206/Exercícios/E03/Evidências/criando_role.png)

Indicando a role “AWSGlueServiceRole-Lab4" para ter acesso ao serviço AWS Glue

![add_role](../Sprint%206/Exercícios/E03/Evidências/add_role_glue.png)

Informando acesso total ao S3 para leitura e escrita

![permissoes_role](../Sprint%206/Exercícios/E03/Evidências/permissoes_role.png)

Criando o banco de dados no AWS Lake Formation no qual o crawler irá adicionar automaticamente uma tabela
a partir dos dados armazenados no S3

![database_lake_formation](../Sprint%206/Exercícios/E03/Evidências/criei_database_lake_formation.png)

Criando novo job no AWS Glue

![criando_job](../Sprint%206/Exercícios/E03/Evidências/config_job.png)

Criando parâmetros

![criando_parametros](../Sprint%206/Exercícios/E03/Evidências/parametros_job.png)

Adicionei o meu script do exercício

![add_script](../Sprint%206/Exercícios/E03/Evidências/adicionei_script.png)


Código executado

![execucao_sucedida](../Sprint%206/Exercícios/E03/Evidências/run_sucedida.png)

Outputs da execução:

![output_1](../Sprint%206/Exercícios/E03/Evidências/output_1.png)

![output_2](../Sprint%206/Exercícios/E03/Evidências/output_2.png)

![output_3](../Sprint%206/Exercícios/E03/Evidências/output_3.png)

Diretórios dos arquivos gerados:

![pastas_geradas](../Sprint%206/Exercícios/E03/Evidências/pastas_arq_gerados.png)


Criei o crawler

![crawler_criado](../Sprint%206/Exercícios/E03/Evidências/crawler_criado.png)

Abri o Athena com a o comando SQL já criado para fazer um Select na tabela criada

![query_table_criada](../Sprint%206/Exercícios/E03/Evidências/query_data_table_criado.png)

# Certificados

![aws_analytics_2](../Sprint%206/Certificados/Fundamentos_analytics_AWS%20–%20Parte%202.png)

![aws_Glue](../Sprint%206/Certificados/AWS_Glue.png)

