#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	dever-manage tools
	name:install.py
	author:rabin
	dever init 初始化，更新核心类库
	dever package manage 更新manage官方组件
	dever put http://git.5dev.cn:3000/php_package/ 定义自定义组件的仓库组路径
	dever get collect 获取自定义组件
	dever pull 在当前目录下更新所有依赖组件
	dever create 在当前目录下创建一个项目
	dever all 更新当前所有组件

"""
from main import *
Main.init('dever')