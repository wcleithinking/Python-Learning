"""SimpleApp.py"""
from pyspark.sql import SparkSession

logFile = "/home/wenchao/Documents/Spark/README.md"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, line with b: %i" % (numAs, numBs))

spark.stop()
