FROM bde2020/spark-submit:2.4.1-hadoop2.7

MAINTAINER Cecile Tonglet <cecile.tonglet@tenforce.com>

COPY template.sh /

ENV SPARK_APPLICATION_PYTHON_LOCATION /app/entrypoint.py
ENV SPARK_APPLICATION_ARGS "foo bar baz"

#ENV    SPARK_MASTER_NAME (default: spark-master)
#    SPARK_MASTER_PORT (default: 7077)
#    SPARK_APPLICATION_PYTHON_LOCATION (default: /app/app.py)
#    SPARK_APPLICATION_ARGS



# Copy the requirements.txt first, for separate dependency resolving and downloading
ONBUILD COPY requirements.txt /app/
ONBUILD RUN cd /app \
      && pip3 install -r requirements.txt

# Copy the source code
ONBUILD COPY . /app

CMD ["/bin/bash", "/template.sh"]

