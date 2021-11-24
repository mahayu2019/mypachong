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

# 提取属性的值 @属性名称
selector = etree.HTML(htm)

li_3_a_href = selector.xpath('//ul/li[3]/a/@href')[0]  # 提取第三个li下的a标签的链接属性值
all_class = selector.xpath('//li/@class')  # 取出所有li下的class的属性值

print(li_3_a_href)
print(all_class)
