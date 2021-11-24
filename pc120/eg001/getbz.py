#!/usr/bin/env python
# coding=utf-8

'''
001号
壁纸爬取
http://www.netbian.com/fengjing/
'''

import requests
import parsel

url = 'http://www.netbian.com/fengjing/'
wurl = 'http://www.netbian.com'


# 获得分页url地址列表
def urls():
    url_list = ['http://www.netbian.com/fengjing/index_{}.htm'.format(i) for i in range(2, 3)]
    url_list.insert(0, url)
    return url_list


# 组装sel对象
def t_sel(url):
    response = requests.get(url)
    sel = parsel.Selector(response.content.decode('gbk'))
    return sel


# 清洗组装获得高清地址
def clearurl(lists):
    nurls = []
    for i in lists:
        # print(i)
        if i.startswith('/desk/'):
            i = wurl + i[:-4] + '-1920x1080.htm'
            nurls.append(i)
    return nurls


# 获取并保存图片
def savepic(gqurls):
    for g_url in gqurls:
        sel = t_sel(g_url)
        gpic = sel.css('td a::attr(href)').extract_first()
        image = requests.get(gpic).content
        with open('../eg001/' + str(g_url[28:-4]) + '.jpg', 'wb') as f:
            f.write(image)


if __name__ == '__main__':
    ulist = urls()
    for url in ulist:
        sel = t_sel(url)
        lists = sel.css('.list li a::attr(href)').extract()  # 获得初始地址
        gqurls = clearurl(lists)
        savepic(gqurls)
