# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline

class TestscrapyPipeline(object):
    def process_item(self, item, spider):

        return item

    # def get_media_requests(self, item, info):
    #     return [Request(x) for x in item.get(self.images_urls_field, [])]
