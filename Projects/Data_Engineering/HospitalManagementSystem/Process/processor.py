from pyspark.sql import SparkSession, functions as F, types as T
from log import logger


class Processor:
    KAFKA_BOOTSTRAP='localhost:9092'
    TOPIC='patient_registrations'

    def __init__(self):
        self.spark = (
            SparkSession
            .builder
            .appName("PatientRegStream")
            .master("local[3]")
            .config("spark.streaming.stopGracefullyOnShutdown", "true")
            .config("spark.sql.shuffle.partitions", 2)
            .config("spark.sql.adaptive.enabled", "false")
            .config("spark.jars.packages", ",".join([
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1",
            "org.apache.spark:spark-token-provider-kafka-0-10_2.12:3.5.1",
            "org.apache.commons:commons-pool2:2.11.1",
            'org.mongodb.spark:mongo-spark-connector_2.12:10.5.0']))
            .config("spark.mongodb.write.connection.uri", "mongodb://localhost:27017")
            .getOrCreate()
        )
        self.spark.sparkContext.setLogLevel("ERROR")
        logger.info(f"Spark Session created with version {self.spark.version}")

    def log_batch_raw(self, df, batch_id):
        df = df.persist()
        try:
            for row in df.toLocalIterator():
                logger.info(f"Raw Data Inserted :- {row.asDict(recursive=True)}")
            (df.write
                .format("mongodb")
                .mode("append")
                .option("database", "hospital_management_system")
                .option("collection", "new_registrations_patient")
                .save()
            )
        finally:
            df.unpersist()

    def log_batch_agg(self, df, batch_id):
        df = df.persist()
        try:
            for row in df.toLocalIterator():
                logger.info(f"Aggregated Data Inserted :- {row.asDict(recursive=True)}")
            (df.write
                .format("mongodb")
                .mode("append")
                .option("database", "hospital_management_system")
                .option("collection", "new_registrations_patient_window_agg")
                .save()
            )
        finally:
            df.unpersist()

    def read_stream(self):
        raw = (
            self.spark.readStream
            .format("kafka")
            .option("kafka.bootstrap.servers", self.KAFKA_BOOTSTRAP)
            .option("subscribe", self.TOPIC)
            .option("startingOffsets", "latest")
            .load()
        )

        json_str = raw.select(F.col("value").cast("string").alias("data_json"))

        # How the Raw data looks like / structure how the raw should be parsed
        schema = T.StructType([
            T.StructField("patient_id", T.StringType()),
            T.StructField("patient_name", T.StringType()),
            T.StructField("patient_address", T.StringType()),
            T.StructField("registration_date", T.StringType())
        ])

        # Parsed Raw Data from Kafka
        value_df = json_str.select(F.from_json("data_json", schema).alias("value"))

        # Cleaning Raw data
        cleaned_df = (
            value_df.select("value.*")
            .withColumn("event_ts", F.to_timestamp("registration_date", "yyyy-MM-dd HH:mm:ss"))
            .withColumn("date", F.to_date("event_ts", "yyyy-MM-dd"))
            .dropna(subset=["event_ts"])
            )

        # Aggregating raw data
        agg_df = cleaned_df.withWatermark("event_ts", "30 minute").groupBy(
                F.col("date"),
                F.window(F.col("event_ts"), "20 minute")
            ).agg(F.count("patient_id").alias("patients_registered"))
        
        # Final Aggregations DataFrame
        final_df = agg_df.select(
            F.col("date").alias("Date"), 
            F.col("window.start").alias("From"), 
            F.col("window.end").alias("To"), 
            "patients_registered"
            )
        
        # Insert Aggregated Data into Mongodb
        agg_write = (
            final_df.writeStream
            .foreachBatch(self.log_batch_agg)
            .option("checkpointLocation", "/tmp/pyspark/patients_reg_agg")
            .start()
            )
        
        # Insert Raw Data into Mongodb
        raw_write = (
            value_df.select("value.*").writeStream
            .foreachBatch(self.log_batch_raw)
            .option("checkpointLocation", "/tmp/pyspark/patients_reg_raw")
            .start()
            )
        

        self.spark.streams.awaitAnyTermination()
