#!/usr/bin/env python
# coding=utf-8


'''
改良的selenium下载器
'''
import os
import re
import wget
import zipfile
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome文件所在路径
path = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application'


# 抽取软件版本号
def getVersion(path):
    file_list = os.listdir(path)  # 读取指定目录下的所有文件名称
    for num in file_list:
        x = re.findall(r'^\d.*', num)  # 正则匹配出版本号
        if x is not None:  # 筛选版本号
            break
    return x[0]


# 拼接下载地址
url = 'https://cdn.npmmirror.com/binaries/chromedriver/' + getVersion(path) + '/chromedriver_win32.zip'

# 指定存放路径
p = r'D:\chromedriver_win32.zip'

# 下载
wget.download(url, p)

#解压下载的文件
zFile = zipfile.ZipFile(p, "r")
for fileM in zFile.namelist():
    zFile.extract(fileM, "d:\\")
    zFile.close()

# 测试部分
browser = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')

browser.get('https://www.baidu.com')

browser.find_element(By.ID, "kw").send_keys('123')
browser.find_element(By.ID, "su").click()

time.sleep(5)
browser.close()
