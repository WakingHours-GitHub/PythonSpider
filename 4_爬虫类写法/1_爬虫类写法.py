"""
学的差不多了, 无论是请求, 还是数据提取, 我们都已经学的差不多了.
因此我们需要学一下类的写法, 将各个模块分隔开, 养成这样的思维, 方便后面框架的学习

    URL管理:
        去除重复的url, 然后识别已经爬取的url
    爬取数据的类
        获得response
    解析数据的类
        从response中提取数据
    数据处理的类
        处理, 保存.
    调度类
        处理上述四个类, 如何工作.



"""

import requests
from fake_useragent import UserAgent

# url管理
class URLManager():
    def __init__(self):
        self.new_url = list()
        self.old_url = list()

    # 获取一个url
    def get_new_url(self) -> str:
        url = self.new_url.pop()  # 弹出一个, 返回值, 并删除, 最后一个元素
        self.old_url.append(url)  # 并且添加到爬取过的列表当中
        return url  # 返回url

    # 增加一个url
    def add_new_url(self, url):
        if url not in self.new_url and url not in self.old_url and url:
            # 只有不在new_url, 以及old_url, 并且url本身不为空的情况下, 才添加
            self.new_url.append(url)

    # 增加多个url
    def add_new_urls(self, urls):
        for url in urls:
            self.add_new_url(url)

    # 判断是否还有可以爬取的url
    def has_new_url(self) -> bool:
        return self.get_new_url_size() > 0

    # 获取可以爬取的数量
    def get_new_url_size(self):
        return len(self.new_url)

    # 获取已经爬取的数量
    def get_old_url_size(self):
        return len(self.old_url)


# 爬取类:
class Downloader:

    def download(self, url):
        response = requests.get(
            url,
            headers={
                "User-Agent": UserAgent().random
            }
        )
        if response.status_code == 200:
            return response.text
        else:
            return None


# 解析:
class Parser:
    def parse(self):
        pass



# 数据处理
class DataOutPut:
    def save(self, datas):
        with open(" ")
        for data in datas:


# 调度
class Scheduling:
    def __init__(self):
        self.downloader = Downloader()
        self.url_manager = URLManager()
        self.parser = Parser()
        self.data_saver = DataOutPut()

    def run(self, url): # 用于调度
        self.url_manager.add_new_url(url) # 添加

        while self.url_manager.has_new_url(): # 判断是否还有url.
            url = self.url_manager.get_new_url() # 获取一个url
            html = self.downloader.download(url)
            data, urls = self.parser.parse() # 解析数据, 从中拿到数据和urls
            # 保存数据
            self.data_saver.save(data)
            # 添加新的urls到URLManager中
            self.url_manager.add_new_urls(urls)



if __name__ == '__main__':
    scheduling = Scheduling()
    scheduling.run('')
