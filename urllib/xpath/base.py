#!/usr/bin/env python3.6
from lxml import etree
'''
结点类型：
    元素:
        /
        //
        /*
    属性：
        @href
        @*
    文本：
    （1）获取最外面的标签，遍历内部的所有子标签并获取标签文本；

    （2）用正则去掉所有标签；

    （3）/text()获取标签的文本，//text()获取标签以及子标签的文本；

    （4）使用xpath('string(.)')这种方式获取所有文本并且拼接。

一些例子：
        nodename 选取此节点的所有子节点
        /       从根节点选取
        //      不考虑位置，从当前节点中选择文档中的节点
        .       选取当前节点
        ..      选取当前节点的父节点
        @       选取属性
    属性表达式：
        bookstore/book[1]
        bookstore/book[last()]
        //title[@lang]
        /bookstore/book[price>35.00]
    表达式
        //title | //price      元素集合
    
'''

text = '''
<head>
    <title>这是一个<b>标题</b>啊!</title>
</head>
<body>
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">before text<span class="bold">third item</span>after text</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>

'''

html = etree.HTML(text)
# 输出html elementTree
print(type(html))

# 自动补全
res = etree.tostring(html, pretty_print=True)
print(type(res))

# 从文件中读取
# html = etree.parse('text.html')
# res = etree.tostring(html,pretty_print=True)

print(res)

print("\n\r")
# 获取title的值
print(html.xpath('//title/text()'))
print(html.xpath('//title//text()'))
print(html.xpath('//title')[0].xpath('string(.)'))

print("\n\r")
# 获取所有li
print(html.xpath('//li'))

# 获取第一个li的属性class
print(html.xpath('//li[1]/@class'))

for li in html.xpath('//li'):
    print(type(li))
    print(li)
    # 获取元素属性
    print(li.xpath('@class'))

print('\n\r')


# 所有li的class属性值
print(html.xpath('//li/@class'))
# li下href = link1.html的 <a>标签的文本内容 属性选择器
print(html.xpath('//li//a[@href="link1.html"]')[0].text)

# li下href = link3.html的 <a>标签的文本内容 属性选择器
print(html.xpath('//li//a[@href="link3.html"]')[0].text)
print(html.xpath('//li//a[@href="link3.html"]/text()'))
print(html.xpath('//li//a[@href="link3.html"]//text()'))
print(html.xpath('//li//a[@href="link3.html"]')[0].xpath('string(.)'))

print("\n\r")

# li的直接子元素span
print(html.xpath('//li/span'))

# li的所有后代span
print(html.xpath('//li//span'))

# 最后一个li下a的href属性
print(html.xpath('//li[last()]/a/@href'))

# 倒数第二个li下a的href属性
print(html.xpath('//li[last()-1]/a/@href'))

# 属性选择器 所有bookstore下book元素，并且元素属性price >35
# /bookstore/book[price>35.00]

print("\n\r")
# 所有class = bold的标签
print(html.xpath('//*[@class="bold"]'))
# 元素的 tag名、 属性值、text
print(html.xpath('//*[@class="bold"]/@class'))
print(html.xpath('//*[@class="bold"]')[0].tag)

print(html.xpath('//*[@class="bold"]')[0].text)



