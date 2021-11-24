#!/usr/bin/env python
# coding=utf-8

'''
漫画图片抓取,保存到本地
'''

from urllib import request, parse
import requests
import re
import os
import time

# 图片地址
# https://image.xmanhua.com/1/73/10344/18_3662.jpg?cid=10344&key=4b5c1d8945a25d020384895c4bf50a40&uk=
# 序列号地址
mh_url = 'https://image.xmanhua.com/1/73/10344/1_8453.jpg?cid=10344&key=615a5e79599a9d6999c854a20ffe0de0&uk='
headers = {
    'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) '
                  'AppleWebKit / 537.36(KHTML, like Gecko) '
                  'Chrome / 88.0.4324.150 Safari / 537.36',
}

# 1.content属性:获取byters数据类型
# html = requests.get(url=mh_url, headers=headers).content

# # 2. 确定图片保存路径
# directory = './images/'
# if not os.path.exists(directory):
#     os.makedirs(directory)
#
# # 3.保存到本地文件,filename:./images/xxxx.jpg
# filename = directory + mh_url[37:47]
# with open(filename, 'wb') as f:
#     f.write(html)

# count = 24
# while (count < 27):
#     url = 'https://www.xmanhua.com/m10344-p1/chapterimage.ashx?cid=10344&page=' + str(
#         count) + '&key=&_cid=10344&_mid=73&_dt=2021-06-27+15%3A19%3A55&_sign=9af1c899d97983e0e702d4837e75f59f'
#     req = request.Request(url=url, headers=headers)
#     res = request.urlopen(req)
#     html = res.read().decode()
#     print(html[587:595])
#     count = count + 1
#     time.sleep(5)

# reg = '<ul.*?target="_blank">(.*?)</a>.*?"list2">(.*?)</li>.*?"_blank">(.*?)</a>'
# pattern = re.compile(reg, re.S)
# r_list = pattern.findall(html)


# 逐行读取
filename = 'mhid.txt'
ids = []
with open(filename) as file_object:
    for line in file_object:
        data = file_object.read().splitlines()
        print(data)
    # ids.append(data)

# print(ids)
