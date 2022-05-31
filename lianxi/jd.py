#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

BASE_URL = 'http://jindouyxt.com/Default/Login'
browser = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
browser.get(BASE_URL)
element = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.ID, "username")))
element.send_keys('xxx')
element2 = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.ID, "pass")))
element2.send_keys('xxx')
element3 = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "submit")))
element3.click()
