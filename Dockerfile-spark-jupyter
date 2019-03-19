FROM muritiku/spark-base

LABEL maintainer='Anton Dziavitsyn a.dziavitsyn@gmail.com'

RUN pip install findspark
RUN mkdir /home/jupyter

EXPOSE 8888

WORKDIR /home/jupyter
CMD jupyter lab --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''
