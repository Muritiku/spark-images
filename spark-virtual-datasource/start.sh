#!/bin/bash

# spark with thrift-server starting config
java \
 -Duser.timezone=UTC \
 -Xmx512m \
 -cp "${SPARK_HOME}/conf:${SPARK_HOME}/jars/*" \
 org.apache.spark.deploy.SparkSubmit \
 --master local[8] \
 --conf spark.yarn.submit.waitAppCompletion=false \
 --conf spark.executor.extraJavaOptions=-Duser.timezone=UTC \
 --conf spark.cores.max=1 \
 --name "JDBC/ODBC Server" \
 --executor-memory 512m \
 /spark_tasks/task_runner.py /spark_tasks/tasks
