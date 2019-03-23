#!/usr/bin/env python
# -*- coding: utf-8 -*-
# dm_process为key，value为具体指令 如：dm call office-convert_call id=1
import time
import os
#import pprint
#import subprocess
from gevent import monkey; monkey.patch_socket()
import gevent
timeSleep = 15
password = 'dm_redis_123'

def redis():
        import redis
        host = '0.0.0.0'
        port = 6379
        pool = redis.ConnectionPool(host=host, port=int(port), password=password)
        return redis.Redis(connection_pool=pool)

def pop(key):
        return popen('redis -a '+password+' lpop ' + key)

def command(process):
        return process

def popen(command, bg=False):
        string = command
        if bg == True:
                command = command + ' &'
        process = os.popen(command)
        output = process.read()
        process.close()
        return output

# 定时执行进程
def process():
        r = redis()
        c = 'dm_process'
        i = 0
        while 1:
                value = r.lpop(c)
                if value:
                        g = command(value)
                        popen(g)
                i = i+1
                if i >= 10:
                        gevent.sleep(timeSleep)
                        i = 0

def handle():
	gevent.joinall([
		gevent.spawn(process),
		#gevent.spawn(backup),
	])

handle()