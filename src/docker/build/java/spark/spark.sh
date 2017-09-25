#!/usr/bin/env sh
set -e

start_share_spark()
{
    share $SPARK_HOME spark
}

stop_share_spark()
{
    true
}

start_spark()
{
    if [ "$1" == "share" ]; then
        start_share_spark
    fi
    $SPARK_HOME/sbin/start-all.sh
}

stop_spark()
{
    $SPARK_HOME/sbin/stop-all.sh &
}

start_spark_log()
{
    if [ "$1" == "share" ]; then
        start_share_spark
    fi
    check hadoop
    hadoop_mkdir spark spark/jars spark/log
    hadoop fs -put -f /usr/local/spark/jars/* /spark/jars/ &
}

stop_spark_log()
{
    true
}

spark_test_pi()
{
	spark-submit --class org.apache.spark.examples.SparkPi --master yarn --deploy-mode client /usr/local/spark/examples/jars/spark-examples_2.11-2.1.1.jar
}