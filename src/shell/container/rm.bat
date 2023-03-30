@echo off
set -e

docker stop %1
docker rm -f %1