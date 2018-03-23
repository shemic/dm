#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    dever-manage tools
    name:php.py
    author:rabin
"""
from core import *

class Php(object):
	@classmethod
	def init(self):
		method = Core.getMethod(Php_Action, Args.action)
		method()

class Php_Action(object):
	package = {
		# 名称-版本号,so名,依赖包,configure参数
		'libevent' : ['event-2.3.0', 'event', 'curl-dev,libevent-dev', '']
		,'swoole' : ['swoole-2.0.10', 'swoole', 'libevent-dev,libaio-dev,libmnl-dev', '']
		,'mongo' : ['mongodb-1.3.4', 'mongodb', '', '']
		,'redis' : ['redis-3.1.5RC2', 'redis', '', '']
		,'memcached' : ['memcached-3.0.4', 'memcached', 'libmemcached-dev,cyrus-sasl-dev', '']
	}

	@classmethod
	def install(self):
		if Args.name in self.package:
			name = self.package[Args.name][0]
			rely = self.package[Args.name][1]
			so = self.package[Args.name][2]
			config = self.package[Args.name][3]
		else:
			print Args.name+' error'
			return

		Core.popen('phpInstall ' + name + ' ' + rely + ' ' + so + ' ' + config, True)
		print 'install '+Args.name+':yes'
		
	@classmethod
	def show(self):
		print self.package.keys()