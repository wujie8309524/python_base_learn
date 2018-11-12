#!/usr/bin/env python3.6
import urllib.parse
import urllib.request

url = "http://localhost/login.php"

values = {'act':'login','login[email]':'abc@abc.com','login[password]':'123456'}

data = urllib.parse.urlencode(values).encode(encoding='UTF-8') #封装post数据

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': len(data),
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://10.1.2.151/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
}

request = urllib.request.Request(url,headers=headers,data=data) # POST 方法

response = urllib.request.urlopen(request)

html = response.read()

print(html)



values = {}
values['username'] = "8309524@qq.com"
values['password'] = 'abc123'
data = urllib.parse.urlencode(values).encode(encoding='UTF-8')

url = url.encode('UTF-8') + "?".encode('UTF-8') + data

url = url.decode("UTF-8")

request = urllib.request.Request(url) #构建get请求

response = urllib.request.urlopen(request)

html = response.read()

print(html)