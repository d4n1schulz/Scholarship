import sys
import re
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, upper, when

# Obtive argumentos do AWS Glue Job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_PATH', 'TARGET_PATH'])

# Converti a string de caminhos em uma lista
json_paths = args['INPUT_PATH'].split(',')
parquet_base_path = args['TARGET_PATH']

# Inicializei Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Função para extrair a data do caminho do arquivo
def extract_date_from_path(path):
    match = re.search(r'(\d{4})/(\d{2})/(\d{2})/', path)
    if match:
        return match.group(1), match.group(2), match.group(3)
    else:
        raise ValueError("Data não encontrada no caminho do arquivo")

# Processar cada arquivo JSON individualmente
for path in json_paths:
    # Extrai a data do caminho do arquivo
    ano, mes, dia = extract_date_from_path(path)
    
    # Cria um DynamicFrame a partir do JSON
    dynamic_frame = glueContext.create_dynamic_frame.from_options(
        format_options={"multiline": True},
        connection_type="s3",
        format="json",
        connection_options={"paths": [path], "recurse": True}
    )

    # Converte para DataFrame
    df = dynamic_frame.toDF()

    # Aplica transformações
    df = df.withColumn("anoLancamento", when(col("anoLancamento") == "", "Desconhecido")
                                       .otherwise(col("anoLancamento").cast("int")))
    df = df.withColumn("numeroEpisodios", when(col("numeroEpisodios").isNull(), 0)
                                         .otherwise(col("numeroEpisodios").cast("int")))
    df = df.withColumn("estudio", when(col("estudio") == "N/A", "Desconhecido")
                                  .otherwise(col("estudio")))
    df = df.withColumn("tituloOriginal", upper(col("tituloOriginal")))
    df = df.withColumn("estudio", upper(col("estudio")))

    # Converte de volta para DynamicFrame
    transformed_dynamic_frame = DynamicFrame.fromDF(df, glueContext, "transformed_df")

    # Cria o caminho de saída com base na data extraída
    final_path = f"{parquet_base_path}/TMDB/Parquet/Series/{ano}/{mes}/{dia}/"

    # Salva como Parquet no S3
    glueContext.write_dynamic_frame.from_options(
        frame=transformed_dynamic_frame,
        connection_type="s3",
        format="parquet",
        connection_options={"path": final_path} 
    )

# Finalizando o job
job.commit()