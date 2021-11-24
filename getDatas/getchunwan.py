#!/usr/bin/env python
# coding=utf-8

'''
从维基百科获得历年春晚数据
https://zh.wikipedia.org/wiki/1983%E5%B9%B4%E4%B8%AD%E5%9B%BD%E4%B8%AD%E5%A4%AE%E7%94%B5%E8%A7%86%E5%8F%B0%E6%98%A5%E8%8A%82%E8%81%94%E6%AC%A2%E6%99%9A%E4%BC%9A

参考
https://mp.weixin.qq.com/s/Zd1l-HM-wA1Wu3k3flB15g
'''

from urllib.parse import quote
import requests
import parsel


# 1.获取导演,主持名单


# keywords = quote('年中国中央电视台春节联欢晚会')
# year = 1983
# url = 'https://zh.wikipedia.org/wiki/{}{}'.format(year, keywords)
#
# response = pd.read_html(url)[1]
# response.to_csv('chinese_newyear.csv', mode='a', encoding='utf_8_sig', index=0, header=0)


# def get_content(year):
#     # 1 节目单； 0 节目信息
#     if year != 2014:
#         response = pd.read_html(url)[1]
#
#     else:
#         response = pd.read_html(url)[3]
#         response['year'] = year
#         response.drop([0], inplace=True)  # 删除首行
#         response.to_csv('chinese_newyear.csv', mode='a', encoding='utf_8_sig', index=0, header=0)


def get_requests(url, encoding='utf-8', timeout=10):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/90.0.4430.93 Safari/537.36",
    }

    res = requests.get(url=url, headers=headers, timeout=timeout)
    res.encoding = encoding

    return res.text


if __name__ == '__main__':
    keywords = quote('年中国中央电视台春节联欢晚会')
    url = 'https://zh.wikipedia.org/wiki/1983{}'.format(keywords)
    get_requests(url)
