import pyspark.sql
from pyspark.sql import SparkSession, functions as f, Window

class ETL:
    def __init__(self, source: str, dest: str):
        self.source = source
        self.destination = dest
        self.spark = SparkSession.getActiveSession() or (
            SparkSession.builder.appName("etl").getOrCreate()
        )
        self.spark.sparkContext.setLogLevel("ERROR")

    def extract_data(self):
        movies_df = self.spark.read.csv(self.source, header=True, inferSchema=True)
        return movies_df

    def transform_data(self, movies_data: pyspark.sql.DataFrame):
        # Use select() to get only Title, Genre, ReleaseYear.
        movies_data.select("Title", "Genre", "ReleaseYear").show(10)

        # Use selectExpr() to:
	    #     Compute profit = Global_BoxOfficeUSD - BudgetUSD.
	    #     Extract year from ReleaseDate.
        movies_data = movies_data.withColumn("ReleaseDate", f.to_date("ReleaseDate", "dd-MM-yyyy"))
        movies_data.selectExpr(
            "ROUND(Global_BoxOfficeUSD - BudgetUSD, 2) AS profit",
            "YEAR(ReleaseDate) AS year").show(5)

        movies_data.selectExpr("Global_BoxOfficeUSD AS WorldWideSales", "US_BoxOfficeUSD AS DomesticSales").show(5)

        # Find movies with IMDbRating > 8.5.
        # Find movies where Country == "USA" and BudgetUSD > 100000000.
        movies_data.select("Title", "Director", "IMDbRating").filter(movies_data.IMDbRating > 8.5).show(5)
        movies_data.select("Title", "Director", "IMDbRating", "Country", "BudgetUSD").filter(
            (movies_data.Country == "USA") & (movies_data.BudgetUSD > 100000000)
        ).show(5)

        # Remove duplicates by Title.
        # Show distinct Country values.

        deduped_movie_df = movies_data.dropDuplicates(["Title"])
        deduped_movie_df.show(100)
        print(deduped_movie_df.count())
        print(movies_data.count())

        movies_data.select("Country").distinct().show()

        # Use withColumn() to add a new column ProfitUSD = Global_BoxOfficeUSD - BudgetUSD.
        # Use withColumnRenamed() to rename IMDbRating → IMDB_Score.
        movies_data.withColumn("ProfitUSD", movies_data.Global_BoxOfficeUSD - movies_data.BudgetUSD).show(5)
        movies_data.select("Title", "IMDBRating").withColumnRenamed("IMDbRating", "IMDB_Score").show(5)

        # Add a column Is_HighBudget = True if BudgetUSD > 50M, else False (use when().otherwise()).
        # Add a constant column with lit("Movies Dataset").
        movies_data.withColumn("Is_HighBudget",  f.when(
                                        movies_data.BudgetUSD > 500000, "True").otherwise("False")
                               ).show(5)
        movies_data.withColumn("DatasetType", f.lit("Movies Dataset")).show(5)

        # Inner join movies with directors_df on Director.
        # Left join movies with actors_df on LeadActor.
        # Try semi join: return only movies that have directors in directors_df.

        director_df = movies_data.select("Director").distinct()
        director_df = director_df.withColumn("DirectorAge", f.floor(f.rand() * 70).cast("int"))
        movies_data.join(director_df, on="Director").select("Director", "Title", "DirectorAge").distinct().show(10)

        actors_df = movies_data.select("LeadActor").distinct()
        actors_df = actors_df.withColumn("ActorAge", f.floor(f.rand() * 50).cast("int"))
        movies_data.join(actors_df, on="LeadActor", how="left").select("Title", "LeadActor", "ActorAge").show(10)

        director_df = director_df.limit(2)
        movies_data.join(director_df, on="Director", how="semi").show(10)

        # Group movies by Director, calculate avg(IMDbRating) and sum(Global_BoxOfficeUSD).
        # Use rollup() on (Country, ReleaseYear) with total sum(Global_BoxOfficeUSD).
        # Use cube() on (Genre, ReleaseYear) for count(MovieID).
        # Pivot: Show avg(IMDbRating) by Genre across ReleaseYear.

        movies_data.groupBy("Director").agg(
            f.avg("IMDbRating").alias("IMDbRating_AVG"),
            f.round(f.sum("Global_BoxOfficeUSD"), 2).alias("Global_Box_Office_Sum")
        ).show(10)

        movies_data.rollup("Country", "ReleaseYear").sum("Global_BoxOfficeUSD").show()

        movies_data.cube("Genre", "ReleaseYear").agg(
            f.count("MovieID").alias("movie_count")
        ).show(10)

        movies_data.groupBy("Genre").pivot("ReleaseYear").agg(f.avg("IMDbRating")).show()


        # Order by IMDbRating descending.
        # Sort by ProfitUSD ascending.
        movies_data.sort(f.desc("IMDbRating")).show(10)
        movies_data.withColumn("ProfitUSD", movies_data.Global_BoxOfficeUSD - movies_data.BudgetUSD).sort(f.asc("ProfitUSD")).show(10)


        # Use row_number() partitioned by Genre, ordered by IMDbRating desc.
        # Use rank() to rank movies by Global_BoxOfficeUSD.
        # Use lag() to see how much this year’s revenue differs from previous year’s (partitioned by Country).
        # Use cume_dist() for rating distribution.
        w = Window.partitionBy("Genre").orderBy(f.desc("IMDbRating"))
        movies_data.withColumn("row_num",f.row_number().over(w)).show(10)

        w = Window.orderBy(f.desc("Global_BoxOfficeUSD"))
        movies_data.withColumn("Ranked", f.rank().over(w)).show(10)

        yearly_movies_data = movies_data.withColumn("ReleaseDate", f.to_date("ReleaseDate", "yyyy-MM-dd"))
        yearly_movies_data = yearly_movies_data.withColumn("Year", f.year("ReleaseDate"))
        yearly_movies_data = yearly_movies_data.groupBy("Country", "Year").agg(f.sum("Global_BoxOfficeUSD").alias("Revenue"))

        w = Window.partitionBy("Country").orderBy("Year")
        res = (yearly_movies_data
               .withColumn("prev_revenue", f.lag("Revenue").over(w))
               .withColumn("revenue_diff", f.col("Revenue") - f.col("prev_revenue"))
        )
        res.show()

        return res

    def load_data(self, data: pyspark.sql.DataFrame):
        data.write.parquet(destination_path + "movies_country_year_wise_revenue.parquet", mode="overwrite")
        pass


    def execute(self):
        data = self.extract_data()
        data = self.transform_data(data)
        self.load_data(data)
        print("File Saved Succesfully !!!")

    def stop_spark(self):
        self.spark.stop()

if __name__ == '__main__':

    source_path = "/Users/arjunshome/personal/Projects/Interview_preparation/Projects/Data_Engineering/PySpark_practice/Datasets/movies_dataset.csv"
    destination_path = "/Users/arjunshome/personal/Projects/Interview_preparation/Projects/Data_Engineering/PySpark_practice/Datasets/"

    etl = ETL(source_path, destination_path)
    etl.execute()
    etl.stop_spark()
