# -*- coding: utf-8 -*-
# @Author: jiangfeng

import pymysql
import mod_config
import mod_logger
import os

DB = "database"
DBNAME = mod_config.getConfig(DB,"dbname")
DBHOST = mod_config.getConfig(DB,"dbhost")
DBUSER = mod_config.getConfig(DB,"dbuser")
DBPWD  = mod_config.getConfig(DB,"dbpwd")
DBCHARSET = mod_config.getConfig(DB,"dbcharset")

log_path = os.path.join(os.getcwd()+r'\log','db_log.log')
logger = mod_logger.logger(log_path)


class database(object):
	def  __init__(self,dbname=None,dbhost=None):
		self._logger = logger
		if dbname is None:
			self._dbname = DBNAME 
		else:
			self._dbname = dbname
		
		if dbhost is None:
			self._dbhost = DBHOST 
		else:
			self._dbhost = dbhost

		self._dbuser     = DBUSER 
		self._dbpassword = DBPWD 
		self._dbcharset  = DBCHARSET 
		# self._dbport   = int(DBPORT)

		self._conn = self.connectMySQL()

		if (self._conn):
			self._cursor = self._conn.cursor()

	#数据库连接
	def connectMySQL(self):
		conn = False
		try:
			conn = pymysql.connect(
					host    = self._dbhost,
					user    = self._dbuser,
					passwd  = self._dbpassword,
					db      = self._dbname,
					# port  = self._dbport,
					charset = self._dbcharset,
					cursorclass = pymysql.cursors.DictCursor,
					)
		except Exception as e:
			self._logger.error("connect database failed, {}".format(e))
			conn = False
		return conn

	#获取查询结果集
	def fetch_all(self,sql,args=None):
		res = ''
		if (self._conn):
			try:
				if args == None:
					self._cursor.execute(sql)
				else:
					self._cursor.execute(sql,args)
				res = self._cursor.fetchall()
			except Exception as e:
				res = False
				self._logger.warn("query database exception:{}".format(e))
		return res

	#更新操作
	def update(self,sql):
		flag = False
		if (self._conn):
			try:
				self._cursor.execute(sql)
				self._conn.commit()
				flag = True
			except Exception as e:
				self._logger.warn("update database excetpion:{}".format(e))
		return flag
	
	#关闭数据库连接
	def close(self):
		if(self._conn):
			try:
				if (type(self._cursor)=='object'):
					self._cursor.close()
				if (type(self._conn)=='object'):
					self._conn.close()
			except Exception as e:
				self._logger.warn("close database exception:{},{},{}.".format(e,type(self._cursor),type(self._conn)))