from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType,IntegerType, TimestampType
from pyspark.sql.functions import from_json,col, to_timestamp, date_format

spark = SparkSession \
    .builder \
    .appName("SSKafka") \
    .config("spark.jars.packages","org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

reviewsSchema = StructType([
                  StructField("name", StringType(),False),
                  StructField("movie", StringType(),False),
                  StructField("date", StringType(),False),
                  StructField("rating", IntegerType(),False)])

df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:29092") \
  .option("subscribe", "test") \
  .option("startingOffsets", "latest") \
  .load() 

# Parse the stream data
parsed_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), reviewsSchema).alias("data")) \
    .select("data.*")

# Convert the date string to timestamp
parsed_df = parsed_df.withColumn("time", to_timestamp(col("date"), "yyyy-MM-dd HH:mm:ss"))

# Create the rating_hour column (truncated to hour)
parsed_df = parsed_df.withColumn("hour", 
                                 date_format(col("time"), "yyyy-MM-dd HH:00:00"))
parsed_df = parsed_df.withColumn("hour", to_timestamp(col("hour"), "yyyy-MM-dd HH:mm:ss"))

# This is the key fix - select only the columns that exist in your Cassandra table
final_df = parsed_df.select("name", "movie", "rating", "time", "hour")


def writeToCassandra(writeDF, _):
  writeDF.write.format("org.apache.spark.sql.cassandra").mode('append').options(table="records", keyspace="reviews").save()

# Process interval in seconds
processing_interval = 30 

result = None
while result is None:
  try:
    # connect
    result = final_df.writeStream.option("spark.cassandra.connection.host","localhost:9042") \
      .foreachBatch(writeToCassandra) \
      .outputMode("update") \
      .trigger(processingTime=f"{processing_interval} seconds") \
      .start() \
      .awaitAnyTermination()
  except KeyboardInterrupt:
    result.stop()
    break
  except:
    pass
