#!/usr/bin/env python3.6
import requests

# http://docs.python-requests.org/en/master/

# ##################### 请求部分 ######################

# 普通get请求
URL = 'http://localhost/python_cookie/index.php'
# URL = 'http://www.baidu.com'
r = requests.get(URL)

# 带参数的get请求
# payload = {'k1':'v1','k2':'v2'}
# r = requests.get(url,params = payload)

# 带headers
# headers = {'content-type':'application/json'}
# r = requests.get(url,params= payload,headers= headers)

# post请求
# r = request.post(url,data=payload)
# 传json
# r = request.post(url,data=json.dumps(payload))

# 上传文件
# files = {'file':open('test.txt','rb')}
# r = requests.post(url,files=files)

# 流式上传 发送大的文件，而不需要先读入内存
#  with open('test.txt') as f:
#       requests.post(url,data=f)

# ##################### 解析部分 ######################

print(type(r))

print(r.status_code)

print(r.encoding)

# 解析普通字符
print(r.text)

# 解析json格式数据
# print(r.json())

# 接收原始数据流 r.raw,需要设置请求stream=True
# r.raw.read(10)  读取原始数据流的10个字节

# ##################### cookie部分 ######################

# 发送cookie
# cookies = dict(cookies_key='value')
# r = requests.get(url,cookies = cookies)

# 得到 服务器发送的 cookie
print(r.cookies)

print(r.cookies['abc'])


# ##################### session部分 ######################
# 每次请求使用的不是一个会话

s = requests.Session()
print("====带session=========")
print(s.get(URL).text)
print(s.get(URL).text)

# ##################### 代理部分 ######################
# proxies = {
# 'https': url 代理的url地址
# }
# r = requests.post(url, proxies = proxies)