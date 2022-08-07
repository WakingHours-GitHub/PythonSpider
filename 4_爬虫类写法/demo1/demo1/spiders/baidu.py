import scrapy

# spider我们需要做两件事, 指定url, 然后解析数据

# 继承Spider
class BaiduSpider(scrapy.Spider):

    name = 'baidu' # 启动时, 指定运行哪个爬虫时用的. 在genspider命令创建.
    # name就是当使用scrapy run name时, 指定的名字, 与文件名无关, 与name字段有关.

    allowed_domains = ['baidu.com'] # 允许爬取的域名. # 不是必要的
    start_urls = ['http://www.baidu.com/']  # 从哪开始的url.

    # 获取从downloader下载的resp, 然后进行解析.
    def parse(self, response):
        # pass
        print(response.text) # 这里直接打印resp.text()页面信息
