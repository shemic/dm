@echo off

for /f "skip=1 tokens=2,3 delims= " %%i in ('docker images') do (echo "%%i" | findstr "none" > nul && (docker rmi -f "%%i") || (echo "no"))
