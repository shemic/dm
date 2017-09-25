#!/bin/bash
set -e

dever_yarn()
{
	$HADOOP_HOME/sbin/start-yarn.sh
}

dever_dfs()
{
	$HADOOP_HOME/sbin/start-dfs.sh
}

dever_start()
{
	dever_dfs
	echo -e "\n"
	dever_yarn
	echo -e "\n"
}

dever_wordcount()
{
	mkdir input
	echo "Hello Docker" >input/file2.txt
	echo "Hello Hadoop" >input/file1.txt

	# create input directory on HDFS
	hadoop fs -mkdir -p input

	# put input files to HDFS
	hdfs dfs -put ./input/* input

	# run wordcount 
	hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/sources/hadoop-mapreduce-examples-2.7.2-sources.jar org.apache.hadoop.examples.WordCount input output

	# print the input files
	echo -e "\ninput file1.txt:"
	hdfs dfs -cat input/file1.txt

	echo -e "\ninput file2.txt:"
	hdfs dfs -cat input/file2.txt

	# print the output of wordcount
	echo -e "\nwordcount output:"
	hdfs dfs -cat output/part-r-00000
}

dever_ssh()
{
	/usr/sbin/sshd
}

if [ "$1" = 'start' ]; then
	dever_start
fi

if [ "$1" = 'wordcount' ]; then
	dever_wordcount
fi

if [ "$1" = 'ssh' ]; then
	dever_ssh
fi

exec $0