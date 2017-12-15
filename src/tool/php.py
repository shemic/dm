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
		# 名称-版本号,依赖包
		'libevent' : ['event-2.3.0', 'libevent-dev', 'event']
		,'swoole' : ['swoole-2.0.10', 'libevent-dev,libaio-dev,libmnl-dev', 'swoole']
	}

	@classmethod
	def install(self):
		if Args.name in self.package:
			name = self.package[Args.name][0]
			rely = self.package[Args.name][1]
			so = self.package[Args.name][2]
		else:
			print Args.name+' error'
			return

		Core.popen('phpInstall ' + name + ' ' + rely + ' ' + so, True)
		print 'install '+Args.name+':yes'
		