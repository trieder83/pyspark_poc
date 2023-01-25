#!/bin/sh

docker run -it --rm --name sparkcli -v $PWD/spark-defaults.conf:/opt/bitnami/spark/conf/spark-defaults.conf -v $PWD/data:/data:rw -v $PWD/ojdbc8.jar:/tmp/ojdbc8.jar -v $PWD/elasticsearch-hadoop-7.8.0/dist/elasticsearch-spark-20_2.11-7.8.0.jar:/tmp/elasticsearch-spark-20_2.11-7.8.0.jar -v $PWD/spark-solr-3.8.0-shaded.jar:/tmp/spark-solr-3.8.0-shaded.jar  bitnami/spark:latest pyspark --jars /tmp/ojdbc8.jar,/tmp/spark-solr-3.8.0-shaded.jar,/tmp/elasticsearch-spark-20_2.11-7.8.0.jar
