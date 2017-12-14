#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	dever-manage tools
	name:install.py
	author:rabin
	chmod +x install
	./install
	基础指令：
	use、set、env、up、shell
	dm up 更新代码
	dm use docker 使用docker工具包
	dm set shemic/aliyun/hub 使用哪个仓库为主
	dm shell hadoop.memory 直接调用src/shell下的脚本

	dm run web 运行web容器组
	dm run web-php 运行web容器组下的php容器
	dm run web-nginx 运行web容器组下的nginx容器
	dm build dev/php 根据dm set定义的主仓库，进行构建镜像
	dm rm web 删除web容器组
	dm rm 删除所有异常状态的容器
	dm show 显示所有容器
	dm showi 显示所有镜像
	dm rmi 删除所有未使用的镜像
	后续实现：
	dm use composer 使用composer工具包
	dm install redis 安装redis
	dm install laravel 安装laravel类库
	dm remove redis 删除redis

	dm use dever 使用dever框架工具包
	dm install manage 安装后台
	dm create myapp 初始化一个项目
	dm install passport 安装官方passport

"""
from core import *
class Main(object):
	use = 'docker'
	def __new__(cls, *args, **kwargs):
		print 'error'
		sys.exit()

	def __init__(self):
		pass

	@classmethod
	def init(self):
		Core.path = File.path().replace('/src/', '/')
		Args.init()
		method = ('use', 'set', 'val', 'up', 'commit', 'path', 'shell')
		if Args.action in method:
			self.handle()
		else:
			use = Env.use()
			if not use:
				use = Env.use(self.use)
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

Main.init()