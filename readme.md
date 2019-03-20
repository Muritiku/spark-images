# Spark based images
**by Anton Dziavitsyn 2019**  
[a.dziavitsyn@gmail.com](mailto:a.dziavitsyn@gmail.com)  
  
Repository on GitHub: [https://github.com/Muritiku/spark-images](https://github.com/Muritiku/spark-images)  
  
Content:
+ Spark Cluster Images
+ Spark virtual datasource image (provide ODBC/JDBC access to schema created by tasks - look at description & examples below)
+ Jupyter LAB with pyspark image (compatible with cluster images to connect)

## DockerHub builded images links (look at using examples below)
+ [muritiku/spark-base](https://hub.docker.com/r/muritiku/spark-base)
+ [muritiku/spark-master](https://hub.docker.com/r/muritiku/spark-master)
+ [muritiku/spark-worker](https://hub.docker.com/r/muritiku/spark-worker)
+ [muritiku/spark-jupyter](https://hub.docker.com/r/muritiku/spark-jupyter)
+ [muritiku/spark-virtual-datasource](https://hub.docker.com/r/muritiku/spark-virtual-datasource)
  
## Introduction
These centos 7 based images, contain Spark+Hadoop for standalone cluster creation, with additions:
+ Java 1.8 openjdk
+ anaconda 3.7 (with numpy, scipy, matplotlib etc...)
  
## Spark Cluster creation example
Here the example of cluster compose file `./spark-cluster.yml`:
```yaml
version: '3.2'

# by Anton Dziavitsyn
# spark cluster compose example

services:
  spark-master:
    image: muritiku/spark-master
    ports:
      - "8080:8080"
      - "4040:4040"
      - "7077:7077"
    networks:
      spark-network:
        aliases:
          - spark-master

  spark-worker-1:
    image: muritiku/spark-worker
    depends_on:
      - spark-master
    ports:
      - "8081:8081"
      - "4041:4041"
      - "7078:7078"
    environment:
      - SPARK_MASTER=spark://spark-master:7077
    depends_on:
      - 'spark-master'
    networks:
      spark-network:
        aliases:
          - spark-worker-1

networks:
  spark-network:
    # driver: overlay # for docker stack deploy

```
  
## Using of spark-jupyter image
  
Run image with notebooks in current directory by command:
```bash
docker run --name spark-jupyter -p 8888:8888 -v ${PWD}:/home/jupyter muritiku/spark-jupyter
```
NOTE: *If you want to connect to spark cluster - use* `--network host` *instead of* `-p 8888:8888`
  
Open Jupyter Lab in web browser: [http://localhost:8888](http://localhost:8888)  
  
Test example for spark:
```python
#Spark test

import findspark
findspark.init()

from pyspark.sql import SparkSession
import random

# for local spark core test
spark = SparkSession.builder.appName('local-test').getOrCreate()
# for spark cluster core test
#spark = SparkSession.builder.appName('cluster-test').master('spark://[SPARK MASTER URL]:7077').getOrCreate()
sc = spark.sparkContext

# Calculate Pi with distributed computing
num_samples = 100000
def inside(p):     
  x, y = random.random(), random.random()
  return x*x + y*y < 1

count = sc.parallelize(range(0, num_samples)).filter(inside).count()
pi = 4 * count / num_samples
print(pi)

# SQL context test
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

df = spark.sql('''select 'spark' as hello ''')
df.show()
```
  
## Using of spark-virtual-datasource image (virtual JDBC/ODBC datasource)
  
This is not final version - I am working to expand its functionality and config options. Ready for your proposals.  

**How it works?**  
It generates sql (hive2) schema, by running tasks, and gives access to it by ODBC/JDBC (default port 10000) with using Spark thrift/hive2 jdbc driver.  
Then it may be used as a consolidated SQL datasource (from many sources), for your applications.  
  
**How to expand schema?**  
You can add new views to schema, by adding new task modules. (look into examples in /spark-virtual-datasource/tasks directory)
Your task module should implement one method:
```python
def task(sparkContext, sparkSession):
    # code
```
  
**How to run the image?**  
To run in with example tasks - just run command in repository root:
```bash
docker run --name spark-datasource -p 10000:10000 -v ${PWD}/spark-virtual-datasource/tasks:/spark_tasks/tasks muritiku/spark-virtual-datasource
```
**NOTE:** You may attach your tasks directory, by changing `${PWD}/spark-virtual-datasource/tasks` to it's location.  
  
Now You can connect to datasource by ODBC/JDBC port 10000 with using Spark thrift/hive2 driver.  By SQL command `SHOW TABLES` - you will get your generated views.  
  
**How to stop the server?**  
Just stop the container in separate bash session:
```bash
docker stop spark-datasource
```

