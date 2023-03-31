@echo off

for /f "skip=1 tokens=1,* delims= " %%i in ('docker ps -a') do (echo "%%j" | findstr "Exited" > nul && (docker rm -f "%%i") || (echo "no"))
