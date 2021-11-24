#!/usr/bin/env python
# coding=utf-8
import re

# 练习懂车帝抓取
html = '''
<a target="_blank" class="jsx-4123353477" href="/auto/series/1145"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-1906909520 jsx-2292158439 img"></span></div><p title="轩逸" class="jsx-4123353477 name line-1">轩逸</p><p class="jsx-4123353477 price">8.48-13.80万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/649"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-3513598532 jsx-2292158439 img"></span></div><p title="哈弗H6" class="jsx-4123353477 name line-1">哈弗H6</p><p class="jsx-4123353477 price">8.30-15.09万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/414"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-960051342 jsx-2292158439 img"></span></div><p title="速腾" class="jsx-4123353477 name line-1">速腾</p><p class="jsx-4123353477 price">9.99-16.59万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/393"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-2544938023 jsx-2292158439 img"></span></div><p title="朗逸" class="jsx-4123353477 name line-1">朗逸</p><p class="jsx-4123353477 price">7.39-13.59万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/276"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-2520280493 jsx-2292158439 img"></span></div><p title="思域" class="jsx-4123353477 name line-1">思域</p><p class="jsx-4123353477 price">11.49-16.49万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/3476"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-870569848 jsx-2292158439 img"></span></div><p title="星瑞" class="jsx-4123353477 name line-1">星瑞</p><p class="jsx-4123353477 price">11.37-15.27万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/542"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-511033205 jsx-2292158439 img"></span></div><p title="卡罗拉" class="jsx-4123353477 name line-1">卡罗拉</p><p class="jsx-4123353477 price">9.98-14.98万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/3196"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-88086380 jsx-2292158439 img"></span></div><p title="长安CS75 PLUS" class="jsx-4123353477 name line-1">长安CS75 PLUS</p><p class="jsx-4123353477 price">10.49-15.29万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/348"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-937993661 jsx-2292158439 img"></span></div><p title="君威" class="jsx-4123353477 name line-1">君威</p><p class="jsx-4123353477 price">14.68-20.78万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/409"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-3911732358 jsx-2292158439 img"></span></div><p title="宝来" class="jsx-4123353477 name line-1">宝来</p><p class="jsx-4123353477 price">7.08-12.70万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/1623"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-417058089 jsx-2292158439 img"></span></div><p title="领克03" class="jsx-4123353477 name line-1">领克03</p><p class="jsx-4123353477 price">11.38-24.88万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/4802"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-1906738822 jsx-2292158439 img"></span></div><p title="秦PLUS DM-i" class="jsx-4123353477 name line-1">秦PLUS DM-i</p><p class="jsx-4123353477 price">11.25-15.25万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/279"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-126931585 jsx-2292158439 img"></span></div><p title="本田XR-V" class="jsx-4123353477 name line-1">本田XR-V</p><p class="jsx-4123353477 price">11.49-16.29万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/534"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-2431824818 jsx-2292158439 img"></span></div><p title="雷凌" class="jsx-4123353477 name line-1">雷凌</p><p class="jsx-4123353477 price">10.18-14.08万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/1355"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-2818560064 jsx-2292158439 img"></span></div><p title="迈锐宝XL" class="jsx-4123353477 name line-1">迈锐宝XL</p><p class="jsx-4123353477 price">13.39-18.39万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/4865"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-2252445246 jsx-2292158439 img"></span></div><p title="宋PLUS DM-i" class="jsx-4123353477 name line-1">宋PLUS DM-i</p><p class="jsx-4123353477 price">14.68-16.98万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/1310"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-2452543080 jsx-2292158439 img"></span></div><p title="伊兰特" class="jsx-4123353477 name line-1">伊兰特</p><p class="jsx-4123353477 price">9.58-13.78万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/1014"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-3166091967 jsx-2292158439 img"></span></div><p title="马自达3 昂克赛拉" class="jsx-4123353477 name line-1">马自达3 昂克赛拉</p><p class="jsx-4123353477 price">10.99-18.39万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/4353"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-2694201659 jsx-2292158439 img"></span></div><p title="长安UNI-T" class="jsx-4123353477 name line-1">长安UNI-T</p><p class="jsx-4123353477 price">11.59-13.89万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/2836"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-1876380055 jsx-2292158439 img"></span></div><p title="途岳" class="jsx-4123353477 name line-1">途岳</p><p class="jsx-4123353477 price">13.98-19.78万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/4532"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-2785975328 jsx-2292158439 img"></span></div><p title="长安欧尚X5" class="jsx-4123353477 name line-1">长安欧尚X5</p><p class="jsx-4123353477 price">6.99-10.29万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/32"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-2551921745 jsx-2292158439 img"></span></div><p title="名爵6" class="jsx-4123353477 name line-1">名爵6</p><p class="jsx-4123353477 price">8.58-13.48万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/2835"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-1212647141 jsx-2292158439 img"></span></div><p title="探岳" class="jsx-4123353477 name line-1">探岳</p><p class="jsx-4123353477 price">14.99-22.79万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/4563"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-3033831298 jsx-2292158439 img"></span></div><p title="哈弗大狗" class="jsx-4123353477 name line-1">哈弗大狗</p><p class="jsx-4123353477 price">11.79-16.09万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/1701"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-1627782346 jsx-2292158439 img"></span></div><p title="红旗H5" class="jsx-4123353477 name line-1">红旗H5</p><p class="jsx-4123353477 price">14.58-19.08万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/741"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-1272320096 jsx-2292158439 img"></span></div><p title="博越" class="jsx-4123353477 name line-1">博越</p><p class="jsx-4123353477 price">7.58-14.28万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/410"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-1601774218 jsx-2292158439 img"></span></div><p title="高尔夫" class="jsx-4123353477 name line-1">高尔夫</p><p class="jsx-4123353477 price">12.98-16.58万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/31"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-816055773 jsx-2292158439 img"></span></div><p title="名爵5" class="jsx-4123353477 name line-1">名爵5</p><p class="jsx-4123353477 price">6.49-10.19万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/4342"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-3395195365 jsx-2292158439 img"></span></div><p title="领克06" class="jsx-4123353477 name line-1">领克06</p><p class="jsx-4123353477 price">11.86-13.86万</p></a><a target="_blank" class="jsx-4123353477" href="/auto/series/352"><div class="jsx-4123353477 image-wrapper"><span class="jsx-4288683969 jsx-2491407554 jsx-2292158439 img"></span></div><p title="昂科威" class="jsx-4123353477 name line-1">昂科威</p><p class="jsx-4123353477 price">14.99-19.99万</p></a><div style="height: 1px;"></div><
'''

reg = '<a target="_blank" class="jsx-4123353477" href="(.*?)"><div class="jsx-4123353477.*?title="(.*?)" class="jsx-4123353477.*?price">(.*?万)'
pattern = re.compile(reg, re.S)
r_list = pattern.findall(html)
#print(r_list)

for t in r_list:
    print(t[0], t[1], t[2].strip())