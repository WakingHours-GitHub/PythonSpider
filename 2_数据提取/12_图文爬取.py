import requests
from fake_useragent import UserAgent
from lxml import etree

url = "http://www.farmer.com.cn/2022/07/27/99897226.html"


headers = {
    'User-Agent': UserAgent().chrome

}


resp = requests.get(url, headers=headers)
resp.encoding = 'UTF-8'

# 这次练习我们使用xpath编写

print(resp.text)


# xpath中, string和text()的区别.
# string是字符串化, 当一个标签嵌套另一个标签时, 我们想要取出所有的文本, 此时就是用string()
# text()只是针对当前标签, 获取标签内的内容.


resp.close()


