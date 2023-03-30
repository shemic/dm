@echo off

if  "%1" == "" (
	docker ps -a
) else (
	docker ps -a | findstr "%1"
)