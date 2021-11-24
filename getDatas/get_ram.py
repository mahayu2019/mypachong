#!/usr/bin/env python
# coding=utf-8

'''
ZOL数据获取
内存报价信息
'''

import requests
import re
import parsel

# 内存报价
url = 'https://detail.zol.com.cn/memory/zhejiang/pic.html'

response = requests.get(url)

sel = parsel.Selector(response.content.decode('gbk'))
lists = sel.css('.list-box .list-item.clearfix')

num = 0
for item in lists:
    mc = item.css('h3 a::text,.param.clearfix li::attr(title)').extract_first()
    cap = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[1]
    sytype = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[2]
    jklx = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[3]
    zs = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[4]
    hc = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[5]
    jksl = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[6]
    size = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[7]
    jg = item.css('.price-type::text').extract()[0]
    num = num + 1
    print(num,
          '名称:', mc,
          '容量:', cap,
          '适用类型:', sytype,
          '接口类型:', jklx,
          '转速:', zs,
          '缓存:', hc,
          '接口速率:', jksl,
          '尺寸:', size,
          '报价:', jg)
