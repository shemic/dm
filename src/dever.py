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
	framework = 'dever/framework.git'
	package = 'dever-package/'
	@classmethod
	def init(self):
		method = Core.getMethod(Dever_Action, Args.action)
		method()

class Dever_Action(object):
	@staticmethod
	def init():
		Git.update(Dever.git + Dever.framework, Dever.path + 'dever')

	@staticmethod
	def install():
		Git.update(Dever.git + Dever.package + Args.name, Dever.path + 'dever_package/' + Args.name)

	@classmethod
	def update(self):
		Git.update(Dever.git + Dever.package + Args.name, Dever.path + 'dever_package/' + Args.name)

	@staticmethod
	def create():
		Git.update(Dever.git + Dever.framework, Dever.path + 'dever')