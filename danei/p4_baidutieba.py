#!/usr/bin/env python
# coding=utf-8

# 抓取百度贴吧案例,抓取并保存到本地

from urllib import request, parse
import time
import random


class BaiduTieBaSpider:
    def __init__(self):
        """定义常用变量"""
        self.url = 'https://tieba.baidu.com/f?kw={}&pn={}'
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


def parse_html(self):
    """解析提取数据"""
    pass


def save_html(self, filename, html):
    """数据处理"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


def run(self):
    """程序入口,整体调控"""
    name = input("请输入贴吧名称:")
    start = int(input("请输入起始页:"))
    end = int(input("请输入结束页:"))
    params = parse.quote(name)  # 对中文进行编码
    # 1 拼接URL地址
    for page in range(start, end + 1):
        pn = (page - 1) * 50
        url = self.url.format(params, pn)  # format字符串格式化函数
        # format 参阅:https://www.runoob.com/python/att-string-format.html

        # 发请求,解析,保存
        html = self.get_html(url)
        filename = '{}_第{}页.html'.format(name, page)
        self.save_html(filename, html)
        # 终端打印提示
        print('第%d页抓取成功' % page)
        # 控制抓取频率,随机停顿1-2秒
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    spider = BaiduTieBaSpider()
    spider.run()
