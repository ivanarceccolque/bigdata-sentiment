from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, to_date, regexp_replace, lower, when

# Inicializar Spark
spark = SparkSession.builder.appName("ProcesamientoTweets").getOrCreate()

# Leer datos simulados desde CSV (puede adaptarse a Kafka si se usa streaming)
df = spark.read.csv("data/tweets.csv", header=True, inferSchema=True)

# Limpieza de texto
df_clean = df.withColumn("text_clean", lower(col("text")))
df_clean = df_clean.withColumn("text_clean", regexp_replace("text_clean", r"http\S+", ""))
df_clean = df_clean.withColumn("text_clean", regexp_replace("text_clean", r"@\w+", ""))
df_clean = df_clean.withColumn("text_clean", regexp_replace("text_clean", r"[^\w\s]", ""))
df_clean = df_clean.withColumn("text_clean", regexp_replace("text_clean", r"\s+", " "))

# Tokenización simple (puede usarse NLP más avanzado si se desea)
df_clean = df_clean.withColumn("tokens", regexp_replace(col("text_clean"), " ", ","))

# Codificación de sentimiento
df_clean = df_clean.withColumn("sentiment_numeric",
    when(col("sentiment") == "positive", 1)
    .when(col("sentiment") == "negative", -1)
    .otherwise(0)
)

# Agregar fecha y longitud
df_clean = df_clean.withColumn("date_formatted", to_date(col("date"), "yyyy-MM-dd"))
df_clean = df_clean.withColumn("text_length", length(col("text_clean")))

# Mostrar resultados
df_clean.select("id", "text_clean", "tokens", "sentiment_numeric", "date_formatted", "text_length").show(10, truncate=False)