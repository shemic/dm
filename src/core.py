#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    dever-manage tools
    name:Core.py
    author:rabin
"""
import time
import datetime
import os
import sys
import getopt
import ConfigParser
import commands
import re
import subprocess
import urlparse

class Args(object):
	@classmethod
	def init(self):
		self.action = ''
		self.name = ''
		self.index = ''
		self.param = ''
		self.argv()

	@classmethod
	def argv(self):
		slen = len(sys.argv)
		if slen >= 2:
			self.action = sys.argv[1]
		if slen >= 3:
			self.name = sys.argv[2]
		if slen >= 4:
			self.param = sys.argv[3]
		self.options()
		if self.action == '':
			print 'action error'
			sys.exit()
		
	@classmethod
	def options(self):
		try:
			options, args = getopt.getopt(sys.argv[1:], "ha:n:p:", ['help', "action=", "name=", "param="])
			for name, value in options:
				if name in ('-h', '--help'):
					self.usage()
				elif name in ('-a', '--action'):
					self.method = value
				elif name in ('-n', '--name'):
					Args.name = value
				elif name in ('-p', '--param'):
					self.param = value
		except getopt.GetoptError:
			self.usage()
	@classmethod
	def usage(self):
		print File.read(Core.path, 'usage')
		sys.exit()

class Env(object):
	dm_use = 'base.use'
	dm_store = 'base.store'
	dm_cluster = 'base.cluster'
	dm_dever = 'base.dever'
	dm_val = 'val.'
	data = {}

	@staticmethod
	def key(name):
		return name.split('.')

	@classmethod
	def init(self, name):
		if not self.data:
			self.data = Config.runtime()
		return self.key(name)

	@classmethod
	def read(self, name):
		key, name = self.init(name)
		if key in self.data and name in self.data[key]:
			return self.data[key][name]
		else:
			return False

	@classmethod
	def write(self, name, value):
		key, name = self.init(name)
		self.data[key][name] = value
		Config.runtime(key, name, value)
		return value

	@classmethod
	def use(self, value=None):
		if value:
			return self.write(self.dm_use, value)
		return self.read(self.dm_use)

	@classmethod
	def dever(self, value=None):
		if value:
			return self.write(self.dm_dever, value)
		return self.read(self.dm_dever)

	@classmethod
	def store(self, value=None):
		if value:
			return self.write(self.dm_store, value)
		return self.read(self.dm_store)

	@classmethod
	def cluster(self, value=None):
		if value:
			return self.write(self.dm_cluster, value)
		return self.read(self.dm_cluster)

	@classmethod
	def val(self, name='', value=None):
		#name = self.dm_val + name.capitalize()
		name = self.dm_val + name
		if value:
			return self.write(name, value)
		return self.read(name)

class Config(object):
	@classmethod
	def runtime(self, key='', name='', value=''):
		runtime = Core.path + 'data/runtime.conf'
		if File.exists(runtime):
			config = ConfigParser.ConfigParser()
			config.read(runtime)
			if key and name:
				config.set(key, name, value)
				config.write(open(runtime, 'w'))
			else:
				result = {}
				for item in config.sections():
					result[item] = self.readOption(config, item)
				return result
		else:
			print runtime + ' is not exists'
			sys.exit()

	@classmethod
	def core(self, path):
		core = Core.path + path + 'core.conf'
		if File.exists(core):
			config = ConfigParser.ConfigParser()
			config.read(core)
			result = {}
			for item in config.sections():
				result[item] = self.readOption(config, item)
			return result
		else:
			print core + ' is not exists'
			sys.exit()

	@classmethod
	def read(self, path):
		if '-' in Args.name:
			temp = Args.name.split('-')
			Args.name = temp[0]
			Args.index = temp[1]

		filename = Core.path + path + 'conf/' + Args.name + '.conf'
		if File.exists(filename):
			config = ConfigParser.ConfigParser()
			config.read(filename)
			result = {}
			result['server'] = []
			result['config'] = {}
			result['base'] = {}
			for item in config.sections():
				if item == 'base':
					result['base'] = self.readOption(config, item)
				else:
					result['server'].append(item)
					result['config'][item] = self.readOption(config, item)

			result['base']['path'] = Core.replace('{base}', Core.path, result['base']['path'])
			return result
		else:
			print filename + ' is not exists'
			sys.exit()

	@staticmethod
	def readOption(config, type):
		value = config.options(type)
		result = {}
		for item in value:
			result[item] = config.get(type, item)
		return result

class Alias(object):
	@classmethod
	def delete(self, config, name, cluster=False):
		result = self.get(config, name)
		for key in result:
			action = self.action(name, key)
			if action[0] != 'sh' and File.exists(action[1]):
				content = File.get(action[1])
				string = 'docker exec -it ' + name + ' ' + action[0] + ' $@'
				if string in content:
					content = content.replace(string, '')
					File.write(action[1], content.strip())
					if 'docker' not in content:
						Core.popen('rm -rf ' + action[1], bg=True)
						Core.popen('rm -rf ' + action[2], bg=True)
			#Core.popen('rm -rf ' + action[1], bg=True)
			#Core.popen('rm -rf ' + action[2], bg=True)
	@classmethod
	def add(self, config, name, content, type, cluster=False):
		result = self.get(config, name)
		for key in result:
			action = self.action(name, key)
			old = ''
			if File.exists(action[1]):
				old = File.get(action[1])
			env = '#!/usr/bin/env sh \nset -e\n'
			if type != 'call':
				dexec = 'docker exec -it ' + name + ' ' + action[0] + ' $@'
				if cluster:
					dexec = 'name=`ds name ' + name + '`\n'
					dexec = dexec + 'docker exec -it $name ' + action[0] + ' $@'
				if action[0] == 'sh':
					content = env + self.define(name, cluster) + \
						'else\n' + \
						dexec + '\n' + \
						'fi'
				elif old:
					content = dexec
					if content not in old:
						content = old + '\n' + content
					else:
						content = ''
				else:
					content = env + dexec
			else:
				content = env + ' $@'
			if content:
				File.write(action[1], content)
				Core.popen('ln -sf ' + action[1] + ' ' + action[2])

	@staticmethod
	def define(name, cluster=False):
		conf = ['logs', 'inspect', 'restart', 'stop', 'rm', 'rmb', 'run', 'uprun', 'show']
		result = ''
		for key in conf:
			control = 'elif'
			command = 'dm'
			if cluster:
				command = 'ds'
			shell = command + ' ' + key + ' ' + name + '\n'
			if key == 'logs':
				control = 'if'
			result = result + control + ' [ "$1" = "'+key+'" ];then\n' + shell
		return result
	@classmethod
	def get(self, config, name):
		self.path = Core.path + 'data/alias/'
		result = []
		default = 'sh->' + name
		if 'alias' in config:
			config['alias'] = config['alias'] + ',' + default
			if ',' in config['alias']:
				result = config['alias'].split(',');
			else:
				result = [config['alias']]
		else:
			result = [default]
		return result
	@classmethod
	def action(self, name, key):
		file = key
		if '->' in key:
			temp = key.split('->')
			key = temp[0]
			file = temp[1]
		link = '/usr/bin/' + file
		file = self.path + file
		return [key, file, link]

class File(object):
	@staticmethod
	def write(file, content):
		handle = open(file, 'w')
		handle.write(content)
		handle.close()
		Core.popen('chmod +x ' + file)

	@staticmethod
	def read(path, name):
		handle = open(path + name, 'r')
		content = handle.read()
		handle.close()
		return content

	@staticmethod
	def get(file):
		handle = open(file, 'r')
		content = handle.read()
		handle.close()
		return content

	@staticmethod
	def getFiles(path):
		return os.listdir(path)

	@staticmethod
	def path():
		return os.path.split(os.path.realpath(__file__))[0] + '/'

	@staticmethod
	def cur():
		return os.getcwd()

	@staticmethod
	def exists(name):
		return os.path.exists(name)

	@staticmethod
	def rename(old, new):
		return os.rename(old, new)

	@staticmethod
	def remove(file):
		return os.remove(file)

	@staticmethod
	def mkdir(path):
		if File.exists(path) == False:
			os.mkdir(path)
		return path

	@staticmethod
	def mkdirs(path):
		if File.exists(path) == False:
			os.makedirs(path)
		return path

class Git(object):
	@staticmethod
	def update(git, path):
		if git and File.exists(path) == False:
			Core.popen('git clone ' + git + ' ' + path, True)
			print 'init:' + path + ' finished!'
		else:
			Core.popen('cd ' + path + ' && git pull', bg=True)
			print 'update:' + path + ' finished!'

class Service(object):
	@staticmethod
	def set(git, path):
		if File.exists(path) == False:
			Core.popen('git clone ' + git + ' ' + path, True)
			print 'init:' + path + ' finished!'
		else:
			Core.popen('cd ' + path + ' && git pull', bg=True)
			print 'update:' + path + ' finished!'

class Core(object):
	path = ''
	@classmethod
	def curl(self, url = '', param={}, method = 'get'):
		import requests
		if method == 'get':
			req = requests.get(url, params=param)
		else:
			req = requests.post(url, params=param)
		result = req.text
		return result
	@classmethod
	def getClass(self, name, path=''):
		obj = self.getObject(name, path)
		if path:
			if not hasattr(obj, name):
				print 'error ' + name
				sys.exit()
			obj = getattr(obj, name)
		name = name.capitalize()
		if not hasattr(obj, name):
			print 'error ' + name
			sys.exit()
		return getattr(obj, name)

	@staticmethod
	def getObject(name, path = ''):
		return __import__(path + name)

	@staticmethod
	def getMethod(obj, name):
		if not hasattr(obj, name):
			print 'error ' + name
			sys.exit()
		return getattr(obj, name)

	@classmethod
	def shell(self, command, sub=False, bg=False):
		shell = self.path + 'src/shell/' + command.replace('.', '/', 1)
		return self.popen(shell, sub, bg)
	@staticmethod
	def popen(command, sub=False, bg=False):
		string = command
		if bg == True:
			command = command + ' 1>/dev/null 2>&1 &'
		if sub == False:
			process = os.popen(command)
			output = process.read()
			process.close()
			return output
		else:
			popen  = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
			output = ''
			print string
			while True:
				output = popen.stdout.readline()
				print output
				if popen.poll() is not None:
					break
			return output
	@classmethod
	def install(self, soft):
		print 'install ' + soft + '...'
		if soft == 'docker':
			self.shell('install.docker', True)
		else:
			self.shell('install.package ' + soft, True)
	@classmethod
	def check(self, soft):
		result = int(Core.popen('which '+soft+' | wc -l'))
		if result != 0:
			return 1
		else:
			self.install(soft)
			return 0
	@staticmethod
	def replace(old, new, string):
		if old in string:
			string = string.replace(old, new)
		return string
	@staticmethod
	def isset(v): 
		try : 
			type(eval(v))
		except : 
			return  0 
		else : 
			return  1

	@staticmethod
	def ip(ifname = 'eth0'):
		import socket, fcntl, struct  
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
		inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))  
		ret = socket.inet_ntoa(inet[20:24])
		return ret