import sys
import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, upper, when

# Obtive argumentos do AWS Glue Job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_PATH', 'OUTPUT_PATH'])

# Converti a string de caminhos em uma lista
json_paths = args['INPUT_PATH'].split(',')
parquet_base_path = args['OUTPUT_PATH']

# Inicializei Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Obtive data da execução para criar diretórios no formato correto
today = datetime.datetime.now()
ano, mes, dia = today.strftime("%Y"), today.strftime("%m"), today.strftime("%d")

# Criei um DynamicFrame para cada JSON e apliquei transformações
dataframes = []
for path in json_paths:
    dynamic_frame = glueContext.create_dynamic_frame.from_options(
        format_options={"multiline": True},
        connection_type="s3",
        format="json",
        connection_options={"paths": [path], "recurse": True}
    )

    df = dynamic_frame.toDF()

    # Apliquei transformações
    df = df.withColumn("anoLancamento", when(col("anoLancamento") == "", "Desconhecido")
                                       .otherwise(col("anoLancamento").cast("int")))
    df = df.withColumn("numeroEpisodios", when(col("numeroEpisodios").isNull(), 0)
                                         .otherwise(col("numeroEpisodios").cast("int")))
    df = df.withColumn("estudio", when(col("estudio") == "N/A", "Desconhecido")
                                  .otherwise(col("estudio")))
    df = df.withColumn("tituloOriginal", upper(col("tituloOriginal")))
    df = df.withColumn("estudio", upper(col("estudio")))

    dataframes.append(df)

# Uni todos os DataFrames
df_final = dataframes[0]
for df in dataframes[1:]:
    df_final = df_final.unionByName(df)

# Converti para DynamicFrame
transformed_dynamic_frame = DynamicFrame.fromDF(df_final, glueContext, "transformed_df")

# Caminho final seguindo o padrão estabelecido
final_path = f"{parquet_base_path}/TMDB/Parquet/Series/{ano}/{mes}/{dia}/"

# Salvando como Parquet no S3
glueContext.write_dynamic_frame.from_options(
    frame=transformed_dynamic_frame,
    connection_type="s3",
    format="parquet",
    connection_options={"path": final_path} 
)

print(f"Processamento concluído! Dados salvos em: {final_path}")

# Finalizando o job
job.commit()
