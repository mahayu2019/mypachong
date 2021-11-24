#!/usr/bin/env python
# coding=utf-8

'''
ZOL数据获取
主板报价信息完成首页获取
'''

import requests
import parsel
import pymysql

host = 'localhost'
port = 3306
db = 'zolbj'
user = 'root'
password = 'asdzxc123'


def get_connection():
    conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
    return conn


# 主板报价
def get_bj():
    url = 'https://detail.zol.com.cn/motherboard/pic.html'

    response = requests.get(url)

    sel = parsel.Selector(response.content.decode('gbk'))
    lists = sel.css('.list-box .list-item.clearfix')

    return lists


def do_dbs(lists):
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    for item in lists:
        sql = '''
            insert into zbbj(mc,xp,cpu,cpu_type,memo_type,jcxp,xk,zblx,jg) 
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            '''
        mc = item.css('h3 a::text,.param.clearfix li::attr(title)').extract_first()
        xp = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[1]
        cpu = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[2]
        cpu_type = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[3]
        memo_type = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[4]
        jcxp = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[5]
        xk = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[6]
        zblx = item.css('h3 a::text,.param.clearfix li::attr(title)').extract()[7]
        jg = item.css('.price-type::text').extract()[0]

        cursor.execute(sql, (mc, xp, cpu, cpu_type, memo_type, jcxp, xk, zblx, jg))
        conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    lists = get_bj()
    do_dbs(lists)
