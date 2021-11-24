#!/usr/bin/env python
# coding=utf-8

'''
目标:
https://m.weibo.cn/u/3181375120
参考老崔的爬虫开发实战第六章案例

'''

import requests
from urllib.parse import urlencode

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/3181375120',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                  'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                  'Chrome/94.0.4606.54 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}


# 组装ajax请求地址
def get_page(page):
    params = {
        'type': 'uid',  # 定值
        'value': '3181375120',  # 用户id
        'containerid': '1076033181375120',  # 容器,定值
        'page': page,  # 翻页id,初始0

    }
    url = base_url + urlencode(params)
    # print(url)
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        return res.json()


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog').get('text')
            print(item)



if __name__ == '__main__':
    json = get_page(1)
    parse_page(json)
