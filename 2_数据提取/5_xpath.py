"""
xpath也是数据提取的工具


xpath中标签与标签之间的关系:
    父节点, 子节点, 兄弟, 前辈, 后代

选取节点:
    表达式             描述
    nodename        选取此节点的所有子节点
    /               从跟节点选取, 或者表示选取节点后面的内容
    //              从匹配选择的当前节点选择文档中的节点, 而不考虑他们的位置, 从任意一个位置开始
    .               选取当前节点
    ..              选取当前节点的父节点
    @               选取属性.

    通配符:
    *           匹配任何元素节点
    @*          匹配任何属性节点
    node()      匹配任何类型的节点

    选取若干路径
    |           使用 | 可以选取若干个路径.

    谓语:
    筛选过滤.






"""

from lxml import etree # 使用etree转换成dom结构
import requests
from fake_useragent import UserAgent



url = "https://www.qidian.com/rank/yuepiao/year2022-month07-page1/"

headers = {
    'User-Agent': UserAgent().random
}
resp = requests.get(url, headers=headers)

e = etree.HTML(resp.text) # 进行解析, 返回dom对象
print(type(e)) # <class 'lxml.etree._Element'>

# 使用e.xpath()使用xpath语法进行寻找.
# 匹配所有的li节点, 这样返回的就是所有找到的名字
names = e.xpath('//*[@id="book-img-text"]/ul/li/div[2]/h2/a/text()')
# text()返回标签中的值
# 否则返回element对象.
authors = e.xpath('//div[@class="book-mid-info"]/p/a[@class="name"]/text()')
print(names)
print(authors)



# 使用字典推导式快速组合字典
book_dict = {name: author for name, author in zip(names, authors)}
print(book_dict)























