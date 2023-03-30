@echo off
  
docker ps --format '{{.Names}}' --filter name=%1