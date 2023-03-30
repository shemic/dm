@echo off
pip install docker
set basepath=%~dp0
setx /M DEVERPATH "%basepath%src/"
setx /M PATH "%PATH%;%DEVERPATH%"
set dockerdaemon=%USERPROFILE%/.docker/daemon.json
(
	echo {
	echo "builder": { "gc": { "defaultKeepStorage": "20GB", "enabled": true } },
	echo "experimental": false,
	echo	"features": { "buildkit": true },
	echo	"registry-mirrors": [
	echo        "https://docker.mirrors.ustc.edu.cn",
	echo        "https://registry.docker-cn.com",
	echo        "http://hub-mirror.c.163.com",
	echo        "https://mirror.ccs.tencentyun.com"
	echo    ],
	echo    "insecure-registries" : ["docker.dever.cc"]
	echo }
) > %dockerdaemon%
set docker="Docker Desktop.exe"
tasklist|find /i %docker%
if %errorlevel%==0 ( 
	taskkill /f /im %docker%
)

start "docker" "%PROGRAMFILES%"\Docker\Docker\%docker%
echo "install success!"
pause