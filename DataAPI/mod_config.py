# -*- coding: utf-8 -*-
# @Author: jiangfeng
# @Date:   2018-06-06 12:18:59
# @Last Modified by:   jiangfeng
# @Last Modified time: 2018-06-06 12:23:33

import ConfigParser
import os

#获取config的配置文件
"""使用方法
dbname = mod_config.getConfig("database", "dbname")
"""
def getConfig(section,key):
	config = ConfigParser.ConfigParser()
	path   = os.path.split(os.path.realpath(__file__))[0] + r'\conf.cfg'
	config.read(path)
	return config.get(section,key)
	pass

#其中 os.path.split(os.path.realpath(__file__))[0] 得到的是当前文件模块的目录