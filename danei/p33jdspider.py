#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
from time import sleep


class Jdspider:
    def __init__(self):
        chromedriver_path = r"d:\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromedriver_path)
        self.driver.get(url='https://www.jd.com/')
        self.driver.find_element_by_class_name('text').send_keys('爬虫书')
        self.driver.find_element_by_class_name('button').click()
        sleep(3)  # 等待页面加载完成

    def parse_html(self):
        '''提取数据'''
        # 把滚动条拉到最底部,等待数据加载完成
        self.driver.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        sleep(3)
        li_list = self.driver.find_elements_by_class_name('gl-item')
        for li in li_list:
            item = {}
            item['price'] = li.find_element_by_class_name('p-price').text.strip()
            item['name'] = li.find_element_by_class_name('p-name').text.strip()
            item['commit'] = li.find_element_by_class_name('p-commit').text.strip()
            item['shop'] = li.find_element_by_class_name('p-shopnum').text.strip()
            print(item)


    def run(self):
        self.parse_html()


if __name__ == '__main__':
    spider = Jdspider()
    spider.run()
