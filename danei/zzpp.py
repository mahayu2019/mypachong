#!/usr/bin/env python
# coding=utf-8


"""
<ul class="son_ul father_ul1_position">.*?target="_blank">(.*?)</a>.*?<li class="list2">(.*?)</li>.*?target="_blank">(.*?)</a>"""
import re

html = """
<ul class="son_ul father_ul1_position">
                                            <li class="list1"><a href="http://www.ttrcw.com.cn/jobinfo_5a464930562.html" target="_blank">外贸业务员</a>
                                                                                                </li>
                                            <li class="list2">3000-1万</li>
                                            <li class="list4"><a href="http://www.ttrcw.com.cn/comabout_b611c07618.html" target="_blank">浙江何升工具股份有限公司</a></li>
                                                                                    </ul>
"""

reg = '<ul.*?target="_blank">(.*?)</a>.*?"list2">(.*?)</li>.*?"_blank">(.*?)</a>'

htmlmaoyan = """
<dd>
                        <i class="board-index board-index-1">1</i>
    <a href="/films/1200486" title="我不是药神" class="image-link" data-act="boarditem-click" data-val="{movieId:1200486}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default">
      <img alt="我不是药神" class="board-img" src="https://p0.meituan.net/movie/414176cfa3fea8bed9b579e9f42766b9686649.jpg@160w_220h_1e_1c">
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1200486" title="我不是药神" data-act="boarditem-click" data-val="{movieId:1200486}">我不是药神</a></p>
        <p class="star">
                主演：徐峥,周一围,王传君
        </p>
<p class="releasetime">上映时间：2018-07-05</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">6</i></p>        
    </div>

      </div>
    </div>

                </dd>
"""
reg = '<dd>.*?board-index-(.*?)">.*?title="(.*?)".*?<p class="star">.*?(.*?)</p>.*?class="releasetime">(.*?)</p>.*?class="integer">(.*?)</i><i class="fraction">(.*?)</i>'
pattern = re.compile(reg, re.S)
r_list = pattern.findall(htmlmaoyan)
print(r_list)

for t in r_list:
    print(t[0], t[1], t[2].strip(), t[3], '得分:', t[4] + t[5])

"""
<dd>.*?board-index-(.*?)">.*?title="(.*?)".*?<p class="star">.*?(.*?).*?class="releasetime">(.*?)</p>.*?class="integer">(.*?)</i><i class="fraction">(.*?)</i>
"""
