# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request
import os
'''
    数据处理
'''
class XhAllPipeline(object):
    def process_item(self, item, spider):
        print(item)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        request = urllib.request.Request(url=item['addr'],headers=headers)
        response = urllib.request.urlopen(request)
        # os.path.join 返回合并之后的路径
        # str.join(str|list|tuple|dict) 返回用str 替换分隔符连接 str list tuple dict 之后的字符
        file_name = os.path.join(r'/Users/wujie/PycharmProjects/frame/xh_all/data',item['name']+'.jpg')
        with open(file_name,"wb") as f:
            f.write(response.read())