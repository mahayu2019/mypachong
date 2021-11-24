#!/usr/bin/env python
# coding=utf-8

# 获取网页的编码charset,用于设置res的encoding避免乱码
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
print(res.text)
