# requests获取的resp对象, 具有cookies属性, 该属性是一个cookieJar类型
# 如何将其转换为cookie字典呢

import requests
import requests.utils

# 转换方法1
# cookies_dict = requests.utils.dict_from_cookiejar(resp.cookies)

url = "http://www.baidu.com"

resp = requests.get(url)

print(resp.cookies)

cookies_dict = requests.utils.dict_from_cookiejar(resp.cookies)

print(cookies_dict)

# 转换回去
cookies_jar = requests.utils.cookiejar_from_dict(cookies_dict)













