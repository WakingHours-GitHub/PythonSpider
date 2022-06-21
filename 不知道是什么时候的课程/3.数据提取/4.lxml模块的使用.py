"""
安装:
    pip install lxml

使用:
    1. 导入lxml的etree库
        from lxml import etree
    2. 利用etree.HTML, 将html字符串(bytes类型或str类型),转换成element对象
    然后调用xpath函数
        html = etree.HTML(test)
        ret_list = html.xpath("XPATH语法")
    3. 返回:
        列表

"""
from lxml import etree

test = """
<div>
    <ul>
        <li class="itemp-1">
            <a href="link1.html">first item</a>
        </li>
        <li class="itemp-1">
            <a href="link2.html">second item</a>
        </li>
        <li class="itemp-1">
            <a href="link3.html">third item</a>
        </li>
        <li class="itemp-inactive">
            <a href="link4.html">fourth item</a>
        </li>
        <li class="itemp-0">
            <a href="link5.html">fifth item</a>
        </li>
    </ul>
</div>
"""

# 创建element对象
html = etree.HTML(test) # 这里放上一个响应：resp.content
print(html) # <Element html at 0x1d77b133340>
print(dir(html))
# 练习使用xpath语法进行数据提取
#
print(html.xpath('//a[@href="link1.html"]/text()'))  # 返回一个列表
print(html.xpath('//a[@href="link1.html"]/text()'[0])) # 加上索引返回元素

# 拿<a>中的属性值和标签内容
text_list = html.xpath('//a/text()')
href_list = html.xpath('//a/@href')

print(text_list)
print(href_list)
# 组装成字典
# low的一种玩法:
myDict = dict() # 生成空字典
for text in text_list:
    index = text_list.index(text) # list.index(内容) 根据内容查找, 返回index值
    href = href_list[index]
    print(text, href)
    myDict[text] = href
print(myDict)

# 稍微高级的写法:
# 利用zip(list1, list2)函数 -> 以相同的索引遍历list1和list2
# 但是这里有一个问题, 就是一旦这两个可迭代对象长度不同时候, 他们他就会错位
for text, href in zip(text_list, href_list):
    print(text, href)
    myDict[text] = href
print(myDict)

# 但是我们平时不会这么提取数据
# 而是将我们要提取的标签作为一个整体, 然后再里面继续去提取, 这样不会影响到表的标签
el_a_list = html.xpath("//a") # 提取所有的a标签
for el_a in el_a_list:
    print(el_a)  # <Element a at 0x22767e03600> -> 发现是Element所以可以继续调用xpath方法
    print('//text()', el_a.xpath('//text()')) # -> 拿取的是所有文本
    print('/text()', el_a.xpath('/text()'))
    print('./text()', el_a.xpath('./text()')) # 可以
    print('.//text()', el_a.xpath('.//text()')) # 可以
    print('text()', el_a.xpath('text()')) # 可以

"""
我们在以后都是先找到一个div(容器, 模块),然后再xpath提取我们想要的数据
这样每个div之间是没有关联的
"""


















