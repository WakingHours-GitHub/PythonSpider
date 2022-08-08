# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NovelPipeline:
    # 表示爬虫开启时, 执行的函数,
    def open_spider(self, spider):
        self.file = open("./dldl.txt", 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 需要看清楚推送过来的item是什么对象, 是dict还是Item对象
        title = item['title']
        content = item['content']

        self.file.write(title + '\n') # 只写入title, 方便查看

        self.file.flush() # 刷新缓冲区, 将缓冲区中的数据立刻写入文件, 同时清空缓冲区.


        print(item)
        return item

    # spider关闭后要执行的函数.
    def close_spider(self, spider):
        self.file.close()
