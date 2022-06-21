"""
哪些地方需要POST请求?
    1. 登录注册
    2. 需要传输大文本内容

方法:
    resp = requests.post(url, data)
    data参数接收一个字典
    requests模块发送POST请求, 和get参数一样





"""
# 解析json数据
# https://www.json.cn/

# POST请求练习:
import json

import requests
import sys

url = "http://fy.iciba.com/" # 已经失效
# 所以这里只模拟流程

class King(object):
    def __init__(self, word):
        self.url = "http://fy.iciba.com/"
        self.word = word
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"
        }
        self.data = { # 通过抓包工具, 推理
            "f": "auto",
            "t": "auto",
            "w": self.word
        }

    def post_data(self):
        # 使用POST请求, 发送带参数的请求
        # data是一个带有参数的字典
        resp = requests.post(self.url, self.data, self.headers)
        return resp.content # 返回字节文件

    def parse_data(self, data): #  解析数据
        # 通过抓波工具, 分析数据
        # 将json字符串转换成python字典
        dict_data = json.loads(data)
        # 拿到返回的响应json
        # 有经验的发现, 发现不同的响应头可以加if条件, 进行判断,
        # 这里我们直接用try except: 做判断捕捉即可
        # 根据不同的响应头, 使用try捕捉异常
        try:
            print(dict_data['content']['out'])
        except:
            print(dict_data['content']['word_mean'][0])






    def run(self): # 爬虫运行逻辑
        resp = self.post_data()
        # print(resp)
        self.parse_data(resp) # 将返回的json
if __name__ == '__main__':
    # word = input("请输入要翻译的单词或句子")
    # 另一种参数输入的方式
    # print(sys.argv)
    # 在终端中, 输入参数, 直接运行
    word = sys.argv[1]
    king = King(word)
    king.run() # 开启运行逻辑


