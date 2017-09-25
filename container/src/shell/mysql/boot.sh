#!/bin/sh
#
mysql_install_db --datadir=/var/lib/mysql

mysqld --defaults-file=/etc/mysql/my.cnf --user=root --datadir=/var/lib/mysql  --skip-networking

mysqladmin -u root password $MYSQL_ROOT_PASSWORD