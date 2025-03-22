import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from pyspark.sql.functions import col, floor, concat_ws
from pyspark.sql.window import Window
import pyspark.sql.functions as F

# Inicializei o contexto do Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Carreguei dados da camada Trusted
local_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://daniel-schulz-datalake/Trusted/Local/"]},
    format="parquet"
).toDF()

tmdb_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://daniel-schulz-datalake/Trusted/TMDB/"]},
    format="parquet"
).toDF()

# Renomeei colunas da TMDB para match com a Local
tmdb_df = tmdb_df.withColumnRenamed("anoLancamento", "anolancamento") \
                 .withColumnRenamed("imdbRating", "notamedia") \
                 .withColumnRenamed("keywords", "palavras_chave") \
                 .withColumnRenamed("numeroEpisodios", "numeroepisodios")

# Filtrei por gêneros Crime e War
local_df = local_df.filter(
    (col("genero").contains("Crime")) | 
    (col("genero").contains("War"))
)

# Selecionei colunas da TMDB
tmdb_df = tmdb_df.select(
    col("tituloOriginal").alias("titulooriginal"),
    "palavras_chave",
    "estudio",
    "numeroepisodios"
)

# Criei coluna década para facilitar as análises
local_df = local_df.withColumn("decada", (floor(col("anolancamento") / 10) * 10))

# Selecionei colunas da Local
local_df = local_df.select(
    "tituloprincipal",
    "titulooriginal",
    "genero",
    "anolancamento",
    "decada",
    "notamedia",
    "numerovotos",
).dropDuplicates()

# Join com colunas unificadas
merged_df = local_df.join(
    tmdb_df,
    "titulooriginal",
    "inner"
)


# Aqui gerei IDs para dimensões com valores distintos


# Dimensão Estúdio
dim_estudio_df = merged_df.select("estudio").distinct()
dim_estudio_df = dim_estudio_df.withColumn("id_estudio", F.row_number().over(Window.orderBy("estudio")))

# Dimensão Tempo
dim_tempo_df = merged_df.select("anolancamento", "decada").distinct()
dim_tempo_df = dim_tempo_df.withColumn("id_tempo", F.row_number().over(Window.orderBy("anolancamento")))

# Dimensão Palavras-Chave
dim_palavras_chave_df = merged_df.select("palavras_chave").distinct()
dim_palavras_chave_df = dim_palavras_chave_df.withColumn(
    "palavras_chave_str", concat_ws(",", col("palavras_chave"))
).withColumn(
    "id_palavras_chave", F.row_number().over(Window.orderBy("palavras_chave_str"))
)

# Dimensão Série
dim_serie_df = merged_df.select("tituloprincipal", "titulooriginal", "genero").distinct()
dim_serie_df = dim_serie_df.withColumn("id_serie", F.row_number().over(Window.orderBy("titulooriginal")))


# Associei IDs de dimensões ao DataFrame principal


merged_df = merged_df.join(dim_estudio_df, "estudio", "inner")
merged_df = merged_df.join(dim_tempo_df, ["anolancamento", "decada"], "inner")
merged_df = merged_df.join(dim_palavras_chave_df, "palavras_chave", "inner")
merged_df = merged_df.join(dim_serie_df, ["tituloprincipal", "titulooriginal", "genero"], "inner")


# Criei tabela fato


merged_df = merged_df.withColumn("id_fato", F.row_number().over(Window.orderBy("titulooriginal")))
fato_df = merged_df.select(
    "id_fato",
    "id_serie",
    "id_tempo",
    "id_estudio",
    "id_palavras_chave",
    "notamedia",
    "numerovotos",
    "numeroepisodios"
)


# Salvei dados na camada Refined


glueContext.write_dynamic_frame.from_options(
    frame=DynamicFrame.fromDF(fato_df, glueContext, "fato_df"),
    connection_type="s3",
    connection_options={"path": "s3://daniel-schulz-datalake/Refined/fato/"},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=DynamicFrame.fromDF(dim_serie_df, glueContext, "dim_serie_df"),
    connection_type="s3",
    connection_options={"path": "s3://daniel-schulz-datalake/Refined/dim_serie/"},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=DynamicFrame.fromDF(dim_tempo_df, glueContext, "dim_tempo_df"),
    connection_type="s3",
    connection_options={"path": "s3://daniel-schulz-datalake/Refined/dim_tempo/"},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=DynamicFrame.fromDF(dim_estudio_df, glueContext, "dim_estudio_df"),
    connection_type="s3",
    connection_options={"path": "s3://daniel-schulz-datalake/Refined/dim_estudio/"},
    format="parquet"
)

glueContext.write_dynamic_frame.from_options(
    frame=DynamicFrame.fromDF(dim_palavras_chave_df, glueContext, "dim_palavras_chave_df"),
    connection_type="s3",
    connection_options={"path": "s3://daniel-schulz-datalake/Refined/dim_palavras_chave/"},
    format="parquet"
)

job.commit()