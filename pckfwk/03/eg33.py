#!/usr/bin/env python
# coding=utf-8

import re
import csv

with open('source.txt', 'r', encoding='utf-8') as f:
    source = f.read()

result_list = []
username_list = re.findall('username="(.*?)"', source, re.S)
content_list = re.findall('j_d_post_content.*?">(.*?)<', source, re.S)
#reply_time_list = re.findall('span">2021(.*?)', source, re.S)

for i in range(len(username_list)):
    result = {'username': username_list[i], 'content': content_list[i]}
    result_list.append(result)

with open('tieba.csv', 'w', encoding='UTF-8') as f:
    write = csv.DictWriter(f, fieldnames=['username', 'content'])
    write.writeheader()
    write.writerows(result_list)
