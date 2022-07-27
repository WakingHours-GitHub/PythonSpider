from fake_useragent import UserAgent
import requests
import re



# 练习
url = "https://weibo.com/"

headers = {
    "User-Agent": UserAgent().chrome,
    "referer": r"https://weibo.com/"
}
# 发送请求
resp = requests.get(url, headers=headers)
resp.encoding = 'gb2312'
print(resp.text)



resp.close()









