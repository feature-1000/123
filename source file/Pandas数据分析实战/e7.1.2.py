# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:24:35 2020

@author: adiministrator
"""

###7.1.2  时间序列与常用操作
import pandas as pd
'''
date_range(start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, closed=None, **kwargs)
    Return a fixed frequency DatetimeIndex.
    
    Parameters
    ----------
    start : str or datetime-like, optional Left bound for generating dates.
    end : str or datetime-like, optional Right bound for generating dates.
    periods : integer, optional Number of periods to generate.
    freq : str or DateOffset, default 'D'
        Frequency strings can have multiples, e.g. '5H'. See
        :ref:`here <timeseries.offset_aliases>` for a list of
        frequency aliases.
    tz : str or tzinfo, optional
        Time zone name for returning localized DatetimeIndex, for example
        'Asia/Hong_Kong'. By default, the resulting DatetimeIndex is
        timezone-naive.
    normalize : bool, default False
        Normalize start/end dates to midnight before generating date range.
    name : str, default None
        Name of the resulting DatetimeIndex.
    closed : {None, 'left', 'right'}, optional
        Make the interval closed with respect to the given frequency to
        the 'left', 'right', or both sides (None, the default).
    **kwargs
        For compatibility. Has no effect on the result.
'''
# start指定起始日期，end指定结束日期，periods指定产生的数据数量
# freq指定间隔，D表示天，W表示周，H表示小时
# M表示月末最后一天，MS表示月初第一天
# T表示分钟，Y表示年末最后一天，YS表示年初第一天
print('间隔5天'.ljust(30, '='))
print(pd.date_range(start='20190601', end='20190630', freq='5D'))

print('间隔1周'.ljust(30, '='))
print(pd.date_range(start='20190601', end='20190630', freq='W'))

print('间隔2天，5个数据'.ljust(30, '='))
print(pd.date_range(start='20190601', periods=5, freq='2D'))

print('间隔3小时，8个数据'.ljust(30, '='))
print(pd.date_range(start='20190601', periods=8, freq='3H'))

print('3:00开始，间隔1分钟，12个数据'.ljust(30, '='))
print(pd.date_range(start='201906010300', periods=12, freq='T'))

print('间隔1月，月末最后一天'.ljust(30, '='))
print(pd.date_range(start='20190101', end='20191231', freq='M'))

print('间隔1年，6个数据，年末最后一天'.ljust(30, '='))
print(pd.date_range(start='20190101', periods=6, freq='A'))

print('间隔1年，6个数据，年初第一天'.ljust(30, '='))
print(pd.date_range(start='20190101', periods=6, freq='AS'))

# 使用日期时间做索引，创建Series对象
data = pd.Series(index=pd.date_range(start='20190701', periods=24, freq='H'), data=range(24))
print('前5条数据'.ljust(30, '='))
print(data[:5])

print('3小时重采样，计算均值'.ljust(30, '='))
print(data.resample('3H').mean())

print('5小时重采样，求和'.ljust(30, '='))
print(data.resample('5H').sum())

# OHLC分别表示OPEN、HIGH、LOW、CLOSE
print('5小时重采样，统计OHLC值'.ljust(30, '='))
print(data.resample('5H').ohlc())

print('所有日期替换为第二天'.ljust(20,'='))
data.index = data.index + pd.Timedelta('1D')
print(data[:5])

print('查看指定日期是周几'.ljust(20,'='))
#print(pd.Timestamp('20190323').weekday_name)
print(pd.Timestamp('20190323').day_name())

print('查看指定日期时间所在年是否闰年'.ljust(20,'='))
print(pd.Timestamp('201909300800').is_leap_year)

print('查看指定日期所在的季度和月份'.ljust(20,'='))
day = pd.Timestamp('20191025')
print(day.quarter, day.month)

print('转换为Python的日期时间对象'.ljust(20,'='))
print(day.to_pydatetime())