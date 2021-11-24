#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup

# BeautifulSoup 基本用法

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

soup = BeautifulSoup(htm, 'lxml')
print(soup.ul)
print(soup.li)
print(soup.a.string)
print(soup.a['href'])