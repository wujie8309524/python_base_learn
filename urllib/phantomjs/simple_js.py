from selenium import webdriver
from bs4 import BeautifulSoup
'''
内置无界面浏览器，渲染页面
'''
driver = webdriver.PhantomJS()
driver.get("http://localhost/testjs.html")
data = driver.title
print(data)

myid = driver.find_element_by_id("myid").text

print(myid)

page = driver.page_source

soup = BeautifulSoup(page,'lxml')

print(soup.prettify())


driver.quit()



