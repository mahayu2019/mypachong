#!/usr/bin/env python
# coding=utf-8

'''
hao6v电影列表爬取
'''
import requests
import parsel

url = 'http://www.hao6v.com/'
response = requests.get(url)
sel = parsel.Selector(response.content.decode('gb2312'))
news = sel.css('.lt li a::text,.lt li a font::text').extract()[:17]  # 最新电影列表含有特殊修饰
for t in news:
    print(t)
