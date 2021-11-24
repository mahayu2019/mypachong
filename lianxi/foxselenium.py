#!/usr/bin/env python
# coding=utf-8

'''
Firefox的selenium
'''
from selenium import webdriver

chromedriver_path = r"d:\geckodriver"
driver = webdriver.Firefox(executable_path=chromedriver_path)

driver.get('https://www.baidu.com/')
