#!/usr/bin/env sh
set -e

pip3 install git+https://github.com/shemic/jupyter-mysql-kernel

mkdir -p ~/.local/config/

echo "{\n
    "user"     : "root",\n
    "port"     : "3306",\n
    "host"     : "127.0.0.1",\n
    "charset"  : "utf8",\n
    "password" : "123456"\n
}" > ~/.local/config/mysql_config.json