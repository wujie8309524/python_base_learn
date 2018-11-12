#!/usr/bin/env python3.6
import urllib.request

response = urllib.request.urlopen("https://baidu.com/")

#html = response.read()

#print(html)

'''使用request对象'''
request = urllib.request.Request('https://baidu.com/')

response = urllib.request.urlopen(request)

html = response.read()

print(html)

