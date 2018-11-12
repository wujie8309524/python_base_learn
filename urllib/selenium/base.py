from selenium import webdriver
from selenium.webdriver.common.keys import Keys
'''
    模拟chrome 打开python首页，点击搜索，获取html页面
'''
browser = webdriver.Chrome()
browser.get('https://www.python.org/')
assert "Python" in browser.title
elem = browser.find_element_by_name('q')
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
print(browser.page_source)
