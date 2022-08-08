import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Zww2Spider(CrawlSpider):
    name = 'zww2'
    allowed_domains = ['81zw.us']
    start_urls = ['https://www.81zw.com/book/57942/']

    rules = ( # 是一个规则。用于提取链接。
        # LinkExtractor: 链接提取器对象
        # callback: 使用回调函数进行解析。
        # follow: 是否继续跟进，提出url后，访问，是否还需要在新的url中提取url。
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),

        Rule(LinkExtractor(restrict_xpaths=r'//dd[1]/a'), callback='parse_item', follow=True),


        # 只需要定位到这里的标签, 会自动抽取其中的值.
        # 这里只需要定位到a, 然后他会自动提取其中的标签, 并且自动拼接
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="bottem1"]/a[4]'), callback='parse_item', follow=True)
        # 但是这里我们无法解析到第一章. 因此我们需要在上面添加解析第一章的规则.
    )

    def parse_item(self, response):

        title = response.xpath('//h1/text()').extract_first() # 抽取内容
        content = response.xpath('string(//div[@id="content"])').extract_first()
        print(title)
        yield {'title': title, content: content}


        # item = {}


        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item # 返回字典.
