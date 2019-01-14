# -*- coding: utf-8 -*-
import scrapy


class ZimukuSpider(scrapy.Spider):
    name = 'zimuku'
    allowed_domains = ['www.zimuku.cn']
    start_urls = ['http://www.zimuku.cn/']

    def parse(self, response):
        pass
