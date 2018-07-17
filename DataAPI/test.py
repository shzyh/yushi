# -*- coding: utf-8 -*-
# @Author: jiangfeng
# @Date:   2018-06-06 09:11:43
# @Last Modified by:   jiangfeng
# @Last Modified time: 2018-06-06 19:53:19

# import logging
# import mod_config

import database
import DataAPI

b_date = '20180506'
e_date = '20180518'
df = DataAPI.getMktDay(beginDate=b_date,endDate=e_date)
# df = DataAPI.getMktDay(ticker='000001',tradeDate='20180518')
print df