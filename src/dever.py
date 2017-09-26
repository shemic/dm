#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    dever-manage tools
    name:php.py
    author:rabin
"""
from core import *

class Dever(object):
	git = 'http://git.dever.cc:3000/'
	path = Core.path + 'container/share/lib/php/'
	@classmethod
	def init(self):
		method = Core.getMethod(Dever_Action, Args.action)
		method()

class Dever_Action(object):
	@staticmethod
	def init():
		if Args.name:
			print 'init appname'
		else:
			Core.popen('git clone '+Dever.git+'dever/framework.git ' + Dever.path + 'dever', True)
			print 'init:yes'

	@staticmethod
	def install():
		print 'install '+Args.name+':yes'

	@classmethod
	def update(self):
		print 'update '+Args.name+':yes'


class Package(object):
	@staticmethod
	def update():
		Core.popen('composer.update', True)
	@staticmethod
	def install(name):
		Core.popen('composer.install ' + name, True)
		print 'finished'