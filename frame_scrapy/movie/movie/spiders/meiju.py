# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']

    # 此处不写 www 会导致 301跳转
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for movie in movies:
            item = MovieItem()
            # scrapy 自带的解析器
            item['name'] = movie.xpath('./h5/a/@title').extract()[0]
            yield item