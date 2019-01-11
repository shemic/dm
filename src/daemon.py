#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用于定时运行容器
import time
import subprocess
import os
import pprint
from gevent import monkey; monkey.patch_socket()
import gevent
timeSleep = 15

def redis():
        import redis
        host = '0.0.0.0'
        port = 6379
        pool = redis.ConnectionPool(host=host, port=int(port))
        return redis.Redis(connection_pool=pool)

def command(file):
        return 'dm call office-convert_call id=' + file

def popen(command, bg=False):
        string = command
        if bg == True:
                command = command + ' &'

        print command
        process = os.popen(command)
        output = process.read()
        process.close()
        print output
        return output

# 文档转换
def convert():
        r = redis()
        c = 'office_file'
        i = 0
        while 1:
                file = r.lpop(c)
                if file:
                        g = command(file)
                        popen(g, False)
                i = i+1
                if i >= 10:
                        time.sleep(timeSleep)
                        i = 0

def handle():
	gevent.joinall([
		gevent.spawn(git),
		#gevent.spawn(backup),
	])

handle()