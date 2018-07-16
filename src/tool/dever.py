#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    dever-manage tools
    name:dever.py
    author:rabin
"""
from core import *
import json

class Dever(object):
	git = 'http://git.dever.cc:3000/'
	lib = Core.path + 'container/share/lib/php/'
	dev = Core.path + 'container/web/'
	framework = 'dever/framework.git'
	demo = 'dever/demo.git'
	package = 'dever-package/'
	product = 'dever-product/'
	@classmethod
	def init(self):
		method = Core.getMethod(Dever_Action, Args.action)
		method()

	@staticmethod
	def rely(self, path):
		package = path + '/package.json'
		if File.exists(package):
			data = File.read(package, '')
			data = json.loads(data)
			if 'rely' in data:
				rely = data['rely'].split(',')
				for v in rely:
					Args.name = v
					self.package()

	@staticmethod
	def boot(lib):
		boot = lib + 'boot.php'
		if not File.exists(boot):
			File.write(boot, "<?php \r\n if (!defined('DEVER_PROJECT')) {\r\ndefine('DEVER_PROJECT', 'default');\r\ndefine('DEVER_PROJECT_PATH', dirname(__FILE__) . DIRECTORY_SEPARATOR);\r\n}\r\ninclude(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../dever/boot.php');")

class Dever_Action(object):
	@staticmethod
	def init():
		Git.update(Dever.git + Dever.framework, Dever.lib + 'dever')

	@classmethod
	def package(self):
		self.update(Dever.git + Dever.package + Args.name)

	@classmethod
	def put(self):
		Env.dever(Args.name)

	@classmethod
	def get(self):
		git = Args.param
		if not git:
			git = Env.dever()
		if not git or 'http' not in git:
			git = Dever.git + Dever.package
		self.update(git + Args.name)

	@classmethod
	def update(self, store):
		lib = Dever.lib + 'dever_package/'
		path = lib + Args.name
		Git.update(store, path)
		Dever.rely(self, path)
		Dever.boot(lib)

	@classmethod
	def all(self):
		path = Dever.lib + 'dever_package/'
		files = File.getFiles(path)
		if files:
			for i in files:
				if '.' not in i:
					Args.name = i
					self.update(False)

	@classmethod
	def pull(self):
		path = File.cur()
		Dever.rely(self, path)

	@classmethod
	def product(self):
		path = Dever.dev + Args.name
		Git.update(Dever.git + Dever.product + Args.name, path)
		Dever.rely(self, path)

	@staticmethod
	def demo():
		Git.update(Dever.git + Dever.demo, Dever.dev + 'demo')

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