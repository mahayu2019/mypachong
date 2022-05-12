#!/usr/bin/env python
# coding=utf-8

'''
selenium 专用工具类
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


# 用于install()获取管理器使用的位置并将其传递给服务类
service = ChromeService(executable_path=ChromeDriverManager().install())
# 初始化驱动时使用Service实例：
browser = webdriver.Chrome(service=service)
browser.get('https://www.baidu.com')

browser.find_element(By.ID,"kw").send_keys('123')
browser.find_element(By.ID,"su").click()

time.sleep(5)
browser.close()