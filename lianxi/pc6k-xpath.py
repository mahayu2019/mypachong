#!/usr/bin/env python
# coding=utf-8
from lxml import etree

# xpath提取www.hao6v.com电影名称列表
import requests

myhead = {
    'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) '
                  'AppleWebKit / 537.36(KHTML, like Gecko) '
                  'Chrome / 88.0.4324.150 Safari / 537.36',
}

url = 'http://www.hao6v.com/'

res = requests.get(url, headers=myhead)
res.encoding = 'gb2312'  # 指定编码,避免中文输出乱码

selector = etree.HTML(res.text)
titles = selector.xpath('//*[@class="box"]/ul/li/a/text()')
# print(titles)
for t in titles:
    print(t)  # 提取值过多,待改善
