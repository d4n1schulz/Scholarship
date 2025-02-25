FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install boto3

RUN mkdir -p /app/data

COPY movies.csv series.csv /app/data/

VOLUME /app/data

CMD ["python", "etapa1.py"]