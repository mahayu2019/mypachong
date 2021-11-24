#!/usr/bin/env python
# coding=utf-8
from lxml import etree

htm = """
    <div>
        <ul>
            <li class="item-0"><a href="link1.html">first item</a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-inactive"><a href="link3.html">third item</a></li>
            <li class="item-1"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
            <li class="else-0">else item</li>
            another item
        <ul>
    </div>
"""

selector = etree.HTML(htm)

# 通过路径查找元素
all_li = selector.xpath('//div/ul/li')  # 注意是反斜杠
li_1 = selector.xpath('//div/ul/li[1]')  # 选择列表元素下标序号,从1开始
li_1_a_text = selector.xpath('//div/ul/li[3]/a/text()')  # 获取链接的文本
a_text = selector.xpath('//ul/li[3]/a/text()')[0]  # ul在此处是唯一的,所以可以省略div标签,最后用下标取出文本值

print(all_li)
print(li_1)
print(li_1_a_text)
print(a_text)
