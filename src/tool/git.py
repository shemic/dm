#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    dever-manage tools
    name:git.py
    author:rabin
"""
from core import *
import json

class Git(object):
	@classmethod
	def init(self):
		method = Core.getMethod(Git_Action, Args.action)
		method()

class Git_Action(object):
	@staticmethod
	def path():
		return Args.name

	@classmethod
	def pull(self):
		path = self.path()
		Core.popen('cd ' + path + ' && git pull', True)

	@classmethod
	def push(self):
		path = self.path()
		if Args.param:
			file = Args.param
		else:
			file = '*'
		Core.popen('cd ' + path + ' && git commit -m "edit" '+file+' && git push -u origin master', True)

	@classmethod
	def clone(self):
		path = self.path()
		Core.popen('cd ' + path + ' && git clone ' + Args.param, True)