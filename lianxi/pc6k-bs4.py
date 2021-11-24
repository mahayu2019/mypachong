#!/usr/bin/env python
# coding=utf-8

# 练习源码,参照fishc下的jk01.py
# 用bs4尝试爬取6v电影网站部分列表

import requests
import bs4

myhead = {
    'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) '
                  'AppleWebKit / 537.36(KHTML, like Gecko) '
                  'Chrome / 88.0.4324.150 Safari / 537.36',
}

url = 'http://www.hao6v.com/'

res = requests.get(url, headers=myhead)
res.encoding = 'gb2312'  # 指定编码,避免中文输出乱码

soup = bs4.BeautifulSoup(res.text, 'html.parser')
targets = soup.find_all('ul', class_='lt')

# print('爬取最新电影的列表:')
for each in targets:
    # print(each.li.span)  # 待完善...标签span无法去除html标记取值
    print(each.li.a.text)
