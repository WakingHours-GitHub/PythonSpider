"""
http是无状态的.




"""


from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.parse import urlencode
from urllib.request import build_opener
from urllib.request import HTTPCookieProcessor



headers = {
    "user-agent": UserAgent().chrome
}
# 登录
login_url = ""
from_data = {
    "user": "123",
    "password": "123"
}
# 转成bytes
f_data = urlencode(from_data).encode()
# 构造请求头
request = Request(login_url, headers=headers, data=f_data)
# response = urlopen(request) # Httphandeler无法维持会话, 所以我们需要更换handeler
# 自己构建opener:
handler = HTTPCookieProcessor() # 构建带cookie保持的handler
# 使用CookieJar()专门用来处理cookie的.
opener = build_opener(handler) # 此时opener会自动保持cookie
response = opener.open(request) #

print(response.read().decode())

# 访问页面
info_url = ""
request = Request(info_url, headers=headers)
response = opener.open(request)
print(response.read().decode())





