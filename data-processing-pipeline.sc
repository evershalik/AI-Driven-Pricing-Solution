// Real-time CDR processing for dynamic pricing
val cdrStream = spark
  .readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "kafka-cluster:9092")
  .option("subscribe", "cdr-events,network-metrics,competitor-pricing")
  .load()

val processedStream = cdrStream
  .select(from_json(col("value"), cdrSchema).as("data"))
  .select("data.*")
  .groupBy(window(col("timestamp"), "5 minutes"), col("cell_id"))
  .agg(
    avg("data_usage").as("avg_usage"),
    count("*").as("connection_count"),
    sum("revenue").as("total_revenue")
  )
  .writeStream
  .outputMode("update")
  .format("delta")
  .option("checkpointLocation", "/checkpoints/cdr-processing")
  .start()
