#!/usr/bin/env python
# coding=utf-8

import requests, parsel

num = 3000

while (num < 3487):
    num += 1
    url = 'http://jindouyxt.com/Default/Content/' + str(num)

    response = requests.get(url)
    sel = parsel.Selector(response.content.decode('utf-8'))

    lists = sel.css('.article-tit h1')
    for item in lists:
        i = item.css('h1::text').extract()[0].strip()
        print(str(num) + ':' + i)
