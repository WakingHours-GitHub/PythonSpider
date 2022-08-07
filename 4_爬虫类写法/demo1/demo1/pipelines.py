# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json

class Demo1Pipeline: # 数据管道
    def open_spider(self, spider):
        self.file_pipeline = open("movie.txt", 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # with open("movie.txt", 'a', encoding='utf-8') as f:
        #     # 将字典转换成字符串 json.dumps
        #     f.write(json.dumps(item, ensure_ascii=False) + '\n ')

        # 如果使用item对象, 则需要转换成dict()然后再使用dumps。
        self.file_pipeline.write(json.dumps(dict(item), ensure_ascii=False) + '\n ')

        # 如果直接使用dict类型, 在无需数据转换
        # self.file_pipeline.write(json.dumps(item, ensure_ascii=False) + '\n ')

        print(item) # 接收spider生成器, yield.
        return item

    def close_spider(self, spider):
        self.file_pipeline.close()
# 但是这样我们的文件流读写会不停的开关开关, 这样会造成资源的浪费
# 因此我们可以实现这两个方法:
# open_spider(self, spider) # 表示spider被开启时就调用这个方法
# close_spider(self, spider) # 表示spider被关闭的时候这个方法被调用.






