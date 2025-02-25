import json
import os
import boto3
import requests
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

API_KEY = os.getenv("TMDB_API_KEY")  
BUCKET_NAME = os.getenv("BUCKET_NAME")  

BASE_URL = "https://api.themoviedb.org/3"


s3 = boto3.client("s3")


ORIGEM_DADO = "Raw"
ESPECIFICACAO_DADO = "TMDB"
FORMATO_DADO = "JSON"
DATA_PROCESSAMENTO = datetime.now().strftime("%Y/%m/%d")

def get_series_details(tmdb_id):
    """Busca detalhes de uma série pelo ID no TMDB."""
    url = f"{BASE_URL}/tv/{tmdb_id}"
    params = {"api_key": API_KEY}
    
    try:
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()

            
            estudio = "N/A"
            if "networks" in data and data["networks"]:
                estudio = data["networks"][0].get("name", "N/A")
            elif "production_companies" in data and data["production_companies"]:
                estudio = data["production_companies"][0].get("name", "N/A")

            return {
                "id": data.get("id"),
                "tituloOriginal": data.get("name"),
                "anoLancamento": data.get("first_air_date", "N/A")[:4],
                "imdbRating": data.get("vote_average"),
                "status": data.get("status"),
                "estudio": estudio,
                "numeroEpisodios": data.get("number_of_episodes", "N/A"),
            }
        else:
            print(f"Erro ao buscar ID {tmdb_id}: {response.status_code}")
    except requests.RequestException as e:
        print(f"Erro na requisição {tmdb_id}: {e}")
    
    return None

def get_war_series():
    
    url = f"{BASE_URL}/discover/tv"
    params = {
        "api_key": API_KEY,
        "with_genres": "10768",
        "page": 1
    }

    all_series = []
    while True:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            total_pages = data.get("total_pages", 1)

            for page in range(1, total_pages + 1):
                params["page"] = page
                response = requests.get(url, params=params)
                if response.status_code == 200:
                    all_series.extend(response.json().get("results", []))
                else:
                    break
        else:
            print(f"Erro ao buscar séries de guerra: {response.status_code}")
            break

        
        if len(all_series) < data["total_results"]:
            params["page"] += 1
        else:
            break
    
    return all_series

def lambda_handler(event, context):
    """Função principal do AWS Lambda."""
    
    series_data = get_war_series()
    print(f"Total de séries encontradas: {len(series_data)}")

    tmdb_ids = [serie["id"] for serie in series_data]

    detailed_data = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_id = {executor.submit(get_series_details, tmdb_id): tmdb_id for tmdb_id in tmdb_ids}
        for future in as_completed(future_to_id):
            result = future.result()
            if result:
                detailed_data.append(result)

    
    file_name = "war_series_all_time.json"

    
    s3_key = f"{ORIGEM_DADO}/{ESPECIFICACAO_DADO}/{FORMATO_DADO}/{DATA_PROCESSAMENTO}/{file_name}"
    
    
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=s3_key,
        Body=json.dumps(detailed_data, ensure_ascii=False, indent=4),
        ContentType="application/json"
    )

    return {
        "statusCode": 200,
        "body": f"Arquivo '{file_name}' salvo no bucket '{BUCKET_NAME}' no caminho '{s3_key}'"
    }
