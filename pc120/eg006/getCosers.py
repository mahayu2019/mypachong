#!/usr/bin/env python
# coding=utf-8

'''
标的:http://www.cosplay8.com/pic/chinacos/
'''

import re
import os
import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/90.0.4430.85 Safari/537.36",
    "host": 'www.cosplay8.com'
}


# 爬取页列表
def run(category, start, end):
    wait_url = [
        f'http://www.cosplay8.com/pic/chinacos/list_{category}_{i}.html' for i in range
        (int(start), int(end) + 1)
    ]
    print(wait_url)

    url_list = []
    for item in wait_url:
        ret = get_list(item)

        print(f'已抓取:{len(ret)}条数据')
        url_list.extend(ret)
    # print(url_list)
    for url in url_list:
        get_detial(f'http://www.cosplay8.com{url}')


def get_list(url):
    # 获取全部详情页连接
    all_list = []
    res = requests.get(url, headers=headers)
    html = res.text
    pattern = re.compile('<li><a href="(.*?)">')
    all_list = pattern.findall(html)
    return all_list


def get_detial(url):
    # 获得详情页数据
    res = requests.get(url=url, headers=headers)
    # 设置编码
    res.encoding = 'utf-8'
    # 获得网页源码
    html = res.text

    # 拆解源码,获得第一张图片
    size_pattern = re.compile('<span>共(\d+)页: </span>')
    # 获取标题
    title_pattern = re.compile('<title>(.*?)-Cosplay(中国|8)</title>')
    # 设置图片正则表达式
    first_img_pattern = re.compile("<img src='(.*?)' id='bigimg'")

    try:
        # 尝试匹配页码
        page_size = size_pattern.search(html).group(1)
        # 尝试匹配标题
        title = title_pattern.search(html).group(1)
        # 尝试匹配地址
        first_img = first_img_pattern.search(html).group(1)

        print(f'URL对应的数据为{page_size}页', title, first_img)
        # 生成路径
        path = f'images/{title}'

        # 路径判断
        if not os.path.exists(path):
            os.makedirs(path)

        # 抓取第一张图片
        save_image(path, title, first_img, 1)

        # 抓取更多图片
        urls = [f'{url[0:url.rindex(".")]}_{i}.html'
                for i in range(2, int(page_size) + 1)]

        for index, child_url in enumerate(urls):
            try:
                res = requests.get(url=child_url, headers=headers)
                html = res.text
                first_img_pattern = re.compile("<img src='(.*?)' id='bigimg'")
                first_img = first_img_pattern.search(html).group(1)
                save_image(path, title, first_img, index)
            except Exception as e:
                print('抓取子页', e)
        # 抓取更多图片
    except Exception as e:
        print(url, e)


def save_image(path, title, first_img, index):
    try:
        # 抓取图片
        img_res = requests.get(f'http://www.cosplay8.com{first_img}', headers=headers)
        img_data = img_res.content

        with open(f'{path}/{title}_{index}.png', 'wb+') as f:
            f.write(img_data)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    category = input('分类编号:')
    start = input('起始页:')
    end = input('结束页:')
    run(category, start, end)
