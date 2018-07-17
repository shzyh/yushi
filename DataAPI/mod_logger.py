# -*- coding: utf-8 -*-
# @Author: jiangfeng
# @Date:   2018-06-06 12:35:28
# @Last Modified by:   jiangfeng
# @Last Modified time: 2018-06-06 13:09:58

import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_LEVEL = logging.DEBUG


def logger(logpath):
	logging.basicConfig(filename=logpath,level=LOG_LEVEL,format=LOG_FORMAT)
	return logging
	pass






# import logging.config
# from logging.handlers import RotatingFileHandler
# import mod_config

# log = "log"
# format = mod_config.getConfig(log,"format").replace('@','%')
# level  = int(mod_config.getConfig(log,"level"))
# backupcount = int(mod_config.getConfig(log,"backupcount"))
# maxbytes = int(mod_config.getConfig(log,"maxbytes"))

# #日志设置
# def logger(logpath):
# 	logger = logging.getLogger(logpath)
# 	Rthandler = RotatingFileHandler(logpath,maxbytes=maxbytes,backupcount=backupcount)
# 	logger.setLevel(level)
# 	formatter = logging.Formatter(format)
# 	Rthandler.setFormatter(formatter)
# 	logger.addHandler(Rthandler)
# 	return logger
# 	pass

"""
日志级别
CRITICAL 50
ERROR    40
WARNING  30
INFO     20
DEBUG    10
NOSET    0
"""