@echo off

if {%1} == {} (
	for /f "skip=1 tokens=2,3 delims= " %%i in ('docker images') do (echo "%%i" | findstr "none" > nul && (docker rmi -f "%%i") || (echo "no"))
) else (
	for /f "skip=1 tokens=1,3 delims= " %%i in ('docker images') do (echo "%%i" | findstr "%1" > nul && (docker rmi -f "%%j") || (echo "no"))
)