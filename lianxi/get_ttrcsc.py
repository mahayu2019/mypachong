#!/usr/bin/env python
# coding=utf-8
'''
天台人才市场爬虫
http://www.ttrcsc.com/
检索页
http://www.ttrcsc.com/sousuo/Company.asp?Position_b=&Position_s=&Qualification=&Province=%CC%EC%CC%A8%CF%D8&City=%C6%BD%C7%C5%D5%F2&County=%B2%BB%CF%DE&ValidityDate=&qiyess=1&keyword=%C7%EB%CA%E4%C8%EB%B9%D8%BC%FC%B4%CA%A3%AC%C8%E7%D6%B0%CE%BB
'''

import requests
import parsel

urls = ['http://www.ttrcsc.com/sousuo/Company.asp?'
        'Position_b=&Position_s=&Qualification=&'
        'Province=%CC%EC%CC%A8%CF%D8&City=%C6%BD%C7%C5%D5%F2&'
        'County=%B2%BB%CF%DE&ValidityDate=&qiyess=1&keyword=&page={}'.format(i) for i in range(8)]
for url in urls:
    response = requests.get(url)

    sel = parsel.Selector(response.content.decode('gb2312'))
    li = sel.css('.zxzwlbz div.zxzwlb')

    for work in li:
        w_title = work.css('a.lsd::text').extract_first()
        w_comp = work.css('a.ls::text').extract_first()
        w_mony = work.css('.zwa4::text').extract_first()
        w_time = work.css('.zwa5::text').extract_first()
        w_sex = work.css('.zwa7 span::text').extract()[3]
        w_num = work.css('.zwa7 span::text').extract()[4]
        w_ms = work.css('.zwa8::text').extract_first()
        print('职位:', w_title, '\n公司:', w_comp, '薪酬:', w_mony, '发布日期:',
              w_time, '\n' + w_sex,w_num, '\n' + w_ms + '\n')
