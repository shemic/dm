#!/bin/bash
#
#
#
D_docker="docker pull"
D_library="daocloud.io/"
D_package[0]="library/php:5.6.25-fpm-alpine,-v /data/nginx/web:/var/www/html"
D_package[1]="library/nginx:stable-alpine"
D_package[2]="library/mysql:5.7.8-alpine"
D_package[3]="library/memcached:alpine"
D_package[4]="library/redis:alpine"
D_package[5]="library/python:alpine"
D_package[6]="library/golang:alpine"
D_package[7]="library/alpine:latest"
D_package[8]="library/ubuntu:latest"

D_application[0]="daocloud/gogs:latest"
#D_application[1]="daocloud/dever:latest"

dever_check()
{
	#if [ `ps -ef | grep $1 | grep -v grep | grep "master" | wc -l` -ne 0 ] ; then
	#if [ `ps -ef | grep $1 | grep -v grep | wc -l` -ne 0 ] ; then
	if [ `which $1 | wc -l` -ne 0 ] ; then
		return 1
	else
		dever_install $1
		return 0
	fi
}

dever_server_check()
{
	if [ `docker ps -a | grep $1 | wc -l` -ne 0 ] ; then
		return 1
	else
		return 0
	fi
}

dever_install()
{
	echo "install $1..."
	if [ $1 = "docker" ] ; then
		`curl -sSL https://get.daocloud.io/docker | sh`
		dever_package
	else
		`apt-get install $1`
	fi
}

dever_init()
{
	dever_check curl
	dever_check docker
}

dever_start()
{
	dever_init
	read -p "please start server:" i j
	#input=`echo $?`
	dever_server $i $j
}

dever_package()
{
	echo "download package..."

	for config in ${D_package[@]};
	do
	    #echo "$D_docker $D_library$var"
	    $D_docker $D_library${config%,*}
	    #${str##*,}
	done

	echo "download finished"
}

dever_server()
{
	dever_server_check $1
	if [ $? = 0 ] ; then
		echo "start $1 server..."
		for i in ${!D_package[@]};
		do
			config=${D_package[$i]}
			param=${config##*,}
			name=${config%,*}
		    [[ $name =~ $1 ]] && 
		    echo "docker run -it --name=$1_1 -d ${param##*,} $D_library$name"
		done
	else
		echo "reload $1 server..."
		for i in ${!D_package[@]};
		do
			var=${D_package[$i]}
		    [[ $var =~ $1 ]] && 
		    echo "docker reload $1"
		done
	fi
}

#read -p "[init|start|reload]please input method:" i
#if [ $i = "init" ] ; then
#	dever_init
#elif [ $i = "start" ] ; then
#	dever_start
#elif [ $i = "reload" ] ; then
#	dever_reload
#fi
dever_start