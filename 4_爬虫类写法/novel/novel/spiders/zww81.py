import scrapy


class Zww81Spider(scrapy.Spider):
    name = 'zww81'
    allowed_domains = ['81zw.com']
    start_urls = ['http://81zw.com/']

    def parse(self, response):
        pass
