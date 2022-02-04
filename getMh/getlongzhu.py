#!/usr/bin/env python
# coding=utf-8

'''
抓取爱奇艺漫画,初步完成
'''

import time
import requests
import pandas as pd
from lxml import etree

url = 'https://www.iqiyi.com/manhua/reader/18yzlq6qr9_18yzef4jhl.html'

headers = {
    'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) '
                  'AppleWebKit / 537.36(KHTML, like Gecko) '
                  'Chrome / 88.0.4324.150 Safari / 537.36',
}

response = requests.get(url=url, headers=headers)
html = etree.HTML(response.text)

#取得图片地址
href1 = html.xpath("/html/body/div[2]/ul/li/img/@src")
href2 = html.xpath("/html/body/div[2]/ul/li/img/@data-original")

# print(href1)
print(href2)

index=1
for img_url in href2:
    image = requests.get(img_url)
    with open('./'+str(index)+'.webp', mode='wb') as f:
        f.write(image.content)
    index=index+1