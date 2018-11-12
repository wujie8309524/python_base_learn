#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import re
import http.cookiejar

class MAIL:
    def __init__(self,username,password):
        # 设置代理，以防止本地IP被封
        self.proxyUrl = "http://202.106.16.36:3128"

        self.loginUrl = "https://mail.163.com/entry/cgi/ntesdoor?style=-1&df=mail163_letter&net=&language=-1&from=web&race=&iframe=1&product=mail163&funcid=loginone&passtype=1&allssl=true&url2=https://mail.163.com/errorpage/error163.htm"

        self.username = username
        self.password = password
        self.sid = ""

        self.cookie = http.cookiejar.MozillaCookieJar("mail.txt")
        self.handler = urllib.request.HTTPCookieProcessor(self.cookie)
        self.opener = urllib.request.build_opener(self.handler)
        # 将opener安装为全局 urlopen 自动调用此self.opener对象
        urllib.request.install_opener(self.opener)


    def login(self):

        headers = {
            'Referer': "https://mail.163.com/",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:62.0) Gecko/20100101 Firefox/62.0"
        }

        postData = {
            'savelogin': "0",
            'url2': "http://mail.163.com/errorpage/error163.htm",
            'username': self.username,
            'password': self.password
        }

        print("URL =======>")
        print(self.loginUrl)

        postData = urllib.parse.urlencode(postData).encode(encoding='UTF-8')
        print("POST =======>")
        print(postData)
        request = urllib.request.Request(self.loginUrl, postData, headers)

        response = urllib.request.urlopen(request)
        page = response.read().decode('UTF-8')
        print("response ======>")
        print(page)

        # 保存cookie信息
        self.cookie.save(ignore_expires=True, ignore_discard=True)

        pattern = re.compile(r'sid=(.*?)&',re.S)



        self.sid = re.search(pattern,page).group(1)

        print("sid =======>")
        print(self.sid)

    # 通过sid码获得邮箱收件箱信息
    def messageList(self):
        # 重定向至收件箱的网址
        listUrl = 'http://mail.163.com/js6/s?sid=%s&func=mbox:listMessages&TopTabReaderShow=1&TopTabLofterShow=1&welcome_welcomemodule_mailrecom_click=1&LeftNavfolder1Click=1&mbox_folder_enter=1' % self.sid
        # 新的请求头
        Headers = {
            'Accept': "text/javascript",
            'Accept-Language': "zh-CN,zh;q=0.9",
            'Connection': "keep-alive",
            'Host': "mail.163.com",
            'Referer': "https://mail.163.com/js6/main.jsp?sid=%suCFJZNnnRnInrsigqunnSrQXsvMMqctH&df=mail163_letter" % self.sid,
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:62.0) Gecko/20100101 Firefox/62.0"
        }
        # 发出请求并获得响应
        request = urllib.request.Request(listUrl, headers=Headers)
        # 带cookie请求
        response = self.opener.open(request)

        # 提取响应的页面内容，里面是收件箱的信息
        content = response.read().decode('utf-8')
        print('Content =====>')
        print(content)

        pattern = re.compile(
            'from..(.*?),.*?to..(.*?),.*?subject..(.*?),.*?sentDate..(.*?),\n.*?receivedDate..(.*?),\n', re.S)
        mails = re.findall(pattern, content)
        for mail in mails:
            print('-' * 50)
            print('发件人:', mail[0], '主题:', mail[2], '发送时间:', mail[3])
            print('收件人:', mail[1], u'接收时间:', mail[4])


mail = MAIL('18801004755@163.com','abc123')
mail.login()
mail.messageList()
