from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType,IntegerType
from pyspark.sql.functions import split,from_json,col, monotonically_increasing_id, to_timestamp

spark = SparkSession \
    .builder \
    .appName("SSKafka") \
    .config("spark.jars.packages","org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

reviewsSchema = StructType([
                StructField("id", IntegerType(),False),
                StructField("name", StringType(),False),
                StructField("movie", StringType(),False),
                StructField("date", StringType(),False),
                StructField("rating", IntegerType(),False)
            ])

df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:29092") \
  .option("subscribe", "test") \
  .option("startingOffsets", "latest") \
  .load() 

sdf = df.selectExpr("CAST(value AS STRING)") \
  .select(from_json(col("value"), reviewsSchema).alias("data")) \
  .select("data.*") \
  .withColumn("date", to_timestamp(col("date"), "yyyy-MM-dd HH:mm:ss"))

def writeToCassandra(writeDF, _):
  writeDF.write.format("org.apache.spark.sql.cassandra").mode('append').options(table="records", keyspace="reviews").save()

result = None
while result is None:
  try:
    # connect
    result = sdf.writeStream.option("spark.cassandra.connection.host","localhost:9042") \
      .foreachBatch(writeToCassandra) \
      .outputMode("update") \
      .trigger(processingTime='30 seconds') \
      .start() \
      .awaitAnyTermination()
  except:
    pass
  