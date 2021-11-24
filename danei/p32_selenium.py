#!/usr/bin/env python
# coding=utf-8

'''
闪退问题查阅博客
https://blog.csdn.net/weixin_42603129/article/details/105561926
'''

from selenium import webdriver
import time

chromedriver_path = r"d:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)

page = driver.get('https://www.baidu.com/')

# F12后选择搜索框,选中后右键copy--copy xpath提取元素
# find_element_by xpath用copyxpath,id用copyid
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('joker')  # 搜索框输入关键字
driver.find_element_by_xpath('//*[@id="su"]').click()  # 单击搜索按钮
driver.maximize_window()  # 窗口最大化
html = driver.page_source.encode('utf-8')  # 获取html源码,指定编码防止出错
print(html)
time.sleep(3)

driver.save_screenshot('p.jpg')  # 截图
# driver.close()  # 关闭窗口
