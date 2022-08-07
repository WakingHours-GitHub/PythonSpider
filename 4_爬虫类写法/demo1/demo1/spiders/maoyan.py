import sys
import scrapy

# sys.path.append(r'D:\PyCharm\PythonCrawler(System)\4_爬虫类写法\demo1\demo1')
from demo1.items import MovieItem  # 将demo1设置为源代码, 即可使用职能提示了.


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://www.maoyan.com/films']

    # 这次我们使用pipelines, 使用yield实现推送, 使用生成器.
    def parse(self, response):
        names = response.xpath('//div[@class="channel-detail movie-item-title"]/a/text()').extract()
        score_div = [score.xpath('string(.)').extract_first() for score in
                     response.xpath('//div[@class="channel-detail channel-detail-orange"]')]
        print(score_div)
        print(names)
        # print(response.xpath("/html/body/div[@id='app']/div[@class='movies-channel']/div[@class='movies-panel']/div[@class='movies-list']/dl[@class='movie-list']/dd/div[@class='channel-detail channel-detail-orange']"))
        # 如果xpath中没有找到, extract_first()没有找到不到, 则返回None. extract()则会报错.

        # 使用pipelines 进行保存数据
        # for name, score in zip(names, score_div):
        # #   这里使用yield推送给pipelines只能只用Item对象或者子字典对象.
        # #   yield推送给pipelines中的Item对象, 我们需要提前配置一下这个
        #     yield {'name': name, 'score':score}

        # 使用yield推送Item对象, 前提是在settings文件中配置好.
        item = MovieItem()  # 创建item对象, 用于保存数据.
        for name, score in zip(names, score_div):  # zip打包 每次返回一个元组, 自动拆包
            # 也是使用key,
            item['name'] = name
            item['score'] = score
            yield item

        # 有什么区别. 其实本质上都是字典. item解析后也是字典类型. 只不过方式不同
