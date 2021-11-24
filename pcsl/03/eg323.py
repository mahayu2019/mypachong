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

# 通过属性来查找元素

li_3 = selector.xpath('//ul/li[@class="item-inactive"]')  # 注意属性标示@class前没有反斜杠
li_3_2 = selector.xpath('//*[@class="item-inactive"]')  # 因为此元素唯一,可用通配符指定
li_a_text = selector.xpath('//*[@class="item-inactive"]/a/text()')  # 属性后续可接下级标签
li_4_a_text = selector.xpath('//*/a[@href="link4.html"]/text()')[0]

print(li_3)
print(li_3_2)
print(li_a_text)
print(li_4_a_text)
