# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.http import Request
from scrapy.pipelines.images import FilesPipeline
import os
class CensusScraperPipeline(FilesPipeline):
    '''
    def process_item(self, item, spider):
        return item

    def file_path(self, request, response=None, info=None):
        original_path = super(CensusScraperPipeline, self).file_path(request, response=None, info=None)
        print(original_path)
        print("in PIPeline \n\n\n")
        return request.meta.get('filename','')
    '''

    def get_media_requests(self, item, info):
        return [Request(x, meta={'title': item["title"]})
                for x in item.get('file_urls', [])]
 
    def file_path(self, request, response=None, info=None):
        print("file_path")
        print(request.meta)
        return request.meta['title']    
