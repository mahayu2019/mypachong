#!/usr/bin/env python
# coding=utf-8

# 案例3.4抓取猫眼电影排行 P150
import json
import re

import requests


def get_one_page(url):
    headers = {'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) '
                             'AppleWebKit / 537.36(KHTML, like Gecko) '
                             'Chrome / 88.0.4324.150 Safari / 537.36', }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    reg = '<dd>.*?board-index-(.*?)">.*?title="(.*?)".*?<p class="star">.*?(.*?)</p>.*?class="releasetime">(.*?)</p>.*?class="integer">(.*?)</i><i class="fraction">(.*?)</i>'
    pattern = re.compile(reg, re.S)
    r_list = pattern.findall(html)
    # print(r_list)

    for t in r_list:
        print(t[0], t[1], t[2].strip(), t[3], '得分:', t[4] + t[5])

    return r_list

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main():
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    # print(html)
    # parse_one_page(html)
    for item in parse_one_page(html):
        write_to_file(item)


main()
