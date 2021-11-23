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

# 创建element对象
html = etree.HTML(test)