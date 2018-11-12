#!/usr/bin/env python3.6
import urllib.request
from urllib.request import HTTPCookieProcessor
from http.cookiejar import MozillaCookieJar

'''带cookie的请求'''

# 创建文件cookie实例
cookie = MozillaCookieJar()
# 加载cookie文件
cookie.load("mycookie.txt",ignore_discard=True,ignore_expires=True)

# 创建handler
handler = HTTPCookieProcessor(cookie)

# 创建opener
opener = urllib.request.build_opener(handler)

# 通过带cookie的opener 请求url
request = urllib.request.Request('http://b.com/python_cookie/index.php')

# opener 可以传入一个request请求
response = opener.open(request)

print(response.read().decode('UTF-8'))


