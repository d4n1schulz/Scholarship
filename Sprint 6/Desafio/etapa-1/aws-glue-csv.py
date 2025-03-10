import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col

# Obtive os parâmetros passados ao job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicializei o contexto do Spark e do Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Defini os caminhos de entrada e saída a partir dos parâmetros
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Fiz a leitura dos dados do S3
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {"paths": [source_file]},
    "csv",
    {"withHeader": True, "separator": "|"}
)

# Converti o DynamicFrame para DataFrame do Spark
df = df.toDF()

# Corrigi o nome da coluna
df = df.withColumnRenamed("tituloPincipal", "tituloPrincipal")

# Converti colunas para numéricas
df = df.withColumn("anoLancamento", col("anoLancamento").cast("int"))
df = df.withColumn("anoTermino", col("anoTermino").cast("int"))
df = df.withColumn("tempoMinutos", col("tempoMinutos").cast("int"))
df = df.withColumn("anoNascimento", col("anoNascimento").cast("int"))
df = df.withColumn("anoFalecimento", col("anoFalecimento").cast("int"))
df = df.withColumn("numeroVotos", col("numeroVotos").cast("int"))
df = df.withColumn("notaMedia", col("notaMedia").cast("int"))

# Removi duplicatas
df = df.dropDuplicates()

# Salvei os dados filtrados no S3 no formato Parquet (usando Spark diretamente)
df.write.mode("overwrite").parquet(target_path)

# Finalizei o job
job.commit()
