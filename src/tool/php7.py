#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    dever-manage tools
    name:php.py
    author:rabin
"""
from core import *

class Php(object):
	path = 'src/php/'
	share = '/share/lib/php'
	@classmethod
	def init(self):
		method = Core.getMethod(Php_Action, Args.action)
		method()

class Php_Action(object):
	@staticmethod
	def install():
		Php_Install.install(Args.name)
		print 'install '+Args.name+':yes'


class Php_Install(object):
	@staticmethod
	def libevent(name):
		Core.popen('php.install ' + name, True)
		print 'finished'