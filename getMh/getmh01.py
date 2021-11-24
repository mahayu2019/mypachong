#!/usr/bin/env python
# coding=utf-8

'''
爬取酷爱漫画网站--目标网址
https://www.kuimh.com/book/mh7614
'''

import requests
import parsel

url = 'https://www.kuimh.com/chapter/189114-1610004'
response = requests.get(url)
data_html = response.text

selector = parsel.Selector(data_html)
sub_url_list = selector.css('.comicpage div img::attr(src)').getall()[:3]
sub_list = selector.css('.comicpage div img::attr(data-echo)').getall()

for i in sub_list:
    sub_url_list.append(i)
    print(sub_url_list)

index = 1
for img_url in sub_url_list:
    image = requests.get(img_url).content
    with open('./密保01/' + '第' + str(index) + '页.jpg', mode='wb') as f:
        f.write(image)
    index += 1
