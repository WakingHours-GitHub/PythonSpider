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
import requests

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
        resp = requests.post(self.url, self.data, self.headers)

        return resp.content # 返回字节文件

    def parse_data(self): #  解析数据
        # 通过抓波工具, tong'y
        # 将json
        pass

