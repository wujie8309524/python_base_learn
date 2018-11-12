#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-
import urllib.request
import re

"""抓取糗事百科"""

class QSBK():
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False

    def request(self,url):
        print('数据加载中...')
        try:
            request = urllib.request.Request(url,headers=self.headers)
            response = urllib.request.urlopen(request)
            page = response.read().decode("UTF-8")
            compile = r'<div.*?class="author.*?</a>.*?<a.*?<h2>(.*?)</h2>'
            pattern = re.compile(compile,re.S)
            res = re.findall(pattern,page)
            for item in res:
                self.stories.append(item)
        except urllib.request.URLError as e:
            if hasattr(e,"code"):
                print("请求出错：" + e.code)
                exit(1)
            if hasattr(e,"reason"):
                print("请求出错: " + e.reason)
                exit(1)



    def loadPage(self, pageIndex):
        if pageIndex == 1:
            url= 'https://www.qiushibaike.com/'
            self.request(url)
        else:
            s = input()
            if s == "Q":
                self.enable = False
                return
            else:
                url = 'https://www.qiushibaike.com/8hr/page/'+str(pageIndex)+'/'
                self.request(url)

    def out(self,page):
        print("第 %s 页:" % (self.pageIndex))
        for item in page:
            print(item,end="")

    def start(self):
        print('正在读取糗事百科，按回车查看新的内容，Q退出')

        self.enable = True
        #先读取一页
        self.loadPage(self.pageIndex)

        while self.enable:
            if len(self.stories) > 0:
                self.out(self.stories)
                self.stories = []
                self.pageIndex += 1
                self.loadPage(self.pageIndex)

spider = QSBK()
spider.start()