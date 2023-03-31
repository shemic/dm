@echo off

if {%2} == {} (
	docker push %1
) else (
	docker tag %1 %2
	docker push %2
	docker rmi -f %2
)