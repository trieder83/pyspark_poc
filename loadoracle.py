docker cp ojdbc8.jar spark-master:/
docker cp spark-solr-3.6.4-shaded.jar  spark-master:/

docker exec -it spark-master /spark/bin/pyspark --jars /ojdbc8.jar,/spark-solr-3.6.0.jar
docker exec -it spark-master /spark/bin/pyspark --jars /ojdbc8.jar,/spark-solr-3.6.4-shaded.jar



empDF = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:oracle:thin:test/test@//192.168.1.12:1521/demo01") \
    .option("dbtable", "test.emp") \
    .option("user", "test") \
    .option("password", "test") \
    .option("driver", "oracle.jdbc.driver.OracleDriver") \
    .load()
empDF.printSchema()
empDF.show()
#
query = "(select empno,ename,dname from emp, dept where emp.deptno = dept.deptno) emp"
empDF = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:oracle:thin:username/password@//hostname:portnumber/SID") \
    .option("dbtable", query) \
    .option("user", "db_user_name") \
    .option("password", "password") \
    .option("driver", "oracle.jdbc.driver.OracleDriver") \
    .load()

data1DF = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:oracle:thin:test/test@//192.168.1.12:1521/demo01") \
    .option("dbtable", "test.data1") \
    .option("user", "test") \
    .option("password", "test") \
    .option("driver", "oracle.jdbc.driver.OracleDriver") \
    .load()
data1DF.printSchema()
data1DF.show()
data1DF.write.format("solr").option("zkhost","192.168.1.12:9983").option("collection","test").option("commit_within", "5000").mode("append").save()
#

writeToSolrOpts = {"zkhost" : "192.168.1.12:9983" , "collection" :  "test" }
empDF.write.format("solr").options(writeToSolrOpts).save

empDF.write.format("solr").option("zkhost","192.168.1.12:9983").option("collection","test").mode("append").save()

# play
empDF.select('JOB').rdd.map(lambda x: (x,1)).reduceByKey(lambda a,b: a+b).take(5)
empDF.select('JOB').rdd.map(lambda x: (x,1)).reduceByKey(lambda a,b: a+b).toDF().show()

df = spark.read.format("solr") \
  .option("zkhost","192.168.1.12:9983") \
  .option("collection","test") \
  .load()


docker exec -it spark-master /spark/bin/spark-shell --master local[*] --jars /ojdbc8.jar,/spark-solr-3.6.4-shaded.jar --driver-class-path /ojdbc8.jar,/spark-solr-3.6.4-shaded.jar
#docker exec -it spark-master /spark/bin/spark-shell --master local[*] --jars /ojdbc8.jar,/spark-solr-3.6.4-shaded.jar

val df_oracle = spark.read.format("jdbc").option("url", "jdbc:oracle:thin:test/test@//192.168.1.12:1521/demo01").option("dbtable", "test.emp").option("user", "test").option("password", "test").load()

var writeToSolrOpts = Map("zkhost" -> "192.168.1.12:9983", "collection" -> "test")
in.write.format("solr").options(writeToSolrOpts).save


## try scala
import org.apache.spark.sql.SparkSession
import spark.implicits._
#import org.apache.spark.SparkConf
#SparkConf conf = new SparkConf().setAppName("solr").setMaster("spark://c23938c40dee:7077");
val spark = SparkSession.builder().appName("Spark SQL basic example").getOrCreate()
#val spark = SparkSession.builder().appName("Spark SQL basic example").setMaster("spark://c23938c40dee:7077");
val sc: spark.SparkContext 
val sqlContext = new org.apache.spark.sql.SQLContext(sc)
val test = sqlContext.load("solr",Map("zkHost" -> "192.168.1.12:9983", "collection" -> "test"))
test.schema();
test.show();
