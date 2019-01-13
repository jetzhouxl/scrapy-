# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes=response.css('.quote');
        for quote in quotes:
            item=QuoteItem()
            item['text']=quote.css('.text::text').extract_first()
            item['author']=quote.css('.author::text').extract_first()
            item['tags']=quote.css('.tag .tag::text').extract()
            yield item
        #通过回调请求下一页面内容
        next=response.css('.pager .next a::attr(href)').extract_first()
        url=response.urljoin(next)
        yield scrapy.Request(url,callback=slef.parse)
    
