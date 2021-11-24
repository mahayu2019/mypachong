#!/usr/bin/env python
# coding=utf-8

# B站极客python之效率革命--爬取豆瓣豆瓣top250电影标题简单实例

import requests
import bs4

myhead = {
    'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) '
                  'AppleWebKit / 537.36(KHTML, like Gecko) '
                  'Chrome / 88.0.4324.150 Safari / 537.36',
}
url = 'https://movie.douban.com/top250'

res = requests.get(url, headers=myhead)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
targets = soup.find_all("div", class_="hd")
for each in targets:
    print(each.a.span.text)
