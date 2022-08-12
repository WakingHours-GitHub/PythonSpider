import scrapy


class Log1Spider(scrapy.Spider):
    name = 'log1'
    allowed_domains = ['login2.scrape','https://login2.scrape.center/login', 'https://login2.scrape.center/']
    # start_urls = ['http://login2.scrape.center/']

    def start_requests(self):
        url = 'https://login2.scrape.center/login'
        form_data = {
            'username': 'admin',
            'password': 'admin'
        }
        # 使用FormRequest， 用于处理表单数据。
        # 发送请求
        yield scrapy.FormRequest(url, method='POST', formdata=form_data, callback=self.parse)

    def parse(self, response):
        # 此时response是登录完的请求
        # print(response.status)
        # print(response.text)
        print("=="*50)

        # 请求真正的url;
        main_url = "https://login2.scrape.center/"

        yield scrapy.Request(main_url, dont_filter=True, callback=self.parse_main) # 将主页面的request请求, 交给蜘蛛, 请求. 然后将response返回到response当中.
        # 而meta参数是用来传递参数的.

    # 不用考虑绘画问题, 会自动保持绘画.
    def parse_main(self, response):
        # print(response.status)
        print(response.text)