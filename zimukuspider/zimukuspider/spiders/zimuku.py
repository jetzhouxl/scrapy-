# -*- coding: utf-8 -*-
import json
import re
from urllib.parse import urlencode

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
        data={}
        for page in range(1,self.settings.get('MAX_PAGE')+1):
            data['p']=page
            params=urlencode(data)
            url='https://www.zimuku.cn/newsubs?'+params
            yield Request(url, callback=self.parse)
    
    def parse(self,response):
        soup=BeautifulSoup(response.text,'html.parser')
        print(soup.find("table").find_all('a')[0])
        for a in soup.find("table").find_all('a'):
            url=self.base_urls+a['href']
            yield Request(url=url,callback=self.parse_detail)


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
