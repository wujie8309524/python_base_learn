#!/usr/bin/env python3.6
import urllib.request
from urllib.request import HTTPCookieProcessor
#文件保存cookie
from http.cookiejar import MozillaCookieJar

'''
   保存cookie到文件
'''
#URL_ROOT = r'http://d.weibo.com/'
URL_ROOT = r'http://www.baidu.com'

filename = "cookie.txt"


# 声明一个cookiejar对象的实例用来保存 cookie
# cookie = CookieJar() #普通方式直接查看
cookie = MozillaCookieJar(filename) #文件保存cookie方式

# 利用 HTTPCookieProcessor 创建cookie 的处理器 handler
handler = HTTPCookieProcessor(cookie)

# 通过handler 构建 opener
opener = urllib.request.build_opener(handler)

# 使用 opener
response = opener.open(URL_ROOT)

# 保存到文件
# ignore_discard 忽视丢弃
# ignore_expires 覆盖写入
cookie.save(ignore_discard=True,ignore_expires=True)

# 带cookie请求response
print(response.read())



