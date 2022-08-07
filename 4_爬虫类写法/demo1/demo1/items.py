# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# module差不错, 就是封装字段.
# 直接使用scrapy.Field()
# class Demo1Item(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class MovieItem(scrapy.Item):
    name = scrapy.Field()
    score = scrapy.Field()