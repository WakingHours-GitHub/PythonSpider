import scrapy


class Log1Spider(scrapy.Spider):
    name = 'log1'
    allowed_domains = ['login2.scrape']
    # start_urls = ['http://login2.scrape.center/']

    def start_requests(self):
        url = 'http://login2.scrape.center/login'
        form_data = {
            'username': 'admin',
            'password': "admin"
        }
        # 使用FormRequest， 用于处理表单数据。
        # 发送请求
        yield scrapy.FormRequest(url, method='post', formdata=form_data, callback=self.parse)

    def parse(self, response):
        print(response.status_code)
        print(response.text)
