#!/usr/bin/env python3.6
import urllib.request
import urllib.parse
import http.cookiejar

filename = "mycookie.txt"
URL_LOGIN = "http://b.com/python_cookie/login.php"
URL_INDEX = "http://b.com/python_cookie/index.php"

# 创建文件类型cookie对象
cookie = http.cookiejar.MozillaCookieJar(filename)
# 创建handler 处理cookie
handler = urllib.request.HTTPCookieProcessor(cookie)
# 创建opener
opener = urllib.request.build_opener(handler)

data = {"user":"wj","password":"123"}
post_data = urllib.parse.urlencode(data).encode("UTF-8")

# 发送登录信息 种cookie
response = opener.open(URL_LOGIN,post_data)
print(response.read().decode('UTF-8'))
# 保存cookie信息
cookie.save(ignore_expires=True,ignore_discard=True)

# 发送带cookie的请求登录其他页面，获取登录之后的信息
response = opener.open(URL_INDEX)
print(response.read().decode('UTF-8'))

