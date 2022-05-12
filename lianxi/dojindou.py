#!/usr/bin/env python
# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService




browser = webdriver.Chrome(executable_path=r'D:\WebDriver\bin\chromedriver.exe')
browser.get('http://jindouyxt.com/Default/Login')


ck=browser.get_cookies()
print(ck)


time.sleep(50)
browser.close()