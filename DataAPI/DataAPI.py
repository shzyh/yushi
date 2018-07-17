# -*- coding: utf-8 -*-
# @Author: jiangfeng
import database
import pandas as pd

db = database.database()

#获取单只股票区间行情数据
def getMktDay(ticker=None,tradeDate=None,beginDate=None,endDate=None,field=None):
	sql = ''
	args = []
	ticker_sel = None

	field_sel = ""
	field_default = [
		"F_STOCK_STDCODE", #股票代码
		"F_TRADE_DATE",    #交易日期
		"F_STATUS",        #交易状态，0-正常，1-停牌，2-非交易日
		"F_PRECLOSE",      #前收盘价
		"F_OPEN",          #开盘价
		"F_HIGH",          #最高价
		"F_LOW",           #最低价
		"F_CLOSE",         #收盘价
		"F_RERIGHT_AFT",   #后复权价
		"F_EXRIGHT",       #除权因子
		"F_AVG",           #均价
		"F_CHG_PCT",       #涨跌幅
		"F_RANGE",         #振幅
		"F_VOLUME",        #成交量
		"F_AMOUNT",        #成交金额
		"F_TURNOVER_RATE", #换手率
		"F_TRADABLE_SHARE",#流通股本
		"F_TOTAL_SHARE",   #总股本
		]
	
	if field == None:
		field_sel = ','.join(field_default)
	else:
		field_sel = field if isinstance(field,str) else ','.join(field)

	if ticker==None and tradeDate==None:
		print "ticker and tradeDate must be not None at least one"
		return False 

	if tradeDate!=None:
		if ticker==None:
			sql = 'select {} from t_stock_trade_ex where F_TRADE_DATE={}'.format(field_sel,tradeDate)
		else:
			ticker_sel = ticker if isinstance(ticker,str) else ','.join(ticker)
			sql = 'select {} from t_stock_trade_ex where F_STOCK_STDCODE IN ({}) and \
				F_TRADE_DATE={}'.format(field_sel,ticker_sel,tradeDate)
	else:
		ticker_sel = ticker if isinstance(ticker,str) else ','.join(ticker)
		sql = 'select {} from t_stock_trade_ex where F_STOCK_STDCODE in ({}) and \
			F_TRADE_DATE between {} and {}'.format(field_sel,ticker_sel,beginDate,endDate)
	
	items = db.fetch_all(sql,args)
	print items
	df = pd.DataFrame(items)

	return df