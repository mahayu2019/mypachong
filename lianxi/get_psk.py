#!/usr/bin/env python
# coding=utf-8
'''
psk网站提取
'''

import requests
import parsel


# 解析内部页面的链接地址
def conts(urls):
    x = []
    for u in urls:
        response = requests.get(u)
        sel = parsel.Selector(response.content.decode('utf-8'))
        dz = sel.css('p a::attr(href)').extract_first()
        x.append(dz)
    return x


url = 'https://www.gotopsk.com/rihan'

response = requests.get(url)
sel = parsel.Selector(response.content.decode('utf-8'))
# li_title_a = sel.css('h2 a::text,h2 a::attr(href)').extract() #同时提取多个目标参数
# li_title = sel.css('h2 a::text').extract()
li_a = sel.css('h2 a::attr(href)').extract()
# print(li_title_a)
# print(li_title)
# print(li_a)

'''
拼接两个list为字典
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
https://www.runoob.com/python/python-func-zip.html
keys = ['name', 'age', 'food']
values = ['Monty', 42, 'spam']
a_dict = dict(zip(keys, values))
print(a_dict)
'''
# a_dict=dict(zip(li_title,li_a))
# print(a_dict)

tt = conts(li_a)
print(tt)
