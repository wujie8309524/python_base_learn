#!/usr/bin/env python3.6
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
import time

'''
    抓取千里马投标
    https://www.cnblogs.com/zhaof/p/6953241.html
'''
class QLM():
    def __init__(self,url,user='',pwd=''):
        self.browser = webdriver.Chrome()
        self.url = url
        self.data_list = []
        self.pageNum = 1
        self.user = user
        self.pwd = pwd
    def login(self):
        pass


    def getIndexPage(self):
        self.browser.get(self.url)
        elem = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.ID, "fkeyword"))
        )
        elem = self.browser.find_element_by_id('fkeyword')

        elem.clear()
        # 移动到搜索框 点击清除默认文字
        actions = ActionChains(self.browser).move_to_element(elem).click(elem).perform()
        elem.send_keys('朗读亭')
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        # 弹出此页面高度
        # browser.execute_script('alert("page height:"+document.body.scrollHeight)')
        # 定位到弹出框 并点击确认
        # browser.switch_to.alert.accept()
        return self.browser.page_source

    def getNextPage(self,maxPage):
        if maxPage == 0:
            self.pageNum += 1
        elif maxPage > 1  and self.pageNum < maxPage:
            self.pageNum += 1
        else:
            # 获取超过maxPage 退出
            self.browser.quit()
            return None
        # 滑动到底部
        self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # 尝试点击下页获取页面
        try:
            # 找到下页按钮并点击
            elem = self.browser.find_element_by_link_text(str(self.pageNum))
            ActionChains(self.browser).move_to_element(elem).click(elem).perform()
            time.sleep(2)
            return self.browser.page_source
        except exceptions.NoSuchElementException as e:
            # 出错退出
            self.browser.quit()
            return None

    def handlerPage(self,html):
        soup = BeautifulSoup(html,'html.parser')
        table = soup.find(id='list')
        for index,tr in enumerate(table.find_all("tr")):
            if index != 0:
                tds = tr.find_all("td")
                title = tds[1].get_text()
                addr = tds[2].get_text()
                time = tds[3].get_text()
                data_dict = dict(title=title,addr=addr,time=time)
                self.data_list.append(data_dict)
    def res(self):
        return self.data_list

    def main(self,maxPage=0):
        html = self.getIndexPage()
        self.handlerPage(html)
        while True:
            nextPage = self.getNextPage(maxPage=maxPage)
            if nextPage is not None:
                self.handlerPage(nextPage)
            else:
                break
        return self.data_list

url ='http://search.qianlima.com/search.jsp'
qlm =QLM(url)
data = qlm.main(2)
print(data)

