#!/usr/bin/env sh
set -e

start_share_java()
{
    share $JAVA_HOME jdk
}
start_java()
{
    start_share_java
}