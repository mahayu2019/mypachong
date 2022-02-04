#!/usr/bin/env python
# coding=utf-8

'''
参考文章:https://mp.weixin.qq.com/s/EaL3H2gwSeA-rZzbYNSm1Q
'''

from selenium import webdriver
import time
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#第一步获得文件名
url = 'https://music.163.com/#/discover/toplist?id=5453912201'

chromedriver_path = r"d:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get(url)
_iframe = driver.find_element_by_id('g_iframe')
driver.switch_to.frame(_iframe)

time.sleep(3)

page_text = driver.execute_script('return document.documentElement.outerHTML')

print(page_text)

#第二步拼接下载地址
base_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'