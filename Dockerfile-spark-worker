FROM muritiku/spark-base

LABEL maintainer='Anton Dziavitsyn a.dziavitsyn@gmail.com'

ENV SPARK_WORKER_OPTS "-Dspark.driver.port=7001 -Dspark.fileserver.port=7002 -Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004 -Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4041"
ENV SPARK_WORKER_PORT 7078
ENV SPARK_WORKER_WEBUI_PORT 8081

EXPOSE 8081 7078 4041 7001 7002 7003 7004 7005 7006

WORKDIR $SPARK_HOME
CMD bin/spark-class org.apache.spark.deploy.worker.Worker $SPARK_MASTER -p $SPARK_WORKER_PORT --webui-port $SPARK_WORKER_WEBUI_PORT
