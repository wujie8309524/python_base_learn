# -*- coding: utf-8 -*-
import scrapy
import re
from xh_all.items import XhAllItem

class AllSpider(scrapy.Spider):
    name = 'all'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/hua/']
    pattren = re.compile(r'http')
    # 保留所有翻页链接
    url_set = set()

    def parse(self, response):
        # 首次爬取 页面为 hua 不会执行此段代码
        # 如果页面地址为 xxx 开头，则取此页面中的 所有图片
        if response.url.startswith("http://www.xiaohuar.com/list-"):
            print("====== 开始爬取 %s ======" % response.url)
            allPics = response.xpath('//div[@class="img"]/a')
            for pic in allPics:
                item = XhAllItem()
                name = pic.xpath('./img/@alt').extract()[0]
                addr = pic.xpath('./img/@src').extract()[0]
                pattern = r''
                if not re.match(AllSpider.pattren,addr):
                    addr = 'http://www.xiaohuar.com' + addr
                item['name'] = name
                item['addr'] = addr
                yield item

        # 处理多页（第一次爬取先执行）
        # 获取所有地址连接
        urls = response.xpath('//a/@href').extract()
        for url in urls:
            if url.startswith("http://www.xiaohuar.com/list-"):
                # 如果没有爬取过
                if url not in AllSpider.url_set:
                    # 添加到已爬取url中
                    AllSpider.url_set.add(url)
                    # 爬取此页面
                    yield self.make_requests_from_url(url)


