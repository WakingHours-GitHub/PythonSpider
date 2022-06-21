# 例如
# https://sam.huat.edu.cn:8443/selfservice/
# 你的连接不是专用连接

import requests

url = "https://sam.huat.edu.cn:8443/selfservice/"
# resp = requests.get(url)
resp = requests.get(url, verify=False) # 会产生一个警告

print(resp.text) # 直接报错requests.exceptions.SSLError:
# certificate verify failed 认证失败














