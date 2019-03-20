# Spark based images
**by Anton Dziavitsyn 2019**  
[a.dziavitsyn@gmail.com](mailto:a.dziavitsyn@gmail.com)  
  
Repository on GitHub: [https://github.com/Muritiku/spark-images](https://github.com/Muritiku/spark-images)  
  
Content:
+ Spark Cluster Images
+ Jupyter with pyspark images (compatible with cluster images to connect)

## DockerHub builded images links (look at using examples below)
+ [muritiku/spark-base](https://hub.docker.com/r/muritiku/spark-base)
+ [muritiku/spark-master](https://hub.docker.com/r/muritiku/spark-master)
+ [muritiku/spark-worker](https://hub.docker.com/r/muritiku/spark-worker)
+ [muritiku/spark-jupyter](https://hub.docker.com/r/muritiku/spark-jupyter)
  
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