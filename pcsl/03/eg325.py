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

# xpath的高级用法
# 提取li标签中属性以item开头(starts-with)的文本
li_1_5 = selector.xpath('//li[starts-with(@class,"item-")]/a/text()')

# 提取ul标签下所有层级的文本
all_text = selector.xpath('string(//ul)')

print(li_1_5)
print([s.strip() for s in all_text.strip().split('\n')])
