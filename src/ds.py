#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	dever-manage tools
	name:ds.py
	author:rabin
	功能：集群管理工具，基本命令和dm一致
	ds init 初始化
	ds join ip 加入集群
	ds run web 运行web服务组
	ds run web-php 运行web服务组下的php服务
	ds run web-nginx 运行web服务组下的nginx服务
	ds rm web 删除web服务组
	ds show 显示所有服务
	ds node 查看所有集群节点
"""
from main import *
Main.init('cluster')