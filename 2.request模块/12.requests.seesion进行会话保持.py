"""
利用session进行状态保持
作用:
    - 自动处理cookie, 即下次请求会带上前一次的cookie
使用场景:
    - 自动处理连续的多次请求过程中产生的cookie
使用方法:
    session = requests.session() # 实例化session对象
    resp = session.gte()
    resp = session.post()
    直接就用session对象发送get或post请求的参数, 与requests模块发送的请求的参数完全一致

课堂测试:
    使用session完成github登录. 并获取登录后的界面

分析github登录过程
发现是静态_html, 可以利用抓包工具, 返回str
然后利用rte进行正则匹配



"""
import requests
import re


# session

# headers

# url1: 获取token
# 发送请求获取响应
# 正则提取
# url2: 登录
# 构建表单数据
# 发送请求登录

# url3： 验证

def login():
    # session
    session = requests.session()

    # headers
    session.headers = {

    }

    # url1: 获取token
    url1 = "loginURL"
        # 发送请求获取响应
    resp1 = session.get(url1).content.decode() # 因为正则只能对str类型进行匹配, 所以这里, 必须解码
        # 正则提取
        # 给一段 text, 然后截取, 正则匹配, 我们想要仅仅获取我们所需的,那么就分组:(.*?)
    token = re.findall('name="authenticity_token" valuex="(.*?)"', resp1)[0] # 返回一个列表, 我们需要获取, 那么就[0]
    print(token)
    # url2: 登录
    url2 = "https://github.com/session"
        # 构建表单数据
    data = {
        # 从浏览器的抓包工具复制
    }

        # 发送请求登录
    session.post(url2, data=data)
    # 此时session会自动的保持会话
    # 当我们POST后, 我们就已经获得了服务器让我们设置的cookie|
    # 然后session会自动处理cookie, 所以下面在session.get时候
    # session会自动带上cookie

    # url3： 验证
    # 个人界面, 验证:
    url3 = "个人网页"
    resp3 = session.get(url3)

    # 然后看看 title 标题是否是我们个人页面
    # 用来以验证成功
















