# Spark based images
**by Anton Dziavitsyn 2019**  
[a.dziavitsyn@gmail.com](mailto:a.dziavitsyn@gmail.com)
  
+ Spark Cluster Images
+ Jupyter with pyspark images (compatible with cluster images to connect)

## DockerHub builded images links
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
