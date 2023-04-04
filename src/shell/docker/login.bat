@echo off

set /p username=请输入username:
set /p password=请输入password:
docker login %1 -u %username -p %password