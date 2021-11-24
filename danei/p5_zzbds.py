#!/usr/bin/env python
# coding=utf-8

# 正则表达式
import re

html = """
<div><p>贪婪模式和非贪婪模式,区别在于此</p></div>
<div><p>啥口气和情况还得分</p></div>
"""

# 贪婪匹配演示:
pattern = re.compile('<div><p>.*</p></div>', re.S)
r_list = pattern.findall(html)
print(r_list,re.S)

# 非贪婪匹配演示:
pattern = re.compile('<div><p>.*?</p></div>', re.S)
r_list = pattern.findall(html)
print(r_list)

# 正则表达式分组
st = 'A B C D'
pattern = re.compile('\w+\s+\w+')
r_list = pattern.findall(st)
print(r_list)
# 输出: ['A B', 'C D']

pattern = re.compile('(\w)+\s+\w+')
r_list = pattern.findall(st)
print(r_list)
# 输出: ['A', 'C']
# 过程: ['A B', 'C D']--->分组'(\w)+\s+\w+'--->['A', 'C']

pattern = re.compile('(\w)+\s+(\w+)')
r_list = pattern.findall(st)
print(r_list)
# 输出: [('A', 'B'), ('C', 'D')]
# 过程: ['A B', 'C D']--->分组'(\w)+\s+(\w+)'--->[('A', 'B'), ('C', 'D')]
