#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	dever-manage tools
	name:install.py
	author:rabin
	chmod +x install
	./install
	基础指令：
	set、env、up、shell
	dm up 更新代码
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

"""
from main import *
Main.init('docker')