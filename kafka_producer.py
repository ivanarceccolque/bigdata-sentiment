from kafka import KafkaProducer
import time
import json
import pandas as pd

# Cargar el dataset
df = pd.read_csv('data/tweets.csv')  # Asegúrate de tener este archivo en tu carpeta 'data'

# Inicializar el productor Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Enviar tweets uno por uno
for _, row in df.iterrows():
    tweet = {
        "id": int(row['id']),
        "text": str(row['text']),
        "sentiment": str(row['sentiment']),
        "date": str(row['date'])
    }
    producer.send('tweets', value=tweet)
    print(f"Enviado: {tweet}")
    time.sleep(1)  # Simula streaming con 1 segundo de intervalo

producer.flush()
producer.close()