#!/usr/bin/env python
# coding=utf-8

'''
pandas一行代码爬取数据,仅限于table元素的数据读取
原文:https://mp.weixin.qq.com/s/5o5uecuEge12zTyQEplx2g

'''

import pandas as pd

data = pd.read_html('https://www.fortunechina.com/fortune500/c/2018-07/19/content_311046.htm')
print(data)

#以下案例无效
# d2=pd.read_html('https://detail.zol.com.cn/motherboard/pic.html')
# print(d2)
