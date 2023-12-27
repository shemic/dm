#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	dever-manage tools
	name:install.py
	author:rabin
	dever init 初始化，更新核心类库
	dever package manage 更新manage官方组件
	dever store http://git.5dev.cn:3000/php_package/ 定义自定义组件的仓库组路径
	dever get collect [git] 获取当前store/[git]下的自定义组件
	dever pull [git] 在当前目录/[git]下更新所有依赖组件
	dever convert name [git] 将当前目录下的name目录转换为组件，推送到当前store/[git]下
	dever create [git] 在当前目录/[git]下创建一个项目
	dever dev 进入开发模式
	dever push 将当前目录下的文件推送到线上 如果是开发模式，将本地分支合并到master上
	dever all 更新当前所有组件

"""
from main import *
Main.init('dever2')