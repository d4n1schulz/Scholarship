# Desafio DataLake - Parte 2

Comecei criando o diretório Trusted no meu DataLake:

![trusted_criado](../Evidências/trusted_criada.png)

Como inicialmente eu escolhi analisar apenas as séries de Guerra, no CSV eu filtrei as séries do gênero Guerra para saber a quantidade, mas ao fazer a filtragem percebi que tinha poucos dados com essas condições:

![linhas_series_war](../Evidências/linhas_war_csv.png)

Sendo assim, pensei em analisar dados de séries de Guerra e Crime, então, precisei buscar no TMDB dados de séries de Crime.

## Análises que pretendo fazer

1. Distribuição de Notas IMDb: Analisar a distribuição das notas IMDb para séries de guerra e crime.

2. Tendência de Lançamentos: Verificar a quantidade de séries lançadas por ano para cada gênero.

3. Relação Nota e Votos: Explorar a correlação entre as notas IMDb e o número de votos.

4. Status das Séries: Examinar a distribuição do status das séries e sua relação com as notas.

5. Comparação de Estúdios: Comparar a produção e avaliação média das séries por estúdio.

6. Produção por Estúdio e Ano: Analisar a evolução da produção de séries por estúdio ao longo dos anos.

---

Código Lambda executado:

![dados_series_crime](../Evidências/dados_crime_api.png)

Arquivo gerado:

![arq_json_crimes](../Evidências/arq_json_crimes.png)

Configurei a role para ter as permissões necessárias para o processamento no Glue

![config_role](../Evidências/config_role.png)

Adicionei a role ao AWS Glue

![add_role_glue](../Evidências/role_glue.png)

Fornecendo ao Glue o acesso ao S3

![acesso_glue_s3](../Evidências/acesso_glue_s3.png)

Configuração final do AWS Glue

![config_final_glue](../Evidências/glue_config_final.png)

Criei um banco de dados no catálogo do Glue

![lakeformation_database](../Evidências/database_glue.png)

## Criando Job 1
Criei Job no AWS Glue 

![criando_job](../Evidências/criando_job.png)

Configurei o Job no AWS Glue

![config_job_Glue](../Evidências/config_job.png)

Adicionei os parâmetros dos caminhos de origem e destino no S3

![parameters](../Evidências/parameters.png)

## Analisando o que eu irei tratar no CSV de Series

Pensei em mudar o nome da coluna tituloPincipal para tituloPrincipal, pois estava digitado errado.

![coluna_errada](../Evidências/coluna_errada.png)

As colunas anoLancamento, anoTermino e tempoMinutos, anoNascimento, anoFalecimento, numeroVotos, notaMedia precisaram ser convertidas para tipo numérico, pois estavam como string.

![tipos_errados](../Evidências/tipos_csv.png)

Também idenfiquei valores duplicados, então escolhi remover as duplicatas.

![duplicados](../Evidências/duplicados.png)

## Código para fazer o ETL no AWS Glue (Job 1):

### **1. Importação de Bibliotecas**
```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col
```
---

### **2. Obtenção de Parâmetros do Job**
```python
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])
```
- Obtém os argumentos **JOB_NAME**, **S3_INPUT_PATH** (caminho do arquivo de entrada no S3) e **S3_TARGET_PATH** (caminho do arquivo de saída).

---

### **3. Inicialização do Spark e Glue**
```python
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
```
---

### **4. Definição dos Caminhos de Entrada e Saída**
```python
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']
```
- Define os caminhos do **S3** com base nos parâmetros fornecidos.

---

### **5. Leitura do Arquivo CSV do S3**
```python
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {"paths": [source_file]},
    "csv",
    {"withHeader": True, "separator": "|"}
)
```
---

### **6. Conversão de DynamicFrame para DataFrame do Spark**
```python
df = df.toDF()
```
- Converti um **DynamicFrame**  para um **DataFrame do Spark**, para permitir a manipulação com PySpark.

---

### **7. Correção de Nome de Coluna**
```python
df = df.withColumnRenamed("tituloPincipal", "tituloPrincipal")
```
- Renomeia a coluna **"tituloPincipal"** para **"tituloPrincipal"** (correção de um erro de digitação).

---

### **8. Conversão de Colunas para Tipo Numérico**
```python
df = df.withColumn("anoLancamento", col("anoLancamento").cast("int"))
df = df.withColumn("anoTermino", col("anoTermino").cast("int"))
df = df.withColumn("tempoMinutos", col("tempoMinutos").cast("int"))
df = df.withColumn("anoNascimento", col("anoNascimento").cast("int"))
df = df.withColumn("anoFalecimento", col("anoFalecimento").cast("int"))
df = df.withColumn("numeroVotos", col("numeroVotos").cast("int"))
df = df.withColumn("notaMedia", col("notaMedia").cast("int"))
```
- Converte as colunas **anoLancamento**, **anoTermino**, **tempoMinutos**, **anoNascimento**, **anoFalecimento**, **numeroVotos** e **notaMedia**  para o tipo **inteiro**.

---

### **9. Remoção de Duplicatas**
```python
df = df.dropDuplicates()
```
---

### **10. Salvamento no S3 em Formato Parquet**
```python
df.write.mode("overwrite").parquet(target_path)
```
---

A Execução foi realizada com sucesso:

![run1_exec](../Evidências/run1_sucedida.png)

Arquivos gerados:

![arq_gerados](../Evidências/arq_csv_gerados.png)

## Criando Job 2

Criando o segundo Job para tratar os dados da API do TMDB

![config_job_json](../Evidências/config_job2.png)

Adicionando parameters ao segundo Job

![parameters_2](../Evidências/parameters_2.png)


## Analisando o que eu irei tratar no JSON do TMDB

Na coluna numeroEpisodios valores nulos (NaN) serão substituídos por 0 e a coluna será convertida para o tipo int. Pois em muitos casos, um valor nulo em numeroEpisodios pode indicar que a série não tem episódios ou que a informação não está disponível. E também o número de episódios é um valor inteiro. A conversão para int garante que os dados estejam no formato correto para análises futuras.

Tipo da coluna numeroEpisodios

![num_ep_tipo](../Evidências/tipo_num_ep.png)

Na coluna estudio valores "N/A" serão substituídos por "Desconhecido". Os textos serão normalizados para maiúsculas. Porque "N/A" é uma forma comum de indicar dados faltantes. Substituí-lo por "Desconhecido" padroniza a representação de valores ausentes. Textos em formatos inconsistentes (como "NHK", "nhk", "Nhk") podem causar problemas em agrupamentos ou filtros. Converter tudo para maiúsculas garante consistência.

Os textos nas colunas tituloOriginal e estudio serão convertidos para maiúsculas, porque textos em maiúsculas facilitam comparações e buscas, evitando problemas como duplicatas causadas por diferenças de caracteres (ex: "Netflix" vs "NETFLIX").


## Código para fazer o ETL no AWS Glue (Job 2):

### **1. Importação das Bibliotecas**
```python
import sys
import re
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, upper, when
```
---

### **2. Obtenção de Argumentos do AWS Glue Job**
```python
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_PATH', 'TARGET_PATH'])
```
- **Argumentos:**
  - `INPUT_PATH`: Caminho(s) dos arquivos JSON de entrada no S3.
  - `TARGET_PATH`: Caminho base de saída para os arquivos Parquet no S3.

---

### **3. Conversão de Caminhos em Listas**
```python
json_paths = args['INPUT_PATH'].split(',')
parquet_base_path = args['TARGET_PATH']
```
- **INPUT_PATH** é dividido em uma lista de caminhos separados por vírgula, permitindo processar múltiplos arquivos JSON.
- **TARGET_PATH** é atribuído à variável **parquet_base_path**, que será usada como base para o caminho de saída.

---

### **4. Inicialização do Spark e AWS Glue**
```python
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
```
---

### **5. Função para Extrair Data do Caminho do Arquivo**
```python
def extract_date_from_path(path):
    match = re.search(r'(\d{4})/(\d{2})/(\d{2})/', path)
    if match:
        return match.group(1), match.group(2), match.group(3)
    else:
        raise ValueError("Data não encontrada no caminho do arquivo")
```
- **Função:**
  - Extrai a data (ano, mês e dia) do caminho do arquivo JSON usando uma expressão regular.
  - Se a data não for encontrada, uma exceção é lançada.

---

### **6. Processamento de Cada Arquivo JSON Individualmente**
```python
for path in json_paths:
    ano, mes, dia = extract_date_from_path(path)
    
    dynamic_frame = glueContext.create_dynamic_frame.from_options(
        format_options={"multiline": True},
        connection_type="s3",
        format="json",
        connection_options={"paths": [path], "recurse": True}
    )
```
- Para cada caminho de arquivo JSON:
  - Extrai a data (ano, mês e dia) do caminho.
  - Cria um **DynamicFrame** a partir do JSON no S3, com a opção **multiline=True** para ler JSONs com múltiplas linhas.

---

### **7. Conversão para DataFrame e Aplicação de Transformações**
```python
    df = dynamic_frame.toDF()

    df = df.withColumn("anoLancamento", when(col("anoLancamento") == "", "Desconhecido").otherwise(col("anoLancamento").cast("int")))

    df = df.withColumn("numeroEpisodios", when(col("numeroEpisodios").isNull(), 0).otherwise(col("numeroEpisodios").cast("int")))

    df = df.withColumn("estudio", when(col("estudio") == "N/A", "Desconhecido").otherwise(col("estudio")))

    df = df.withColumn("tituloOriginal", upper(col("tituloOriginal")))
    
    df = df.withColumn("estudio", upper(col("estudio")))
```
- **Transformações aplicadas:**
  - `anoLancamento`: Se estiver vazio, é atribuído "Desconhecido". Caso contrário, é convertido para **inteiro**.
  - `numeroEpisodios`: Se for **NULL**, é substituído por 0, caso contrário, é convertido para **inteiro**.
  - `estudio`: Se o valor for **"N/A"**, é substituído por "Desconhecido".
  - `tituloOriginal` e `estudio`: São convertidos para **maiúsculas**.

---

### **8. Conversão de Volta para DynamicFrame**
```python
    transformed_dynamic_frame = DynamicFrame.fromDF(df, glueContext, "transformed_df")
```
- O **DataFrame** transformado é convertido de volta para **DynamicFrame**, que é o formato utilizado pelo AWS Glue para salvar os dados.

---

### **9. Definição do Caminho de Saída**
```python
    final_path = f"{parquet_base_path}/TMDB/Parquet/Series/{ano}/{mes}/{dia}/"
```
- O caminho de saída é criado com base na data extraída do caminho do arquivo JSON, seguindo o padrão **ano/mês/dia**.

---

### **10. Escrita do DataFrame Transformado no S3 em Parquet**
```python
    glueContext.write_dynamic_frame.from_options(
        frame=transformed_dynamic_frame,
        connection_type="s3",
        format="parquet",
        connection_options={"path": final_path} 
    )
```
- O **DynamicFrame** transformado é salvo no S3 no formato **Parquet**, no caminho especificado.
---

### **11. Finalizando o Job**
```python
job.commit()
```
- Finaliza o job do Glue com **job.commit()**.

---

A execução foi realizada com sucesso

![exec_job_2](../Evidências/exec_suced_job2.png)

Arquivos gerados no S3

![arq_s3_job2](../Evidências/arq_tmdb_gerados.png)

### Catalogando os dados

Criando Crawler para o Primeiro Job do CSV

![config_crawler](../Evidências/criando_crawler1.png)

Abrindo o Athena, foi criado a tabela local

![2_tables](../Evidências/tables_criadas.png)

Colunas da tabela local:

![local_table1](../Evidências/local_table1.png)

![local_table2](../Evidências/local_table2.png)


Consulta das primeiras 10 linhas da tabela local:

![consulta_local](../Evidências/consulta_local.png)


Criando Crawler para o segundo Job de JSON

![criando_crawler2](../Evidências/criando_crawler2.png)

Colunas da tabela tmdb:

![tmdb_table](../Evidências/tmdb_table.png)


Consulta das primeiras 10 linhas da tabela tmdb:

![consulta_tmdb](../Evidências/consulta_tmdb.png)


