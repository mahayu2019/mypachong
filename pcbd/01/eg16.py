#!/usr/bin/env python
# coding=utf-8

import requests
import parsel
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.news
collection = db.phei

url = 'https://www.phei.com.cn/xwxx/index.shtml'

urls = ['https://www.phei.com.cn/xwxx/index_{}.shtml'.format(i + 1) for i in range(54)]
urls.append(url)
# print(urls)

for u in urls:
    resp = requests.get(u)
    sel = parsel.Selector(resp.content.decode('utf8'))
    li = sel.css('.web_news_list ul li.li_b60')
    for news in li:
        title = news.css('p.li_news_title::text').extract_first()
        pub_time = news.css('span::text').extract_first()
        desc = news.css('p.li_news_summary::text').extract_first()
        img = news.css('div.li_news_line img::attr("src")').extract_first()
        # print('-----')
        # print(title, pub_time, desc, img)
        collection.insert_one({'title': title, 'pub_time': pub_time, 'desc': desc, 'image:': img})
