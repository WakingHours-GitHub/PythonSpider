"""
启动爬虫有两种方式, 一种是通过命令行
    scrapy crawl name (名称) -> 启动爬虫
另一种是使用ide启动:
    如下


scrapy也有对应的api说明; 



"""


from scrapy.cmdline import execute
execute('scrapy crawl baidu'.split())
execute(['scrapy', 'crawl', 'baidu']) # 同理.
