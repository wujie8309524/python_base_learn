#!/usr/bin/env python3.6
import bs4
'''
节点类型：
    tag
        html标签  tag.name、tag.attrs
    navigableString
        文档内容   soup.p.string 类型为navigableString
        获取内容：
            string
                navigablesString 对象不包括其他tag，可直接获取
                如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点:
                如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同:
                如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None :  
                  
            get_text("|",strip=True)
                navigablesString 对象有子节点tag时，将各tag内容用 | 分割，并去除空格
                
            .contents 
                navigablesString 当没有子节点时报错, 对象有子节点tag时，返回一个tag list
    BeautifulSoup
        整个文档对象，特殊的tag，tag.name == document、tag.attrs
    Comment
        注释


'''
from bs4 import BeautifulSoup
'''
https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
'''
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse">111111<b>The Dormouse's story</b>2222222</p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>

"""

soup = BeautifulSoup(html,'lxml')

#使用本地文件
#soup = BeautifulSoup(open('index.html'))

# 输出格式化内容

print(soup.prettify())

# 直接点 元素名
print("=======title==========")
print(soup.title)
print("=======title.string========")
print(soup.title.string)
print("=======title.parent.name========")
print(soup.title.parent.name)
print("======= p ========")
print(soup.p)
print("======= p.string ========")
print(soup.p.string)
print("======= p.b ========")
print(soup.p.b)
print("======= p.b.string =======")
print(soup.p.b.string)
print("======= a ========")
print(soup.a)
print("======= find_all('a') ========")
print(soup.find_all('a'))
print("======= find(id='link3') ========")
print(soup.find(id='link3'))

print("==========================")
print("=========== all_link ===============")
all_link = soup.find_all('a')
print(all_link)
for link in all_link:
    print("========= type(link) ======")
    print(type(link))
    # 提取tag为link的属性值
    print("======== link.get('href') =======")
    print(link.get('href'))
    print(link['href'])
    # 提取tag为link的文本内容
    print("======== type(link.string) =======")
    print(type(link.string))
    # 判断是否为注释类型 屏蔽内容类型为注释的url
    #if(type(link.string) == bs4.element.Comment):

    print("========= link.string ========")
    print(link.string)

print("==========================")
print("==========================")
print(soup.get_text())