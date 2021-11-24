#!/usr/bin/env python
# coding=utf-8

from lxml import etree
import requests
import csv
import time

# 代码效果未完成...

def spider():
    # 定义头部
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
               }
    pre_url = 'https://shenzhen.qfang.com/sale/'
    html = requests.get(pre_url, headers=headers)
    for x in range(1,2):
        html = requests.get(pre_url + str(x), headers=headers)
        time.sleep(2)
        selector = etree.HTML(html.text)
        list=selector.xpath('//*[@id="cycleListings"]/ul/li')
    print(list)

spider()
