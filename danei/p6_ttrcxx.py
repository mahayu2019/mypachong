#!/usr/bin/env python
# coding=utf-8

# 正则提取天台人才网招聘信息

from urllib import request, parse
import time
import random
import re


class MaoYanTop100Spider:
    def __init__(self):
        """定义常用变量"""
        self.url = 'http://www.ttrcw.com.cn/job?jobarea1=33102301&page={}'
        self.header = {
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) '
                          'AppleWebKit / 537.36(KHTML, like Gecko) '
                          'Chrome / 88.0.4324.150 Safari / 537.36',
        }

    def get_html(self, url):
        """获取响应内容"""
        req = request.Request(url=url, headers=self.header)
        res = request.urlopen(req)
        html = res.read().decode()

        return html

    def parse_html(self, html):
        """解析提取数据"""
        reg = '<ul.*?target="_blank">(.*?)</a>.*?"list2">(.*?)</li>.*?"_blank">(.*?)</a>'
        pattern = re.compile(reg, re.S)
        r_list = pattern.findall(html)
        return r_list

    def save_html(self, filename, html):
        """数据处理"""
        pass

    def run(self):
        """程序入口,整体调控"""
        # 1 拼接URL地址
        for page in range(1, 5):
            url = self.url.format(page)  # format字符串格式化函数
            #print(url)
            # 2 发请求,解析,保存
            html = self.get_html(url)
            lists = self.parse_html(html)
            for x in lists:
                print('职位名称:', x[0])
                print('薪酬:', x[1])
                print('公司名称:', x[2])
                print('~' * 50)

            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    spider = MaoYanTop100Spider()
    spider.run()
