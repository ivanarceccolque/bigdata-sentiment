Análisis de Sentimiento en Tweets  — Pipeline de Big Data
Este proyecto implementa un pipeline de Big Data para procesar tweets en español y analizar el sentimiento expresado en cada uno. Utiliza herramientas modernas como Apache Kafka, PySpark y MongoDB Atlas, y está diseñado para ejecutarse completamente en Google Colab.

Resumen del Pipeline
El flujo de datos sigue esta secuencia:
- Ingesta: Lectura de tweets desde un archivo CSV
- Simulación de streaming: Envío de datos mediante Kafka
- Procesamiento distribuido: Limpieza, codificación y enriquecimiento con PySpark
- Almacenamiento NoSQL: Inserción de datos procesados en MongoDB Atlas
- Exploración visual: Validación de calidad y distribución de datos en notebooks

📁 Estructura del Proyecto
bigdata-sentiment/
├── data/
│   └── tweets.csv
├── src/
│   ├── kafka_producer.py
│   ├── process_tweets.py
│   └── mongo_writer_pymongo.py
├── notebooks/
│   └── exploratory_analysis.ipynb
├── config/
│   └── spark_config.json
├── requirements.txt
└── README.md

🚀 Ejecución del Proyecto en Google Colab
1. Abrir un notebook en Colab
- Ve a Google Colab
- Crea un nuevo notebook
- Renómbralo como pipeline_sentiment_analysis.ipynb
2. Cargar la estructura del proyecto
- Sube los archivos y carpetas del proyecto a tu entorno de Colab
- Asegúrate de que el archivo tweets.csv esté en la carpeta /content/data/
3. Instalar dependencias
- Instala Java y las librerías necesarias usando comandos en celdas
- Configura la variable de entorno JAVA_HOME para que PySpark funcione correctamente
4. Importar librerías y configurar Spark
- Importa pyspark, pandas, matplotlib, seaborn, pymongo, y kafka-python
- Crea una sesión de Spark con nombre personalizado
5. Cargar y explorar el dataset
- Usa pandas para visualizar las primeras filas del archivo CSV
- Ejecuta el notebook exploratory_analysis.ipynb para ver:
- Distribución de sentimientos
- Limpieza de texto
- Longitud de tweets
- Palabras frecuentes
6. Procesar los tweets con PySpark
- Ejecuta el script process_tweets.py o copia su contenido en una celda
- Este script realiza:
- Limpieza de texto
- Tokenización
- Codificación de sentimiento
- Enriquecimiento con fecha y longitud
7. Guardar los datos en MongoDB Atlas

🔐 Crear una cuenta en MongoDB Atlas
- Ve a MongoDB Atlas
- Regístrate y crea un clúster gratuito
- Crea una base de datos llamada tweets_db y una colección llamada processed
- En Network Access, agrega la IP 0.0.0.0/0 para permitir acceso desde Colab
- En Database Access, crea un usuario con permisos de lectura y escritura
🔗 Obtener tu URI de conexión
- Copia el URI de conexión que MongoDB Atlas te proporciona
- Reemplaza <password> por tu contraseña real
- Asegúrate de incluir el nombre de la base de datos en el URI
🗃️ Ejecutar el script de almacenamiento
- Ejecuta el script mongo_writer_pymongo.py en una celda
- Este script:
- Verifica la conexión con MongoDB Atlas
- Convierte los datos procesados en diccionarios
- Inserta los documentos en la colección processed

✅ Requisitos
- Python 3.10+
- Google Colab o entorno local con PySpark
- Cuenta activa en MongoDB Atlas
- Conexión a internet

📚 Créditos
- Dataset: Kaggle — Tweets en español con etiquetas de sentimiento
- Herramientas: Apache Spark, Kafka, MongoDB Atlas, PyMongo, Google Colab
- Autor: Iván Arce Ccolque

codigo directo en colab.  https://colab.research.google.com/drive/1GOqFjFuMOEHC6Box-DS5zBlfJ3_13g6L?usp=sharing
