import os
import sys
import findspark
findspark.init()

from pyspark import sql
import importlib

spark = sql.SparkSession.builder.appName("JDBC source") \
            .enableHiveSupport() \
            .config('spark.sql.hive.thriftServer.singleSession', True) \
            .getOrCreate()
sc = spark.sparkContext

from py4j.java_gateway import java_import
java_import(sc._gateway.jvm,"")

#Start the Thrift Server with current jvm and session
sc._gateway.jvm.org.apache.spark.sql.hive.thriftserver.HiveThriftServer2.startWithContext(spark._jwrapped)

#EXECUTE tasks from path in parameters
files = [os.path.join(sys.argv[1], f) for f in os.listdir(sys.argv[1]) if os.path.isfile(os.path.join(sys.argv[1], f)) and f.endswith(".py")]

for module in files:
    spec = importlib.util.spec_from_file_location("module.name", module)
    task_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(task_module)
    print('===================================Running task from file: {}=================================='.format(module))
    task_module.task(sc, spark)

print('===================================SCHEMA IS READY==================================')

# Loop with redicing CPU usage
import time
while True:
    time.sleep(9223372036.854775)
