import os.path

import requests
from fake_useragent import UserAgent
from lxml import etree

url = "http://www.farmer.com.cn/2022/07/27/99897226.html"

headers = {
    'User-Agent': UserAgent().chrome

}

resp = requests.get(url, headers=headers)
resp.encoding = 'UTF-8'

# print(resp.text) # 打印源代码
# 这次练习我们使用xpath编写
e = etree.HTML(resp.text)
# 使用string获取该div下面所有标签的内容
content = e.xpath('string(//div[@class="article-main"])').strip()  # string是针对当前标签, 以及所有子标签
img_src_list = e.xpath('//p/img/@src') # 返回一个列表, 注意是url是相对还是绝对路径, 这里是绝对路径
# 将文件写入到temp文件夹当中.
if not os.path.exists("./temp"):
    os.mkdir('./temp')
for img_src in img_src_list:
    img_resp = requests.get(img_src, headers=headers)
    with open("./temp/"+img_src.split('/')[-1].__str__(), 'wb') as f:
        f.write(img_resp.content)




# xpath中, string和text()的区别.
# string是字符串化, 当一个标签嵌套另一个标签时, 我们想要取出所有的文本, 此时就是用string()
# text()只是针对当前标签, 获取标签内的内容.


resp.close()
