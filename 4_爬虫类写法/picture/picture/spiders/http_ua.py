import scrapy


class HttpUaSpider(scrapy.Spider):
    name = 'http_ua'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']



    def parse(self, response):
        print(response.text) # 查看设置的UA是否生效
        pass
