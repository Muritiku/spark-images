from pyspark.sql import SQLContext
import pyspark.sql.functions as f

# Need to implement this method for task_runner
def task(sparkContext, sparkSession):

    sc = sparkContext
    spark = sparkSession
    sqlContext = SQLContext(sc)

    #generate test view to access by JDBC
    test_frame = spark.createDataFrame([[1,2], [3,4]], ['a', 'b'])
    test_frame.createOrReplaceTempView('test_view')
    sqlContext.cacheTable('test_view')
    test_frame.unpersist()
