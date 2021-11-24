#!/usr/bin/env python
# coding=utf-8

'''
ZOL数据获取
主板报价信息完成首页获取
'''

import requests
import parsel

# 主板报价
url = 'https://detail.zol.com.cn/motherboard/pic.html'

response = requests.get(url)

sel = parsel.Selector(response.content.decode('gbk'))
lists = sel.css('.list-box .list-item.clearfix')

num = 0
for item in lists:
    mc = item.css('h3 a::text,.param.clearfix li::attr(title)').extract_first()
    xp = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[1]
    cpu = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[2]
    cpu_type = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[3]
    memo_type = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[4]
    jcxp = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[5]
    xk = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[6]
    zblx = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[7]
    jg = item.css('.price-type::text').extract()[0]
    num = num + 1
    print(num,
          '名称:', mc,
          '主芯片组:', xp,
          'CPU插槽:', cpu,
          'CPU类型:', cpu_type,
          '内存类型:', memo_type,
          '集成芯片:', jcxp,
          '显示芯片:', xk,
          '主板板型:', zblx,
          '报价:', jg)
