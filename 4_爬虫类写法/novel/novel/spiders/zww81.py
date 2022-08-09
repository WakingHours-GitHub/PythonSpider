import scrapy


class Zww81Spider(scrapy.Spider):
    name = 'zww81'
    allowed_domains = ['81zw.com']

    # 从开始url进行开始。
    # start_urls = ['https://www.81zw.com/book/57181/373776.html'] # 第一章节
    start_urls =['https://www.81zw.com/book/57181/932697.html'] # 最后三章节, 测试是否能够正常结束

    def parse(self, response):
        title = response.xpath('//h1/text()').extract() # 抽取内容
        content = response.xpath('string(//div[@id="content"])').extract_first()

        yield {'title': title, content: content}

        # 接下来解析下一个url, 并且拼接url
        # base_url = "https://www.81zw.com" # 基准url
        # href_url = response.xpath('//div[@class="bottem1"]/a[4]/@href').extract_first() # 抽取下一章的url -> 这里是相对列表
        # print(href_url)
        # next_url = base_url + href_url
        # print(next_url)
        # # 判断是否为最后一章节:
        # # if response.url
        # if href_url.find('.html') == -1: #  使用find查看.html是否再下一个列表当中. 如果不在返回-1, 表示最后一章节.
        #     # 然后我们继续获取下一章节
        #     yield scrapy.Request(url=next_url, callback=self.parse)

        # 或者使用urljoin进行拼接
        next_url = response.xpath('//div[@class="bottem1"]/a[4]/@href').extract_first()
        if next_url.find('.html') == -1:
            # 使用urljoin进行拼接
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse) # 这样进行拼接
        #

        pass
