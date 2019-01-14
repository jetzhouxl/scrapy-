# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline


class ZimukuFilePipeline(FilesPipeline):
    filename=''
    def get_media_requests(self, item, info):
        print(item['file_url'])
        self.filename=item['filename']
        yield Request(item['file_url'])

    def item_completed(self, results, item, info):
        return item

    def file_path(self, request, response=None, info=None):
        return self.filename


    
