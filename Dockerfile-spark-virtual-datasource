FROM muritiku/spark-base

LABEL maintainer='Anton Dziavitsyn a.dziavitsyn@gmail.com'

RUN pip install findspark

ENV PYSPARK_PYTHON="/opt/conda/bin/python3"

EXPOSE 10000

COPY /spark-virtual-datasource/* /spark_tasks/
RUN chmod +x /spark_tasks/start.sh

ENTRYPOINT /spark_tasks/start.sh