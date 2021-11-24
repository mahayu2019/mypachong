#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver


# 1、不设置driver为全局，放在函数内（会闪退）

# 登陆百度
def main():
    chromedriver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    # 打开页面
    page = driver.get('https://www.baidu.com/')


if __name__ == "__main__":
    main()

# 2、把driver放在函数外，为全局（不会闪退）

chromedriver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)


# 登陆百度
def main():
    # 打开页面
    page = driver.get('https://www.baidu.com/')


if __name__ == "__main__":
    main()


# 3、也可以把driver放在函数内，只要设置为全局变量就可以

# 登陆百度
def main():
    global driver
    chromedriver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    # 打开页面
    page = driver.get('https://www.baidu.com/')


if __name__ == "__main__":
    main()
