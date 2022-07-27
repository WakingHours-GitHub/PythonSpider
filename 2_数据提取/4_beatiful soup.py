"""
BS也是数据提取的工具
    应用于HTML和XML等放回去请求方式.






"""

from bs4 import BeautifulSoup
from bs4.element import Comment

str = """
<title>尚学堂</title>
<div class="info" float='left'>Welcome to SXT</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <a href='www.bjsxt.cn'></a>
    <strong><!--没用--></strong>
</div>
"""

# 创建BeautifulSoup对象
soup = BeautifulSoup(str, "lxml")

# 直接使用 soup.标签, 就可以拿到标签和其中的值
print(soup.title) # <title>尚学堂</title>
print(soup.div) # <div class="info" float="left">Welcome to SXT</div>

# 拿到属性
# soup.标签.attrs返回一个字典, 获取标签中的所有属性
print(soup.div.attrs) # {'class': ['info'], 'float': 'left'}
# 拿取单独的一个属性
print(soup.div.get('class')) # ['info']
print(soup.div['float']) # left

print(soup.a['href']) #

# 获取标签中内容
print(soup.div.string) # Welcome to SXT
print(soup.title.text) # 尚学堂

# 注释的问题:
print(soup.strong.string) # 没用
print(soup.strong.text) # 空 可见text不解析注释

# 判断是否是注释
print(type(soup.title.string)) # <class 'bs4.element.NavigableString'>

print(type(soup.strong.string)) # <class 'bs4.element.Comment'>

# 判断:
if type(soup.strong.string) == Comment:
    print(soup.strong.string)
    # 获取整个标签, 这样更加方便我们去处理.
    print(soup.strong.prettify) # <bound method Tag.prettify of <strong><!--没用--></strong>>

else:
    print(soup.strong.text)



# 过滤器:
# soup.find_all()
print(soup.find_all('title')) #  [<title>尚学堂</title>]
print(soup.find_all(id_='title')) # [] 没有找到
print(soup.find_all(class_='info')) #
# [<div class="info" float="left">Welcome to SXT</div>, <div class="info" float="right">
# <span>Good Good Study</span>
# <a href="www.bjsxt.cn"></a>
# <strong><!--没用--></strong>
# </div>] # 返回一个列表

# attrs也可以传入一个字典, 找到标签对应属性的标签.
print(soup.find_all('div', attrs={'float': 'left'})) # [<div class="info" float="left">Welcome to SXT</div>]



# 还支持CSS选择器 与css选择器一样, 用于选择标签的
# chrome一般支持直接复制.
# soup.select()

print(soup.select('title')) # [<title>尚学堂</title>]
print(soup.select('#title')) # 选择class='title'的标签
print(soup.select('.info')) #  选择id=info的标签

# 标签的嵌套查找
print(soup.select("div span")) #  [<span>Good Good Study</span>]
print(soup.select("div > span")) # [<span>Good Good Study</span>]

# 可以按照index去查找, select查找后的对象还是一个soup对象, 可以继续使用select
print(soup.select('div')[1].select('span')) # [<span>Good Good Study</span>]


