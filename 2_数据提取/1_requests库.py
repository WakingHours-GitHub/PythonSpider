"""
安装requests请求。
get请求, 和post请求.
get请求可以使用显示拼接, 也可以单独传入一个params字典即可
post请求, 传入一个data字典
timeout: 设置超时
代理访问:
    直接使用字典
cookies:
    session自动保存cookies, 维持一个会话.
    使用创建的session对象发送请求, 默认维持会话

ssl
    直接使用verify=False, 屏蔽安全验证证书.

获取相应信息:
    resp.json()             获取相应内容(以json字符串)
    resp.text               获取响应内容(以字符串)
    resp.content            获取响应内容(以字节的方式)
    resp.headers            后去响应头内容
    resp.url                获取访问地址
    resp.encoding           获取网页编码
    resp.request.headers    获取请求头内容
    resp.cookie             获取cookie


"""
import requests
from fake_useragent import UserAgent

headers = {
    'user-agent': UserAgent().chrome
}

url = "http://httpbin.org/get" # 测试网址
params = {
    "wd": "尚学堂"
}

# 使用requests发送get请求
response = requests.get(url, headers=headers, params=params)

print(response.text)


# 使用requests发送post请求
url = "http://httpbin.org/post" # post测试网址

data={
    "user": "123",
    "password": "123"
}
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response.status_code)

# origin": "221.206.110.63",

# 测试代理:
url = "http://httpbin.org/get" # 测试网址
proxies = {
    "http": "114.115.251.155:30001"
}

response = requests.get(url, headers=headers, proxies=proxies)
print(response.text)
print(response.status_code)

# "origin": "114.115.251.155", # 可见, 我们的来源已经切换成代理服务器了.



# SSL证书
url = "http://passport2.chaoxing.com/login?fid=&refer=http://i.mooc.chaoxing.com" # 超新星,
# 安全证书自己做的, 显示不安全
requests.packages.urllib3.disable_warnings() # 忽略安全警告

# verify=False表示忽略证书安全.
response = requests.get(url, headers=headers, verify=False) #
print(response.text)
print(response.status_code)





# cookie
# 使用session保持会话
from_data = {
    '': '',
    '': ''
}
login_url = ""
session = requests.Session()
session.post(login_url)

info_url = ""
session.get(info_url1)


