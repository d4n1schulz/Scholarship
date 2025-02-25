import boto3
import os
from datetime import datetime


session = boto3.Session(profile_name="daniel.schulz")  
s3 = session.client('s3')


file1_path = 'movies.csv'
file2_path = 'series.csv'


bucket_name = 'daniel-schulz-datalake'


origem_dado = 'Raw'  
formato_dado = 'CSV'  


especificacao_dado1 = 'Movies' 
especificacao_dado2 = 'Series'  


data_processamento = datetime.now().strftime('%Y/%m/%d')


def criar_nome_arquivo(file_path):
    nome_arquivo = os.path.basename(file_path)
    return nome_arquivo


def upload_arquivo_s3(file_path, especificacao_dado):
    nome_arquivo = criar_nome_arquivo(file_path)

    caminho_s3 = f"{origem_dado}/Local/{formato_dado}/{especificacao_dado}/{data_processamento}/{nome_arquivo}"

    try:
        with open(file_path, 'rb') as file:
            s3.put_object(Bucket=bucket_name, Key=caminho_s3, Body=file)
            print(f"Arquivo '{nome_arquivo}' enviado para o S3 no caminho: {caminho_s3}")
    except Exception as e:
        print(f"Erro ao enviar arquivo '{nome_arquivo}': {e}")


upload_arquivo_s3(file1_path, especificacao_dado1)
upload_arquivo_s3(file2_path, especificacao_dado2)
