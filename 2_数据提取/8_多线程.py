"""
queue模块:



"""
import gc
from threading import Thread

import requests
from fake_useragent import UserAgent

from queue import Queue

import lxml
from lxml import etree

# 创建两个队列维护。
url_queue = Queue()  # 创建存储url对象
# queue对象有put()方法和get()方法, 一个是放入, 一个是取
page_queue = Queue()  # 创建存储页面的队列

TOTAL_PAGE_NUM = 1
IS_PROXIES = False
GET_THREAD_NUM = 1
PARSE_THREAD_NUM = 1


class from_url_get_content(Thread):
    """
    用于获取页面源代码的类别
    """

    def __init__(self):
        Thread.__init__(self)  # 继承父类

    def run(self):
        headers = {
            'User-Agent': UserAgent().random
        }
        proxies = None
        if IS_PROXIES:  # 未完善
            proxies = {
                "HTTP": "12."
            }

        while not url_queue.empty():
            # construct requests
            resp = requests.get(url_queue.get(), headers=headers)
            if resp.status_code == 200:  # if access is normal
                # 将请求得到的page放入到page_queue中
                page_queue.put(resp.text)

            resp.close()


class parse_page(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        page = page_queue.get()
        # print(page) # 测试页面是否能拿到
        # 使用xpath解析
        e = etree.HTML(page)
        movie_names = e.xpath('//*[@id="index"]/div[1]/div[1]/div/div/div/div[2]/a/h2/text()')
        # '//*[@id="index"]/div[1]/div[1]/div[1]'
        score = [ele.strip() for ele in e.xpath('//*[@id="index"]/div[1]/div[1]/div/div/div/div[3]/p[1]/text()')]

        print(score)


def main() -> None:
    url = "https://ssr1.scrape.center/page/{}"
    # 添加url到queue中 # add url to queue that storage url
    [url_queue.put(url.format(i)) for i in range(1, TOTAL_PAGE_NUM + 1)]

    # 开启线程:
    # 创建爬虫线程对象
    crawl_list = list()
    for i in range(GET_THREAD_NUM):
        crawl = from_url_get_content()
        crawl_list.append(crawl)
        # 启动线程
        crawl.start()

    # 等待线程, 因为需要等待构造page_queue, 所以需要等待爬虫类全部完成后, 才进行解析数据
    for crawl in crawl_list:
        crawl.join()

    parse_page().start()

    gc.collect()


if __name__ == "__main__":
    main()
