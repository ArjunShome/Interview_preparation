
from pyspark.sql import SparkSession, functions as f

def aggregate():
    spark = SparkSession.builder.appName("Aggregate").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    json_file_path = "/Users/arjunshome/personal/Projects/Interview_preparation/Projects/Data_Engineering/PySpark_practice/Datasets/data.json"
    json_write_path = "/Users/arjunshome/personal/Projects/Interview_preparation/Projects/Data_Engineering/PySpark_practice/Datasets/data_1.json"
    df = spark.read.json(path=json_file_path)
    df.show()
    m = df.select("dept_id", f.explode("e_id").alias("emp_id"))
    m.show()
    m = m.groupBy("dept_id").agg(f.collect_list("emp_id").alias("emp_id"))
    m.write.json(path=json_write_path, mode="overwrite")
    spark.stop()






if __name__ == '__main__':
    aggregate()