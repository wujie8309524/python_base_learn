1.Opener<br>
---

当你获取一个URL你使用一个opener(一个urllib2.OpenerDirector的实例)。在前面，我们都是使用的默认的opener，也就是urlopen。它是一个特殊的opener，可以理解成opener的一个特殊实例，传入的参数仅仅是url，data，timeout。

如果我们需要用到Cookie，只用这个opener是不能达到目的的，所以我们需要创建更一般的opener来实现对Cookie的设置。<br>

2.Cookielib
---
cookielib模块的主要作用是提供可存储cookie的对象，以便于与urllib2模块配合使用来访问Internet资源。Cookielib模块非常强大，我们可以利用本模块的CookieJar类的对象来捕获cookie并在后续连接请求时重新发送，比如可以实现模拟登录功能。该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。<br>

它们的关系：CookieJar —-派生—->FileCookieJar  —-派生—–>MozillaCookieJar和LWPCookieJar


urllib.request.urlopen(opener)<br>
1. 默认的opener 只能传入 url,data,timeout<br>
2. 通过url.request.Request() 构建的request 可以添加 header<br>
3. 通过cookiejar 可以实现获取cookie<br>


3.python3.6
---
```python
#!/usr/bin/env python3.6
import urllib.request
from urllib.request import HTTPCookieProcessor
from http.cookiejar import CookieJar

'''
普通方式查看cookie
'''
URL_ROOT = r'http://www.baidu.com'

# 1.声明一个cookiejar对象的实例用来保存 cookie
cookie = CookieJar() #普通方式直接查看


# 2.利用 HTTPCookieProcessor 创建cookie 的处理器 handler
handler = HTTPCookieProcessor(cookie)

# 3.通过handler 构建 opener
opener = urllib.request.build_opener(handler)

# 4.使用 opener 请求资源 url_root 可以是一个url 也可以是一个request
response = opener.open(URL_ROOT)

request = urllib.request.Request(URL_ROOT)
response = opener.open(request)

#普通方式直接查看cookie
for item in cookie:
    print('Name = ' + item.name)
    print('Value =' + item.value)






```