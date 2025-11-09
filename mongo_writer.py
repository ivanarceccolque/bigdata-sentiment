from pyspark.sql import SparkSession

# Inicializar Spark
spark = SparkSession.builder \
    .appName("GuardarEnMongo") \
    .config("spark.mongodb.output.uri", "mongodb://localhost:27017/tweets_db.processed") \
    .getOrCreate()

# Cargar DataFrame procesado (puede venir del script anterior)
df = spark.read.csv("data/tweets.csv", header=True, inferSchema=True)

# Procesamiento básico (puedes importar funciones del script anterior)
df = df.withColumn("sentiment_numeric",
    when(col("sentiment") == "positive", 1)
    .when(col("sentiment") == "negative", -1)
    .otherwise(0)
)

# Guardar en MongoDB
df.write \
    .format("mongo") \
    .mode("append") \
    .save()
