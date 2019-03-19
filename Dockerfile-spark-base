FROM centos:7

LABEL maintainer='Anton Dziavitsyn a.dziavitsyn@gmail.com'

# SPARK
ENV SPARK_PROFILE 2.4
ENV SPARK_VERSION 2.4.0
ENV HADOOP_PROFILE 2.7
ENV HADOOP_VERSION 2.7.0

RUN yum install -y \
        telnet \
        bzip2 \
        git \
        java-1.8.0-openjdk \
        java-1.8.0-openjdk-devel \
        tar \
        unzip \
        curl \
        && \
        yum clean all


# Spark install
RUN curl -sSL https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_PROFILE.tgz -o /tmp/spark.tgz \
  && tar -xvzf /tmp/spark.tgz -C /opt/ \
  && rm -rf /tmp/spark.tgz \
  && ln -s /opt/spark-$SPARK_VERSION-bin-hadoop$HADOOP_PROFILE /opt/spark
COPY ./drivers /opt/spark/jars/
RUN chmod -R +rw /opt/spark
ENV SPARK_HOME /opt/spark

# Anaconda install
RUN curl -sSL https://repo.anaconda.com/archive/Anaconda3-2018.12-Linux-x86_64.sh -o /tmp/anaconda.sh \
    && bash /tmp/anaconda.sh -bfp /opt/conda/ \
    && rm -rf /tmp/anaconda.sh
ENV PATH /opt/conda/bin:$PATH
RUN conda install -y python=3 \
    && conda update conda \
    && conda clean --all --yes \
    && yum clean all
