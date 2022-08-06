import scrapy


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian,com']
    # start_url, 就是我们开始要爬取的主页面
    start_urls = ['https://www.qidian.com/rank/hotsales/']

    # 解析部分
    def parse(self, response):
        # 直接response.提取 就可以了. 因为scrapy中继承了多种提取数据的方式.
        names = response.xpath("//h2/a/text()").extract() # extract抽取全部满足的数据, 返回一个列表
        authors = response.xpath('//p[@class="author"]/a[1]/text()').extract()
        # 可见, 默认提取出来的都是Selector对象. 我们还需要使用.extract()进行抽取
        # print(names) # <Selector xpath='//h2/a/text()' data='夜的命名术'>
        print(response.text)

        book = list()
        # return
        for name, author in zip(names, authors):
            # 写字典也可以. 写item的方式也可以.
            book.append({'name':name, 'author': author})
        return book
    # 然后在调用出, 使用-o book.json即可. 就可以导出为json格式文件.
    # 或者-o book.csv
    # -o book.xml
    # 都可以生成不同的数据格式.
