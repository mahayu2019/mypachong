#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup

# 2.3.1 获取页面
link = "http://www.santostang.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
           }
r = requests.get(link, headers=headers)
print(r.text)

soup = BeautifulSoup(r.text, 'lxml')
title = soup.find("h1", class_="post-title").a.text.strip()
print(title)

# 2.3.3 存储数据
with open('title.txt', "a+") as f:
    f.write(title)
    f.close()
