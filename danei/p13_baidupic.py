#!/usr/bin/env python
# coding=utf-8

'''
百度图片抓取,保存到本地
'''

import requests
import os

img_url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwx4.sinaimg.cn%2Fmw690%2F8397d3c0ly1gripyiq59wg20tr0ts1l7.gif&refer=http%3A%2F%2Fwx4.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1627191155&t=319116ebaa19c0184d58fc36adfd738f.jpg'
headers = {
    'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) '
                  'AppleWebKit / 537.36(KHTML, like Gecko) '
                  'Chrome / 88.0.4324.150 Safari / 537.36',
}

# 1.content属性:获取byters数据类型
html = requests.get(url=img_url, headers=headers).content

# 2. 确定图片保存路径
directory = './images/'
if not os.path.exists(directory):
    os.makedirs(directory)

# 3.保存到本地文件,filename:./images/xxxx.jpg
filename = directory + img_url[-10:]
with open(filename, 'wb') as f:
    f.write(html)
