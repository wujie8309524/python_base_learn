scrapy
==
```python
"""
在pycharm中启动scrapy
https://www.cnblogs.com/cuzz/p/7623663.html
在spider目录下创建start.py
1 # -*- coding:utf-8 -*-
2 
3 from scrapy import cmdline 
4 
5 cmdline.execute("scrapy crawl itcast -o itcast1.csv".split())
右上角 add configuration
script 新增start.py路径

1.创建scrapy项目
    scrapy startproject projectName

2.生成框架基础文件
    scrapy genspider meiju meijutt.com
    此处会在spider/xx.py中自动生成
    start_urls = [url]
    url 格式不正确会导致301
3.设置数据存储模板，保存需要提取的字段
    items.py
    import scrapy
    class MovieItem(scrapy.Item):
        name = scrapy.Filed()
        
4.编写spider/xx.py 提取item中规定的字段


5.修改pipelines.py 编写数据处理脚本

6.执行爬虫
    scrapy crawl xiaohua --nolog



"""





```