"""
http: 明文传输
https: http + ssl, 需要证书




"""
import ssl
from urllib.request import Request, urlopen
from fake_useragent import UserAgent

url = "https://www.12306.cn/index/index.html"

headers = {
    'user-agent': UserAgent().chrome
}
request = Request(url, headers=headers)

# 忽略验证证书:
context = ssl._create_unverified_context()
print(context) # <ssl.SSLContext object at 0x00000211ACC56240>
response = urlopen(request, context=context)
response = urlopen(request)

info = response.read().decode()
print(info)
