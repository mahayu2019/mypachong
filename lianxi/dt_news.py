#!/usr/bin/env python
# coding=utf-8

'''
动态新闻抓取初步,演练json
'''

import requests
import json

urls = ['https://www.ptpress.com.cn/newsInfo/getNewsInfoList4Portal?rows=16&page={}&type=news'
            .format(i + 1) for i in range(12)]
for url in urls:
    res = requests.get(url).text
    data = json.loads(res)
    news = data['data']['rows']
    for n in news:
        n_title = n['mainTitle']
        n_date = n['newsDate']
        print(n_title, n_date)
