#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core import *
class Main(object):
	use = 'docker'
	def __new__(cls, *args, **kwargs):
		print 'error'
		sys.exit()

	def __init__(self):
		pass

	@classmethod
	def init(self, use = 'docker'):
		Core.path = File.path().replace('/src/', '/')
		Args.init()
		method = ('use', 'set', 'val', 'up', 'commit', 'path', 'shell')
		if Args.action in method:
			self.handle()
		else:
			"""
			use = Env.use()
			if not use:
				use = Env.use(self.use)
			"""
			cls = Core.getClass(use, 'tool.')
			cls.init()

	@classmethod
	def handle(self):
		method = Core.getMethod(Main_Action, Args.action)
		method()

class Main_Action(object):
	@staticmethod
	def use():
		if not Args.name:
			print 'dm name is not exists!'
			sys.exit()
		Env.use(Args.name)

	@staticmethod
	def set():
		if not Args.name:
			print 'dm name is not exists!'
			sys.exit()
		Env.store(Args.name)

	@staticmethod
	def val():
		if not Args.name:
			print 'dm name is not exists!'
			sys.exit()
		if not Args.param:
			print 'dm param is not exists!'
			sys.exit()
		Env.val(Args.name, Args.param)

	@staticmethod
	def up():
		print 'loading...'
		Core.shell('git.pull ' + Core.path)
		print 'dm update success!'

	@staticmethod
	def commit():
		print Core.shell('git.push ' + Core.path)

	@staticmethod
	def path():
		print Core.path

	@staticmethod
	def shell():
		print Core.shell(Args.name)

#Main.init()