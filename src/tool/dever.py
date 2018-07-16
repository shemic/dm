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
	package_list = []
	@classmethod
	def init(self):
		method = Core.getMethod(Dever_Action, Args.action)
		method()

	@classmethod
	def rely(self, action, path):
		package = path + 'package.json'
		if Args.param:
			Dever_Create.package(path, Args.param)
			Args.param = ''

		if File.exists(package):
			data = File.read(package, '')
			data = json.loads(data)
			if 'rely' in data:
				rely = data['rely'].split(',')
				for v in rely:
					package = action.package(v)
					self.package_list.append({'path':package, 'name':v})

	@classmethod
	def create(self, path):
		name = os.path.basename(path)
		Dever_Create.boot(path + '/', name)
		print "create finished!"

	@staticmethod
	def cur(up = True):
		name = Args.name
		path = File.cur()
		if name:
			git = ''
			if '/' in name:
				git = name
				name = os.path.basename(git).replace('.git', '')
			path = path + '/' + name
			if git and up:
				Dever_Create.git(git, path)
		return path

class Dever_Create(object):

	@staticmethod
	def package_boot(lib):
		file = lib + 'boot.php'
		if not File.exists(file):
			File.write(file, "<?php \r\nif (!defined('DEVER_PROJECT')) {\r\ndefine('DEVER_PROJECT', 'default');\r\ndefine('DEVER_PROJECT_PATH', dirname(__FILE__) . DIRECTORY_SEPARATOR);\r\n}\r\ninclude(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../dever/boot.php');")

	@classmethod
	def boot(self, path, name):
		file = path + 'boot.php'
		if not File.exists(file):
			File.write(file, "<?php \r\ndefine('DEVER_PROJECT', '"+name+"');\r\ndefine('DEVER_PROJECT_PATH', dirname(__FILE__) . DIRECTORY_SEPARATOR);\r\nif (defined('DEVER_PACKAGE')) {\r\n	include('dever_package/'.DEVER_PACKAGE.'/index.php');\r\n} else {\r\n	include('dever/boot.php');\r\n}")

		self.dm(path)
		self.gitignore(path)
		self.data(path)
		self.config(path, name)

	@classmethod
	def index(self, path, name, package):
		path = path + name + '/'
		if File.exists(package + 'index.php') and not File.exists(path):
			File.mkdir(path)
			file = path + 'index.php'
			if not File.exists(file):
				File.write(file, "<?php \r\ndefine('DEVER_PACKAGE', '"+name+"');\r\ndefine('DEVER_APP_SETUP', dirname(__FILE__) . DIRECTORY_SEPARATOR);\r\ninclude(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../boot.php');")
		if File.exists(package + 'daemon'):
			path = path + 'daemon/'
			if not File.exists(path):
				Core.popen('cp -R ' + package + 'daemon/ ' + path)

	@staticmethod
	def gitignore(path):
		file = path + '.gitignore'
		if not File.exists(file):
			File.write(file, "dm\r\n.DS_Store\r\n*.pyc\r\ndata/upload/*\r\ndata/database/*\r\ndata/project/*\r\ndata/logs/*\r\n\r\ndata/signature/*\r\ndata/avatar/*")

	@staticmethod
	def dm(path, check = False):
		file = path + 'dm'
		state = File.exists(file)
		if check:
			return state
		if not state:
			File.write(file, "dm created")

	@staticmethod
	def package(path, rely):
		file = path + 'package.json'
		if not File.exists(file):
			File.write(file, '{\r\n"rely": "'+rely+'"\r\n}')

	@staticmethod
	def git(addr, path):
		file = path + '/' + '.git/'
		if not File.exists(file):
			Git.update(addr, path)
		else:
			Git.set(addr, path)

	@staticmethod
	def data(path):
		path = path + 'data/'
		if not File.exists(path):
			File.mkdir(path)
			Core.popen('chmod -R 777 ' + path)
			file = path + 'readme'
			if not File.exists(file):
				File.write(file, "dever create")

	@staticmethod
	def config(path, name):
		path = path + 'config/'
		if not File.exists(path):
			File.mkdir(path)
			file = path + 'base.php'
			if not File.exists(file):
				File.write(file, "<?php\r\n$config['base'] = array\r\n(\r\n'name' => '"+name+"',\r\n'version' => '1.0.0 Beta'\r\n);\r\nreturn $config;")

			file = path + 'route.php'
			if not File.exists(file):
				File.write(file, "<?php\r\nreturn array\r\n(\r\n'home' => 'home',\r\n);")

			path = path + 'env/localhost/'
			if not File.mkdirs(path):
				File.mkdir(path)
				file = path + 'default.php'
				if not File.exists(file):
					File.write(file, "<?php\r\n$config['database'] = array\r\n(\r\n'default' => array\r\n(\r\n'type' => 'pdo',\r\n'host' => array\r\n(\r\n'read' => 'web-mysql:3306',\r\n'update' => 'web-mysql:3306',\r\n),\r\n'database' => '"+name+"',\r\n'username' => 'root',\r\n'password' => '123456',\r\n'charset' => 'utf8',\r\n),\r\n);\r\nreturn $config;")


class Dever_Action(object):
	@staticmethod
	def init():
		Git.update(Dever.git + Dever.framework, Dever.lib + 'dever')

	@classmethod
	def package(self, name = False):
		if not name:
			name = Args.name
		return self.update(Dever.git + Dever.package + name, name)

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
		return self.update(git + Args.name, Args.name)

	@classmethod
	def update(self, store, name = False):
		if not name:
			name = Args.name
		lib = Dever.lib + 'dever_package/'
		path = lib + name + '/'
		Git.update(store, path)
		Dever.rely(self, path)
		Dever_Create.package_boot(lib)
		project = Dever.cur(False) + '/'
		if Dever_Create.dm(project, True):
			Dever_Create.index(project, name, path)
		return path

	@classmethod
	def all(self):
		path = Dever.lib + 'dever_package/'
		files = File.getFiles(path)
		if files:
			for i in files:
				if '.' not in i:
					self.update(False, i)

	@classmethod
	def pull(self):
		path = Dever.cur()
		Dever.rely(self, path + '/')
		Git.update('', path + '/')
		return path

	@classmethod
	def push(self):
		path = File.cur()
		Git.push(path + '/', Args.name, Args.param)

	@classmethod
	def dev(self):
		path = File.cur()
		Git.push(path + '/', Args.name, Args.param)

	@classmethod
	def product(self):
		path = Dever.dev + Args.name
		Git.update(Dever.git + Dever.product + Args.name, path)
		Dever.rely(self, path)

	@staticmethod
	def demo():
		Git.update(Dever.git + Dever.demo, Dever.dev + 'demo')

	@classmethod
	def create(self):
		path = self.pull()
		print "creating..."
		for v in Dever.package_list:
			Dever_Create.index(path + '/', v['name'], v['path'])
		Dever.create(path)