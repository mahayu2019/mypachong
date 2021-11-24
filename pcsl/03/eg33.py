#!/usr/bin/env python
# coding=utf-8
import requests
from lxml import etree

# 抓取百度首页新闻标题及链接

response = requests.get('https://www.baidu.com')
response.encoding = 'utf-8'
selector = etree.HTML(response.text)

title = selector.xpath('//*[@id="u1"]/a[1]/text()')[0]  # id在实际网页中不存在?
# 实际获得的xpath如下所示:
# //*[@id="s-top-left"]/a[1]

print(title)
