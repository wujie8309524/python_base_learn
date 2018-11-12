#!/usr/bin/env python3.6
import urllib.request
from urllib.request import HTTPCookieProcessor
from http.cookiejar import CookieJar

'''
普通方式查看cookie
'''
URL_ROOT = r'http://www.baidu.com'

# 声明一个cookiejar对象的实例用来保存 cookie
cookie = CookieJar() #普通方式直接查看


# 利用 HTTPCookieProcessor 创建cookie 的处理器 handler
handler = HTTPCookieProcessor(cookie)

# 通过handler 构建 opener
opener = urllib.request.build_opener(handler)

# 使用 opener
response = opener.open(URL_ROOT)

#普通方式直接查看cookie
for item in cookie:
    print('Name = ' + item.name)
    print('Value =' + item.value)




