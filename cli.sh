#!/bin/sh

docker run -it --rm --name sparkcli -v $PWD/spark-defaults.conf:/opt/bitnami/spark/conf/spark-defaults.conf bitnami/spark:latest spark-shell
