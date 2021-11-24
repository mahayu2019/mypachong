#!/usr/bin/env python
# coding=utf-8

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

import requests

pro='103.103.3.6:8080'

def probyurllib():
    proxy = pro
    proxy_handler = ProxyHandler({
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    })

    opener = build_opener(proxy_handler)
    try:
        response = opener.open('http://httpbin.org/get')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)


def probyrequests():
    proxy = '211.24.95.49:20008'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }
    try:
        response = requests.get('https://httpbin.org/get', proxies=proxies)
        print(response.text)
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)


if __name__ == '__main__':
    probyurllib()
    print('res')
    probyrequests()
