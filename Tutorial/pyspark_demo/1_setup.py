from pyspark.sql import SparkSession 

from pyspark.sql.types import (
    StructType, StructField,
    StringType, IntegerType, DoubleType, DateType, BooleanType,
)




# Create (or reuse) a local Spark session using all available CPU cores
spark = (
    SparkSession.builder
    .appName("pyspark_demo")
    .master("local[*]")
    .config("spark.sql.shuffle.partitions", "4")  # default 200 is overkill locally
    .getOrCreate()
) 

full_schema = StructType([
    StructField("year", IntegerType(), nullable=True),
    StructField("topic", StringType(), nullable=True)
])

df_seminar=spark.read.csv("data/seminars.csv",header=True, schema=full_schema)
df_seminar.show() 

df=spark.createDataFrame([(2020,"Data Science"),(2021,"Machine Learning"), (2022, "Deep Learning")],schema=full_schema)
df.show()
spark.sparkContext.setLogLevel("WARN")

print(f"Spark version: {spark.version}")
print(f"Spark UI: {spark.sparkContext.uiWebUrl}")
input("Spark UI is live — press Enter to stop Spark...")
spark.stop()
# Quick sanity check
#spark.range(5).show()

