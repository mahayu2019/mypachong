#!/usr/bin/env python
# coding=utf-8

import csv

'''
csv模块示例
'''

# writerow 一次只写入一行
with open('pachong.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['阿三', '爬虫'])

clines = [
    ('大雄', '主角'),
    ('哆啦A梦', '机器猫'),
    ('静子', '美女')
]

# 一次写入多行
with open('pachong.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(clines)
