#!/usr/bin/env python
# coding=utf-8

'''
5.3.1 find_element_by_name 方法,检索元素对应的name
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chromedriver_path = r"d:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)

driver.maximize_window()
driver.get('https://cn.bing.com/')

# 检测搜索框的name并填入搜索关键字
# driver.find_element_by_name('q').send_keys('异步社区')

# 把name内置到参数中,效果相同
# driver.find_element(By.NAME, 'q').send_keys('异步社区')

# find_elements的复数形式,注意加上list下标
driver.find_elements(By.NAME, 'q')[0].send_keys('异步社区')

# 检测搜索按钮name并单击搜索按钮
# driver.find_element_by_name('go').click()

# driver.find_element(By.NAME, 'go').click()

driver.find_elements(By.NAME, 'go')[0].click()

sleep(5)  # 暂停5秒
driver.close()
