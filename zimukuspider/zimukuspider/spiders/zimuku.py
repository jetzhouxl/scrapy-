# -*- coding: utf-8 -*-
import json
import re

import scrapy
from bs4 import BeautifulSoup
from scrapy import Request
from scrapy.http.headers import Headers

from zimukuspider.items import ZimukuspiderItem


class ZimukuSpider(scrapy.Spider):
    name = 'zimuku'
    allowed_domains = ['www.zimuku.cn']
    start_urls = ['https://www.zimuku.cn/dld/113270.html']
    base_urls = 'https://www.zimuku.cn'

    def start_requests(self):
        yield Request('https://www.zimuku.cn/detail/113270.html', callback=self.parse_detail)

    def parse_detail(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        dld = soup.find(id='down1')['href']
        url = self.base_urls+dld
        yield Request(url=url, callback=self.parse_downloadfile)

        # print(soup.li.a['href'])

    def parse_downloadfile(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        url = self.base_urls+soup.li.a['href']
        yield Request(url=url, callback=self.downloadfile)

    def downloadfile(self, response):
        # 使用正则表达式解析出文件名
        result = re.match(
            '.*="(.+)"', response.headers.to_unicode_dict()['content-disposition'])
        item = ZimukuspiderItem()
        item['filename'] = result.group(1)
        item['file_url'] = response.url
        yield item
