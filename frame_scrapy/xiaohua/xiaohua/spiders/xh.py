# -*- coding: utf-8 -*-
import scrapy
from xiaohua.items import XiaohuaItem

class XhSpider(scrapy.Spider):
    name = 'xh'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-1.html']

    def parse(self, response):
        allPics = response.xpath('//div[@class="img"]/a')
        for pic in allPics:
            item = XiaohuaItem()
            name = pic.xpath('./img/@alt').extract()[0]
            src = pic.xpath('./img/@src').extract()[0]
            addr = 'http://www.xiaohuar.com'+src
            item['name'] = name
            item['addr'] = addr
            yield item