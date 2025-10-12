
"""
input -
col1    col2    col3
A       AA      1
A       AA      2
A       AA      3
B       BB      1
B       BB      2
B       BB      3
B       BB      4
C       CC      1
"""

"""
output -

col1    col2    col3
A       AA      [1, 2, 3,]
B       BB      [1, 2, 3, 4]
C       CC      [1]
"""

from pyspark.sql import SparkSession, functions as f


def aggregate():
    spark = SparkSession.builder.appName("Aggregate").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    schema = ["col1", "col2", "col3"]
    data = [
        ["A", "AA", 1],
        ["A", "AA", 2],
        ["A", "AA", 3],
        ["B", "BB", 1],
        ["B", "BB", 2],
        ["B", "BB", 3],
        ["B", "BB", 4],
        ["C", "CC", 1],
    ]
    df = spark.createDataFrame(data=data,schema=schema)

    df.show()

    df = df.groupBy("col1", "col2").agg(
        f.collect_list("col3").alias("col3")
    )

    df.show()
    spark.stop()


if __name__ == '__main__':
    aggregate()