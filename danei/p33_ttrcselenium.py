#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver

options = webdriver.ChromeOptions()  # 设置参数
options.add_argument('--headless')  # 设置为无界面模式

chromedriver_path = r"d:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

#page = driver.get('http://www.ttrcw.com.cn/job?jobarea1=33102301')
page = driver.get('http://www.ttrcw.com.cn/job')


# 获取一页的数据
def get_one_page():
    # 基准xpath:匹配每个职位信息的节点对象列表
    dd_list = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[5]/div[1]/div[2]/div')
    for dd in dd_list:
        # print(dd.text.split('\n'))  # 去除换行符,变为list
        zdmod = {}  # 存储为字典
        zdmod['所属单位'] = dd.text.split('\n')[2]
        zdmod['职位'] = dd.text.split('\n')[0]
        zdmod['佣金'] = dd.text.split('\n')[1]
        print(zdmod)
    # driver.close()


while True:
    get_one_page()
    try:
        # 判断是否为最后一页,next在每个链接页面都存在,最终页面不存在,判断为-1
        # pg = driver.page_source.find('next')
        # print(pg)
        # 点击下一页,分类不同,链接不同,选择使用
        # driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[5]/div[1]/div[3]/div/ul/li[7]/a').click()
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[5]/div[1]/div[3]/div/ul/li[13]/a').click()
    except Exception as e:
        driver.quit()
        break
