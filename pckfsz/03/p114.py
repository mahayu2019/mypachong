#!/usr/bin/env python
# coding=utf-8

# 3.1.3解析连接
# 1.urlparse()
from urllib.parse import urlparse

result = urlparse('www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
