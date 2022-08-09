import scrapy


class ZolSpider(scrapy.Spider):
    name = 'zol'
    allowed_domains = ['zol.com']
    start_urls = ['https://tv.zol.com.cn/slide/795/7953043_1.html#p=1'] # 请求的第一个一个链接.


    def parse(self, response):
        img_src = response.xpath('//table/tbody/tr/td/img[@class="main-Img"]/@src').extract()  # 返回一个列表, 底层用于遍历


        """
        源代码: 
        def get_media_requests(self, item, info):
            urls = ItemAdapter(item).get(self.images_urls_field, [])
            return [Request(u) for u in urls] 
        """
        title = response.xpath('//h1/a/text()').extract_first()
        print(img_src)

        yield {
            'img_src': img_src, # 这里必须是列表.
            # 'title': title
        }

