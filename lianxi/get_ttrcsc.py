#!/usr/bin/env python
# coding=utf-8
'''
天台人才市场爬虫
http://www.ttrcsc.com/
检索页
http://www.ttrcw.com.cn/job?jobarea1=33102301
'''

import requests
import parsel

urls = ['http://www.ttrcw.com.cn/job?page={}'.format(i) for i in range(106)]

for url in urls:
    response = requests.get(url)

    sel = parsel.Selector(response.content.decode('utf-8'))
    li = sel.css('.job_display_left .saith')

    for work in li:
        w_title = work.css('.list1 a::text').extract_first()
        w_comp = work.css('.list4 a::text').extract_first()
        w_mony = work.css('.list2::text').extract_first()
        w_time = work.css('.list2.son_list2_refont::text').extract_first()
        print('职位:', w_title, '\n公司:', w_comp, '薪酬:', w_mony, '发布日期:',
              w_time)
