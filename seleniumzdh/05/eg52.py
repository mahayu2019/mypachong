#!/usr/bin/env python
# coding=utf-8

'''
5.2.1 find_element_by_id 方法,检索元素对应的id
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chromedriver_path = r"d:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)

driver.maximize_window()
driver.get('https://cn.bing.com/')

# 检测搜索框的id并填入搜索关键字
# 把id内置到参数中,效果相同
driver.find_element(By.ID, 'sb_form_q').send_keys('异步社区')

# 检测搜索按钮id并单击搜索按钮
driver.find_element(By.ID, 'sb_form_go').click()

sleep(5)  # 暂停5秒
driver.close()
