FROM muritiku/spark-base

LABEL maintainer='Anton Dziavitsyn a.dziavitsyn@gmail.com'

ENV SPARK_MASTER_OPTS "-Dspark.driver.port=7001 -Dspark.fileserver.port=7002 -Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004 -Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4040"
ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 8080

EXPOSE 8080 7077 4040 7001 7002 7003 7004 7005 7006

WORKDIR $SPARK_HOME
CMD bin/spark-class org.apache.spark.deploy.master.Master
