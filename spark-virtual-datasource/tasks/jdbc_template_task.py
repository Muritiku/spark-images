from pyspark.sql import SQLContext
import pyspark.sql.functions as f

# Need to implement this method for task_runner
def task(sparkContext, sparkSession):

    sc = sparkContext
    spark = sparkSession
    sqlContext = SQLContext(sc)

    def create_tmp_view(table_name, query):
        # data provider JDBC connection
        df = sqlContext.read.format("jdbc")\
        .option("url", "<JDBC connection string>")\
        .option("driver", "<JDBC driver class>")\
        .option("schema", "<SHEMA_NAME>")\
        .option("dbtable", "({}) result".format(query))\
        .load()
        
        df.createOrReplaceTempView(table_name)
        sqlContext.cacheTable(table_name)
        df.unpersist()
    
    # To create view based on query just call this method
    # create_tmp_view("<VIEW NAME>", "<QUERY TO DATA PROVIDER>")