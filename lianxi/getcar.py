#!/usr/bin/env python
# coding=utf-8

'''
懂车帝xpath爬取测试
https://www.dongchedi.com/auto/library/0,10-0-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
'''

import time
import requests  # 请求库
import pandas as pd
from lxml import etree  # 提取信息库

# 日期
today = time.strftime('%Y{y}%m{m}%d{d}', time.localtime()).format(y='年', m='月', d='日')
# 网址
url = 'https://www.dongchedi.com/auto/library/0,10-0-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x'
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
# 发送请求
response = requests.get(url=url, headers=headers)
# 数据解析,xpath可以用浏览器检查元素获得
html = etree.HTML(response.text)  # 类型变换

titles = html.xpath('//*[@id="__next"]/div[1]/div[2]/div[1]/div/div[2]/section/div[7]/ul/li/a/p[1]/text()')

print(titles)