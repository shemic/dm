#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    dever-manage tools
    name:php.py
    author:rabin
"""
from core import *

class Composer(object):
	@classmethod
	def init(self):
		method = Core.getMethod(Composer_Action, Args.action)
		method()

class Composer_Action(object):
	@staticmethod
	def install():
		Composer.install(Args.name)
		print 'install '+Args.name+':yes'

	@classmethod
	def update(self):
		Composer.update()


class Composer(object):
	@staticmethod
	def update():
		Core.popen('composer.update', True)
	@staticmethod
	def install(name):
		Core.popen('composer.install ' + name, True)
		print 'finished'