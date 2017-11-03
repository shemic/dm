#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    dever-manage tools
    name:php.py
    author:rabin
"""
from core import *
import json

class Dever(object):
	git = 'http://git.dever.cc:3000/'
	lib = Core.path + 'container/share/lib/php/'
	dev = Core.path + 'container/web/'
	framework = 'dever/framework.git'
	package = 'dever-package/'
	@classmethod
	def init(self):
		method = Core.getMethod(Dever_Action, Args.action)
		method()

class Dever_Action(object):
	@staticmethod
	def init():
		Git.update(Dever.git + Dever.framework, Dever.lib + 'dever')

	@classmethod
	def install(self):
		self.update()

	@classmethod
	def update(self):
		path = Dever.lib + 'dever_package/'
		boot = path + 'boot.php'
		if not File.exists(boot):
			File.write(boot, "<?php \r\n if (!defined('DEVER_PROJECT')) {\r\ndefine('DEVER_PROJECT', 'default');\r\ndefine('DEVER_PROJECT_PATH', dirname(__FILE__) . DIRECTORY_SEPARATOR);\r\n}\r\ninclude(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../dever/boot.php');")
		path = path + Args.name
		Git.update(Dever.git + Dever.package + Args.name, path)
		package = path + '/package.json'
		if File.exists(package):
			data = File.read(package, '')
			data = json.loads(data)
			if 'rely' in data:
				rely = data['rely'].split(',')
				for v in rely:
					Args.name = v
					self.update()


	@staticmethod
	def create():
		path = Dever.dev + Args.name
		if not Args.name:
			print 'name is error'
			return
		if File.exists(path):
			print path + ' is exists'
		else:
			print path