@echo off

docker build --no-cache -t %1 %2
docker images %1