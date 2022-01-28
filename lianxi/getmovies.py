#!/usr/bin/env python
# coding=utf-8

'''
案例参考
'''
import time
import requests  # 请求库
import pandas as pd
from lxml import etree  # 提取信息库

# 日期
today = time.strftime('%Y{y}%m{m}%d{d}', time.localtime()).format(y='年', m='月', d='日')
# 网址
url = 'https://movie.douban.com/cinema/later/shenzhen/'
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
# 发送请求
response = requests.get(url=url, headers=headers)
# 数据解析,xpath可以用浏览器检查元素获得
html = etree.HTML(response.text)  # 类型变换
# 电影详细超链接
href = html.xpath('//*[@id="showing-soon"]/div/div/h3/a/@href')
# 上映日期
Ondate = html.xpath('//*[@id="showing-soon"]/div/div/ul/li[1]/text()')
# 片名
name = html.xpath('//*[@id="showing-soon"]/div/div/h3/a/text()')
# 类型
movie_class = html.xpath('//*[@id="showing-soon"]/div/div/ul/li[2]/text()')
# 制片国家 / 地区
area = html.xpath('//*[@id="showing-soon"]/div/div/ul/li[3]/text()')
# 想看人数
num = html.xpath('//*[@id="showing-soon"]/div/div/ul/li[4]/span/text()')
# 利用pandas保存文件
df = pd.DataFrame()
df['上映日期'] = Ondate
df['片名'] = name
df['类型'] = movie_class
df['制片国家/地区'] = area
df['想看人数'] = num
df['超链接'] = href
df.to_csv('2022春节档电影_' + today + '.csv', mode='w', index=None, encoding='gbk')
print('保存完成!')
