#!/usr/bin/env python
# coding=utf-8

# 正则分组练习
import re

html = """
<div class="animal">
    <p class="name">
        <a title="Tiger"></a>
    </p>
    <p class="content">
        Two tiger two tiger run fast
    </p>>
</div>

<div class="animal">
    <p class="name">
        <a title="Rabbit"></a>
    </p>
    <p class="content">
        Small white rabbit white and white
    </p>
</div>    
"""


html2="""
<div class="movie-item-info">
        <p class="name"><a href="/films/1200486" title="我不是药神" data-act="boarditem-click" data-val="{movieId:1200486}">我不是药神</a></p>
        <p class="star">
                主演：徐峥,周一围,王传君
        </p>
<p class="releasetime">上映时间：2018-07-05</p>    </div>

"""
# 删除部分用.*?代替,取值需要加上()
regex = '<div class="animal">.*?<a title="(.*?)">.*?<p class="content">(.*?)</p>'
reg2 = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'

pattern = re.compile(reg2, re.S)
r_list = pattern.findall(html2)
print(r_list)

print('-' * 50)
for st in r_list:
    print('动物名称:', st[0].strip())
    print('描述:', st[1].strip())  # strip()过滤多余空白换行等字符
    print('*' * 50)
