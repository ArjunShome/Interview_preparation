data = [
    ("2023-01-01", "AAPL", 150.00),
    ("2023-01-02", "AAPL", 155.00),
    ("2023-01-01", "GOOG", 2500.00),
    ("2023-01-02", "GOOG", 2550.00),
    ("2023-01-01", "MSFT", 300.00),
    ("2023-01-01", "MSFT", 310.00),
]

from pyspark.sql import SparkSession, functions as f

def transform():
    spark = SparkSession.builder.appName("Transform").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    df = spark.createDataFrame(data=data, schema=["date", "co", "st_val"])
    df.show()
    df_average = df.groupBy("co","date").agg(f.avg("st_val").alias("average_st_price"))
    df = df.join(df_average, on=["co", "date"])
    df_max = df.groupBy("co").agg(f.max("average_st_price").alias("max_st_price"))
    df = df.join(df_max, on="co")
    df.show()
    df_max.show()
    spark.stop()



if __name__ == '__main__':
    transform()