from pyspark.sql import SparkSession, functions as f

def check_partitions():
    spark = SparkSession.builder.appName("Partition").getOrCreate()
    csv_path = "/Users/arjunshome/personal/Projects/Interview_preparation/Projects/Data_Engineering/PySpark_practice/Datasets/movies_dataset.csv"
    df = spark.read.csv(path=csv_path, inferSchema=True, header=True)
    print(df.rdd.getNumPartitions())
    print(df.count())
    df.select(f.spark_partition_id().alias("partitions")).groupBy("partitions").count().alias("row_counts").show()
    df = df.repartition(20)
    print(df.rdd.getNumPartitions())
    df.select(f.spark_partition_id().alias("partitions")).groupBy("partitions").count().alias("row_counts").show()
    df.write.bucketBy(4, "MovieID").sortBy("MovieID").mode("overwrite").saveAsTable("Arjun")
    df = spark.table("Arjun")
    df.show()



if __name__=='__main__':
    check_partitions()